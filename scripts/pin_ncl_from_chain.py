#!/usr/bin/env python3
"""Pin the Net Change Limit for the current period from admitted public chain evidence.

WHY THIS EXISTS
---------------
`treasury_policy_state.json` gates every directional treasury vote: engine.py requires a
verified NCL with `ncl_lovelace > 0` before it will vote YES or NO on a withdrawal. It shipped
as a hand-written fail-closed placeholder (`ncl_lovelace: null`) with NO producer, so all
active treasury withdrawals dead-ended at NEEDS_MORE_INFO forever, regardless of merit.

THE TRAP THIS SCRIPT AVOIDS
---------------------------
The original gate demanded `verification_status == "verified_on_chain"`, meaning ENACTED
ledger state. **No NCL can ever satisfy that.** Under the Constitution the NCL is set by an
*Info* governance action, and Info actions change no ledger state -- they ALWAYS expire and
can NEVER be enacted. The gate was therefore unsatisfiable by construction: a permanent
freeze on all treasury funding, dressed up as caution.

So "verified" here means the strongest evidence the chain can actually offer:

  1. an Info action whose anchor document is byte-verified against the on-chain
     `voting_anchor.data_hash` (blake2b-256) -- the document is authentic, not a copy;
  2. whose stated period covers the epoch we are voting in;
  3. which won a majority of PARTICIPATING DRep stake (Yes > No, abstains excluded);
  4. and, where several cover the same period, the LATEST such action -- NCL documents
     explicitly supersede prior NCLs for the same period.

We record `verification_status: "verified_onchain_info_action"` -- deliberately NOT
"verified_on_chain", so nobody can later mistake this for enacted ledger state. The caveat
that Info actions never formally ratify travels WITH the number, into every rationale.

FAILS CLOSED. If no action hash-verifies, or none covers this epoch, or the leader did not
win its vote, the existing fail-closed placeholder is LEFT UNTOUCHED. This script will never
invent a limit -- pinning a wrong NCL would unblock treasury voting against a wrong capacity
ceiling, which is worse than abstaining.

Usage:
  python3 scripts/pin_ncl_from_chain.py            # write if verified
  python3 scripts/pin_ncl_from_chain.py --dry-run  # report only, touch nothing
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GOV = REPO / "data" / "input" / "governance"
ANCHORS = GOV / "anchors"
STATE_PATH = GOV / "treasury_policy_state.json"

SCHEMA_VERSION = "treasury-policy-state-v1"
VERIFIED = "verified_onchain_info_action"

# Candidate NCL Info actions: type, ids, anchor hash, proposal epoch, and the stake-weighted
# DRep tally at expiry. One query -- the engine must not depend on a live chain scrape per action.
SQL = """
\\pset footer off
with tip as (select max(epoch_no) as e from block where epoch_no is not null),
cand as (
  select g.id,
         encode(t.hash,'hex') as tx_id,
         g.index as ix,
         encode(va.data_hash,'hex') as anchor_hash,
         va.url as anchor_url,
         (select epoch_no from block b join tx t2 on t2.block_id=b.id where t2.id=g.tx_id) as proposed_epoch,
         g.expiration
    from gov_action_proposal g
    join tx t on t.id = g.tx_id
    left join voting_anchor va on va.id = g.voting_anchor_id
   where g.type = 'InfoAction' and va.data_hash is not null
)
select c.id, c.tx_id, c.ix, c.anchor_hash, c.anchor_url, c.proposed_epoch, (select e from tip) as tip_epoch,
       coalesce(sum(dd.amount) filter (where vp.vote='Yes'), 0)::bigint as yes_stake,
       coalesce(sum(dd.amount) filter (where vp.vote='No'), 0)::bigint  as no_stake,
       count(*) filter (where vp.vote='Yes') as yes_n,
       count(*) filter (where vp.vote='No')  as no_n
  from cand c
  left join voting_procedure vp on vp.gov_action_proposal_id = c.id and vp.voter_role='DRep'
  left join drep_hash dh on dh.id = vp.drep_voter
  left join drep_distr dd on dd.hash_id = dh.id
       and dd.epoch_no = (select max(epoch_no) from drep_distr where epoch_no <= c.expiration)
 group by c.id, c.tx_id, c.ix, c.anchor_hash, c.anchor_url, c.proposed_epoch
 order by c.proposed_epoch desc;
