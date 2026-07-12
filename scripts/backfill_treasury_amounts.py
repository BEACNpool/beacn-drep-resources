#!/usr/bin/env python3
"""Backfill missing treasury_amount_lovelace from the chain.

The upstream poller scrapes the requested amount out of proposal metadata, and for some actions
it comes back EMPTY. That is not a harmless blank: engine.py cannot run its capacity or
cost-efficiency arithmetic without an amount, so the action trips MISSING_BASELINE_EVIDENCE and
ABSTAINS — no matter how strong the evidence against it is.

On 2026-07-12 that silently neutralised the two largest and most contentious asks on the ballot:

    Withdraw 120,000,000 ada for AlphaGrowth's Cardano PRIME   -> amount blank -> ABSTAIN
    Revised Cardano dOSPO and OMF Program Proposal             -> amount blank -> ABSTAIN

AlphaGrowth already carried independently verified evidence of material duplication AND excessive
cost versus market comparables, and asks ~14x the entire remaining Net Change Limit. It abstained
because of a missing CSV column.

The amount is not a matter of interpretation — it is on-chain, in db-sync's `treasury_withdrawal`
table, which is what the ledger will actually pay out. That is strictly more authoritative than a
number scraped from a proposal document. So we read it from the chain and fill the gap.

Only ever FILLS blanks; never overwrites a value already present. Read-only against relay.
"""
from __future__ import annotations

import csv
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GOV = REPO / "data" / "input" / "governance"
FILES = ("governance_actions_all.csv", "governance_actions_active.csv")

SQL = """
select encode(t.hash,'hex') || '#' || g.index, coalesce(sum(tw.amount),0)::bigint
  from gov_action_proposal g
  join tx t on t.id = g.tx_id
  join treasury_withdrawal tw on tw.gov_action_proposal_id = g.id
 group by 1;
"""


def chain_amounts() -> dict[str, int]:
    remote = ("docker exec -i dbsync-mainnet-postgres "
              "psql -U postgres -d cexplorer -v ON_ERROR_STOP=1 -A -F '|' -t")
    p = subprocess.run(["ssh", "relay", remote], input=SQL, text=True,
                       capture_output=True, check=True)
    out: dict[str, int] = {}
    for line in p.stdout.splitlines():
        if "|" not in line:
            continue
        aid, amt = line.rsplit("|", 1)
        try:
            out[aid.strip()] = int(amt)
        except ValueError:
            continue
    return out


def main() -> int:
    amounts = chain_amounts()
    print(f"db-sync knows the withdrawal amount for {len(amounts)} governance actions")

    total_filled = 0
    for name in FILES:
        path = GOV / name
        if not path.exists():
            continue
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            header = list(reader.fieldnames or [])
            rows = list(reader)

        filled = 0
        for r in rows:
            if r.get("action_type") != "TreasuryWithdrawals":
                continue
            if (r.get("treasury_amount_lovelace") or "").strip():
                continue          # never overwrite an existing value
            amt = amounts.get(r["action_id"])
            if not amt:
                continue
            r["treasury_amount_lovelace"] = str(amt)
            filled += 1
            print(f"  filled {amt / 1e6:>15,.0f} ADA  {(r.get('metadata_title') or '')[:46]}")

        if filled:
            with path.open("w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=header)
                w.writeheader()
                w.writerows(rows)
        print(f"{name}: filled {filled} missing amounts")
        total_filled += filled

    if not total_filled:
        print("no gaps to fill")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
