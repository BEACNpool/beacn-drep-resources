#!/usr/bin/env python3
import csv
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_BASE = ROOT / "data" / "history" / "governance_metrics"

Q_TIP = """
select b.block_no, encode(b.hash,'hex') as block_hash, b.time
from public.block b
order by b.block_no desc nulls last
limit 1;
"""

Q_RECIPIENT_REPEAT = """
COPY (
  with tw as (
    select
      tw.id,
      tw.gov_action_proposal_id,
      tw.stake_address_id,
      tw.amount,
      sa.view as stake_address,
      gap.type::text as action_type,
      encode(tx.hash,'hex') as action_tx_hash,
      gap.index as cert_index,
      b.time as proposal_time,
      b.epoch_no as proposal_epoch
    from public.treasury_withdrawal tw
    join public.gov_action_proposal gap on gap.id = tw.gov_action_proposal_id
    join public.tx tx on tx.id = gap.tx_id
    join public.block b on b.id = tx.block_id
    join public.stake_address sa on sa.id = tw.stake_address_id
  )
  select
    stake_address,
    count(*) as proposal_count,
    sum(amount) as total_lovelace,
    min(proposal_time) as first_seen,
    max(proposal_time) as last_seen,
    string_agg(action_tx_hash, ';' order by proposal_time desc) as action_tx_hashes
  from tw
  group by stake_address
  having count(*) > 1
  order by total_lovelace desc
) TO STDOUT WITH CSV HEADER
"""

Q_ACTION_VOTE_PROFILE = """
COPY (
  select
    encode(atx.hash,'hex') as action_tx_hash,
    gap.index as cert_index,
    gap.type::text as action_type,
    b.epoch_no as proposal_epoch,
    sum(case when vp.voter_role='DRep' and vp.vote='Yes' then 1 else 0 end) as drep_yes,
    sum(case when vp.voter_role='DRep' and vp.vote='No' then 1 else 0 end) as drep_no,
    sum(case when vp.voter_role='DRep' and vp.vote='Abstain' then 1 else 0 end) as drep_abstain,
    count(*) filter (where vp.voter_role='DRep') as drep_total_votes
  from public.gov_action_proposal gap
  join public.tx atx on atx.id = gap.tx_id
  join public.block b on b.id = atx.block_id
  left join public.voting_procedure vp on vp.gov_action_proposal_id = gap.id
  group by atx.hash, gap.index, gap.type, b.epoch_no
  order by b.epoch_no desc, action_tx_hash
) TO STDOUT WITH CSV HEADER
"""

Q_TREASURY_FLOW_6M = """
select
  coalesce((
    select sum(tx.fee)::bigint
    from public.tx tx
    join public.block b on b.id = tx.block_id
    where b.time >= (now() at time zone 'utc') - interval '180 days'
  ),0) as chain_fees_6m_lovelace,
  coalesce((
    select sum(tw.amount)::bigint
    from public.treasury_withdrawal tw
    join public.gov_action_proposal gap on gap.id = tw.gov_action_proposal_id
    join public.tx tx on tx.id = gap.tx_id
    join public.block b on b.id = tx.block_id
    where b.time >= (now() at time zone 'utc') - interval '180 days'
  ),0) as treasury_withdrawals_6m_lovelace;
"""

Q_WITHDRAWALS_73E = """
with tip as (
  select max(epoch_no) as current_epoch from public.block
), w as (
  select tw.amount::bigint as amount_lovelace, b.epoch_no
  from public.treasury_withdrawal tw
  join public.gov_action_proposal gap on gap.id = tw.gov_action_proposal_id
  join public.tx tx on tx.id = gap.tx_id
  join public.block b on b.id = tx.block_id
  cross join tip
  where b.epoch_no between greatest(tip.current_epoch - 72, 0) and tip.current_epoch
)
select (select current_epoch from tip) as current_epoch,
       coalesce(sum(amount_lovelace),0) as withdrawals_73e_lovelace
from w;
"""


def _run_sql(sql: str, tuples_only: bool = False) -> str:
    cmd = [
        "ssh", "relay", "docker", "exec", "-i", "dbsync-mainnet-postgres",
        "psql", "-U", "postgres", "-d", "cexplorer", "-v", "ON_ERROR_STOP=1"
    ]
    if tuples_only:
        cmd.extend(["-A", "-t"])
    p = subprocess.run(cmd, input=sql, text=True, capture_output=True, check=True)
    return p.stdout


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _write_csv(path: Path, text: str) -> int:
    path.write_text(text, encoding="utf-8")
    with path.open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