"""

# "300,000,000,000,000 lovelace" / "300 million ADA" / "₳300,000,000"
LOVELACE_RE = re.compile(r"([\d][\d,\s]{6,})\s*lovelace", re.I)
EPOCH_RANGE_RE = re.compile(r"epochs?\s*(\d{3,4})\s*(?:to|-|–|—|through)\s*(?:epoch\s*)?(\d{3,4})", re.I)


def run_sql(sql: str) -> str:
    # ssh joins argv into a single remote SHELL command, so the '|' field separator MUST be
    # quoted -- unquoted it becomes a pipe and psql dies with exit 127.
    remote = ("docker exec -i dbsync-mainnet-postgres "
              "psql -U postgres -d cexplorer -v ON_ERROR_STOP=1 -A -F '|' -t")
    p = subprocess.run(["ssh", "relay", remote], input=sql, text=True,
                       capture_output=True, check=True)
    return p.stdout


def anchor_bytes_for(tx_id: str, ix: int, anchor_hash: str) -> bytes | None:
    """Return the cached anchor doc whose blake2b-256 MATCHES the on-chain hash.

    We do not trust filenames or titles -- only the hash. A document that does not hash to the
    on-chain anchor is not the document the chain committed to, and is discarded.
    """
    for path in ANCHORS.glob("*.bin"):
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if hashlib.blake2b(raw, digest_size=32).hexdigest() == anchor_hash:
            return raw
    return None


def parse_ncl(raw: bytes) -> tuple[int | None, tuple[int, int] | None]:
    text = raw.decode("utf-8", "ignore")
    lovelace = None
    m = LOVELACE_RE.search(text)
    if m:
        digits = re.sub(r"[,\s]", "", m.group(1))
        if digits.isdigit():
            lovelace = int(digits)
    period = None
    e = EPOCH_RANGE_RE.search(text)
    if e:
        period = (int(e.group(1)), int(e.group(2)))
    return lovelace, period


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    rows = [r for r in run_sql(SQL).strip().splitlines() if r.strip()]
    tip = None
    candidates = []
    for row in rows:
        f = row.split("|")
        if len(f) < 11:
            continue
        gid, tx_id, ix, anchor_hash, url, proposed, tip_epoch, yes_s, no_s, yes_n, no_n = f[:11]
        tip = int(tip_epoch)
        raw = anchor_bytes_for(tx_id, int(ix), anchor_hash)
        if raw is None:
            continue  # anchor not cached, or does not hash-verify -> not admissible evidence
        lovelace, period = parse_ncl(raw)
        if not lovelace or not period:
            continue  # not an NCL document
        candidates.append({
            "gid": int(gid), "tx_id": tx_id, "ix": int(ix), "anchor_hash": anchor_hash,
            "anchor_url": url, "proposed_epoch": int(proposed),
            "ncl_lovelace": lovelace, "period": period,
            "yes_stake": int(yes_s or 0), "no_stake": int(no_s or 0),
            "yes_n": int(yes_n or 0), "no_n": int(no_n or 0),
        })

    if tip is None:
        print("FAIL: could not read chain tip", file=sys.stderr)
        return 1

    # 2. period must cover the epoch we are actually voting in
    covering = [c for c in candidates if c["period"][0] <= tip <= c["period"][1]]
    # 3. must have won a majority of PARTICIPATING DRep stake
    passed = [c for c in covering if c["yes_stake"] > c["no_stake"] and c["yes_stake"] > 0]
    # 4. latest wins -- NCL documents supersede earlier ones for the same period
    passed.sort(key=lambda c: c["proposed_epoch"], reverse=True)

    print(f"tip epoch {tip} | {len(candidates)} hash-verified NCL docs | "
          f"{len(covering)} cover this epoch | {len(passed)} won their vote")
    for c in covering:
        tot = c["yes_stake"] + c["no_stake"]
        pct = (100.0 * c["yes_stake"] / tot) if tot else 0.0
        mark = "WON " if c["yes_stake"] > c["no_stake"] else "LOST"
        print(f"  [{mark}] epochs {c['period'][0]}-{c['period'][1]}  "
              f"{c['ncl_lovelace'] / 1e12:.0f}M ADA  yes {pct:.1f}% stake "
              f"({c['yes_n']}y/{c['no_n']}n)  {c['tx_id'][:12]}…#{c['ix']}")

    if not passed:
        print("\nNo NCL action hash-verifies, covers this epoch, AND won its vote.")
        print("Leaving the fail-closed placeholder untouched. Treasury stays at NEEDS_MORE_INFO.")
        return 2

    w = passed[0]
    tot = w["yes_stake"] + w["no_stake"]
    pct = round(100.0 * w["yes_stake"] / tot, 2) if tot else 0.0

    # Spend must be measured over the NCL's OWN period. The portfolio previously charged a
    # rolling 73-epoch window against it, which swept in withdrawals enacted BEFORE this period
    # began (they belong to the prior NCL) -- 638.5M ADA vs the true 291.4M at epoch 642. That
    # overstatement drove remaining capacity to zero and blocked every proposal on a phantom.
    #
    # INTERPRETATION (not a chain fact): we read the limit as GROSS treasury withdrawals enacted
    # within the period. The anchor sizes the NCL against prior-year inflows but does not define
    # the measurement basis; gross is the conservative reading. Netting inflows against it would
    # create far more headroom, so we do not do it without an explicit decision.
    spend_sql = (
        "select coalesce(sum(tw.amount),0)::bigint from treasury_withdrawal tw "
        "join gov_action_proposal g on g.id = tw.gov_action_proposal_id "
        f"where g.enacted_epoch is not null and g.enacted_epoch >= {int(w['period'][0])} "
        f"and g.enacted_epoch <= {int(w['period'][1])};"
    )
    spent = int((run_sql(spend_sql).strip() or "0").splitlines()[0])
    remaining = max(0, w["ncl_lovelace"] - spent)

    state = {
        "schema_version": SCHEMA_VERSION,
        "verification_status": VERIFIED,
        "ncl_lovelace": w["ncl_lovelace"],
        "period_start_epoch": w["period"][0],
        "period_end_epoch": w["period"][1],
        "source_action_id": f"{w['tx_id']}#{w['ix']}",
        "source_anchor_hash": w["anchor_hash"],
        "source_anchor_url": w["anchor_url"],
        "verified_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "verified_at_epoch": tip,
        # Measured over the NCL's own period — NOT a rolling window. See note above.
        "withdrawals_in_period_lovelace": spent,
        "remaining_capacity_lovelace": remaining,
        "spend_basis": "gross_treasury_withdrawals_enacted_within_period",
        "drep_support": {
            "yes_stake_lovelace": w["yes_stake"],
            "no_stake_lovelace": w["no_stake"],
            "yes_pct_of_participating_stake": pct,
            "yes_dreps": w["yes_n"],
            "no_dreps": w["no_n"],
        },
        "caveat": (
            "Set by an Info governance action. Info actions change no ledger state and can NEVER "
            "be enacted -- they always expire -- so no formally ratified NCL exists or can exist. "
            "This is the strongest available public chain evidence: an anchor document byte-verified "
            "against its on-chain blake2b-256 hash, covering the current epoch, which won a majority "
            "of participating DRep stake. It is NOT enacted ledger state, and the majority may fall "
            "short of the supermajority other action types require. Published with every treasury "
            "rationale that relies on it."
        ),
        "note": (
            "Produced by scripts/pin_ncl_from_chain.py from relay db-sync. Re-run each cycle: a later "
            "NCL action covering the same period supersedes this one."
        ),
    }

    print(f"\nOPERATIVE NCL: {w['ncl_lovelace']:,} lovelace "
          f"({w['ncl_lovelace'] / 1e12:.0f}M ADA), epochs {w['period'][0]}-{w['period'][1]}")
    print(f"  source    {w['tx_id']}#{w['ix']}")
    print(f"  anchor    {w['anchor_hash']}  (blake2b-256 VERIFIED)")
    print(f"  support   {pct}% of participating DRep stake")
    print(f"  spent     {spent / 1e12:.1f}M ADA enacted within epochs "
          f"{w['period'][0]}-{w['period'][1]} (gross)")
    print(f"  REMAINING {remaining / 1e12:.1f}M ADA of capacity")

    if args.dry_run:
        print("\n--dry-run: nothing written.")
        return 0

    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    print(f"\nwrote {STATE_PATH.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
