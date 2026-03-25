#!/usr/bin/env python3
import csv
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GOV_CSV = ROOT / "data" / "input" / "governance" / "governance_actions_all.csv"
OUT_BASE = ROOT / "data" / "history" / "drep_votes"

SQL = r"""
COPY (
  select
    encode(atx.hash,'hex') as action_tx_hash,
    gap.index as cert_index,
    dh.view as drep_id,
    vp.vote::text as vote,
    encode(vtx.hash,'hex') as vote_tx_hash,
    vb.time as vote_time_utc,
    vb.epoch_no as vote_epoch,
    vb.slot_no as vote_slot
  from public.voting_procedure vp
  join public.gov_action_proposal gap on gap.id=vp.gov_action_proposal_id
  join public.tx atx on atx.id=gap.tx_id
  join public.tx vtx on vtx.id=vp.tx_id
  join public.block vb on vb.id=vtx.block_id
  left join public.drep_hash dh on dh.id=vp.drep_voter
  where vp.voter_role='DRep'
  order by vb.time asc, vp.id asc
) TO STDOUT WITH CSV HEADER
"""


def run_sql_over_relay() -> str:
    cmd = [
        "ssh",
        "relay",
        "docker",
        "exec",
        "-i",
        "dbsync-mainnet-postgres",
        "psql",
        "-U",
        "postgres",
        "-d",
        "cexplorer",
        "-v",
        "ON_ERROR_STOP=1",
    ]
    p = subprocess.run(cmd, input=SQL, check=True, capture_output=True, text=True)
    return p.stdout


def load_action_map() -> dict[tuple[str, str], str]:
    out = {}
    with GOV_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = ((r.get("tx_hash") or "").lower(), str(r.get("cert_index") or ""))
            if key[0]:
                out[key] = r.get("action_id") or ""
    return out


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = OUT_BASE / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    action_map = load_action_map()
    raw_csv = run_sql_over_relay()

    raw_path = out_dir / "relay_drep_votes_raw.csv"
    raw_path.write_text(raw_csv, encoding="utf-8")

    norm_path = out_dir / "drep_vote_history.csv"
    rows = []
    with raw_path.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key = ((r.get("action_tx_hash") or "").lower(), str(r.get("cert_index") or ""))
            rows.append(
                {
                    "snapshot_at_utc": ts,
                    "action_id": action_map.get(key, ""),
                    "action_tx_hash": r.get("action_tx_hash", "").lower(),
                    "cert_index": r.get("cert_index", ""),
                    "drep_id": r.get("drep_id", ""),
                    "vote": (r.get("vote") or "").upper(),
                    "vote_tx_hash": (r.get("vote_tx_hash") or "").lower(),
                    "vote_time_utc": r.get("vote_time_utc", ""),
                    "vote_epoch": r.get("vote_epoch", ""),
                    "vote_slot": r.get("vote_slot", ""),
                }
            )

    fields = [
        "snapshot_at_utc",
        "action_id",
        "action_tx_hash",
        "cert_index",
        "drep_id",
        "vote",
        "vote_tx_hash",
        "vote_time_utc",
        "vote_epoch",
        "vote_slot",
    ]
    with norm_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    latest = OUT_BASE / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    (latest / "drep_vote_history.csv").write_text(norm_path.read_text(encoding="utf-8"), encoding="utf-8")

    summary = {
        "snapshot_at_utc": ts,
        "rows": len(rows),
        "distinct_actions": len({r["action_id"] for r in rows if r["action_id"]}),
        "distinct_dreps": len({r["drep_id"] for r in rows if r["drep_id"]}),
        "unmapped_rows": sum(1 for r in rows if not r["action_id"]),
        "paths": {
            "raw_csv": str(raw_path.relative_to(ROOT)),
            "normalized_csv": str(norm_path.relative_to(ROOT)),
            "latest_csv": str((latest / "drep_vote_history.csv").relative_to(ROOT)),
        },
    }
    (out_dir / "manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    (latest / "manifest.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary))


if __name__ == "__main__":
    main()