def main() -> None:
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_dir = OUT_BASE / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    tip_raw = _run_sql(Q_TIP, tuples_only=True)
    tip_lines = [x for x in tip_raw.strip().splitlines() if x.strip()]
    tip_parts = tip_lines[0].split("|") if tip_lines else ["", "", ""]
    tip = {
        "block_no": tip_parts[0].strip() if len(tip_parts) > 0 else "",
        "block_hash": tip_parts[1].strip() if len(tip_parts) > 1 else "",
        "block_time": tip_parts[2].strip() if len(tip_parts) > 2 else "",
    }

    recip_path = out_dir / "recipient_repeat_risk.csv"
    votes_path = out_dir / "action_vote_profile.csv"

    recip_rows = _write_csv(recip_path, _run_sql(Q_RECIPIENT_REPEAT))
    vote_rows = _write_csv(votes_path, _run_sql(Q_ACTION_VOTE_PROFILE))

    flow_raw = _run_sql(Q_TREASURY_FLOW_6M, tuples_only=True).strip()
    flow_parts = (flow_raw.split("|") if flow_raw else ["0", "0"])
    chain_fees_6m = int((flow_parts[0] or "0").strip())
    treasury_out_6m = int((flow_parts[1] or "0").strip())
    w73_raw = _run_sql(Q_WITHDRAWALS_73E, tuples_only=True).strip()
    w73_parts = (w73_raw.split("|") if w73_raw else ["0", "0"])
    current_epoch = int((w73_parts[0] or "0").strip())
    withdrawals_73e = int((w73_parts[1] or "0").strip())

    treasury_tax_assumed = 0.20
    treasury_fee_inflow_6m = int(chain_fees_6m * treasury_tax_assumed)
    flow = {
        "window_days": 180,
        "window_epochs": 73,
        "current_epoch": current_epoch,
        "withdrawals_73e_lovelace": withdrawals_73e,
        "chain_fees_6m_lovelace": chain_fees_6m,
        "treasury_tax_assumed": treasury_tax_assumed,
        "treasury_fee_inflow_6m_lovelace": treasury_fee_inflow_6m,
        "treasury_withdrawals_6m_lovelace": treasury_out_6m,
        "outflow_inflow_ratio": round((treasury_out_6m / treasury_fee_inflow_6m), 6) if treasury_fee_inflow_6m > 0 else None,
    }
    flow_path = out_dir / "treasury_flow_6m.json"
    flow_path.write_text(json.dumps(flow, indent=2) + "\n", encoding="utf-8")

    receipt = {
        "artifact_id": f"governance-risk-metrics-{ts}",
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "source": {
            "mode": "dbsync",
            "network": "cardano-mainnet",
            "node": "relay",
            "tip": tip,
        },
        "query": {
            "files": [
                "scripts/export_governance_risk_metrics.py::Q_RECIPIENT_REPEAT",
                "scripts/export_governance_risk_metrics.py::Q_ACTION_VOTE_PROFILE",
            ],
            "params": {},
        },
        "outputs": [
            {
                "path": str(recip_path.relative_to(ROOT)),
                "rows": recip_rows,
                "sha256": _sha256(recip_path),
            },
            {
                "path": str(votes_path.relative_to(ROOT)),
                "rows": vote_rows,
                "sha256": _sha256(votes_path),
            },
            {
                "path": str(flow_path.relative_to(ROOT)),
                "rows": 1,
                "sha256": _sha256(flow_path),
            },
        ],
        "notes": "Repeat-recipient and vote-profile metrics for governance risk triage. Use tx hashes for independent replay via db-sync/Koios/Blockfrost.",
    }

    (out_dir / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

    latest = OUT_BASE / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    for p in [recip_path, votes_path, flow_path, out_dir / "receipt.json"]:
        (latest / p.name).write_text(p.read_text(encoding="utf-8"), encoding="utf-8")

    print(json.dumps({
        "out_dir": str(out_dir),
        "recipient_repeat_rows": recip_rows,
        "action_vote_rows": vote_rows,
        "tip": tip,
    }))


if __name__ == "__main__":
    main()
