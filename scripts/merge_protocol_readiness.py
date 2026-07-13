#!/usr/bin/env python3
"""Merge independently researched protocol-readiness evidence into the engine's CSV.

Why this file exists: `protocol_readiness_profiles.csv` contained only a header row. With no
readiness evidence at all, the engine could not re-derive its own YES on the 'van Rossem' hard fork
and fell to ABSTAIN with MISSING_PROTOCOL_READINESS_EVIDENCE — a divergence against a vote BEACN had
already cast on the single most consequential action type on Cardano.

The gap was BEACN's, not the proposal's. So it was closed by doing the research, not by relaxing a
gate. The load-bearing checks were measured against the chain rather than taken from the proposer:

  * mainnet sits at protocol_major 10; the ask is 11 -> the version guardrails provably hold
  * Preview and PreProd are ALREADY running protocol_major 11 on-chain -> the fork is executed,
    not merely promised
  * SPO signalling by block production (stake-proportional, so an unbiased estimator of active
    stake) rose 85.71% -> 92.58% across epochs 638-642, clearing the Constitution's 85% bar

`security_review_pass` is written as UNKNOWN, deliberately. The anchor asserts that audits were
undertaken but cites no document, and no audit could be found. On a hard fork that is the weakest
point in the package, and it is recorded as an open question rather than quietly rounded up to yes.
Missing evidence never becomes negative evidence here — but it never becomes positive evidence either.

Run: merge_protocol_readiness.py <researched.json>
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CSV_PATH = REPO / "data/input/governance/decision_support/protocol_readiness_profiles.csv"
OWNER = "beacn-independent-research"


def main() -> int:
    data = json.loads(Path(sys.argv[1]).read_text())
    aid = data["action_id"]
    fields = data["fields"]

    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        header = list(reader.fieldnames or [])
        rows = [r for r in reader if r.get("action_id") != aid]   # replace, never duplicate

    refs = sorted({s["url"] for item in fields.values() for s in (item.get("sources") or [])})

    row = {"action_id": aid, "action_family": "hardfork"}
    for col in header:
        if col in ("action_id", "action_family"):
            continue
        if col in fields:
            row[col] = fields[col]["value"]
        elif col == "evidence_status":
            row[col] = data.get("evidence_status", "partial")
        elif col == "evidence_refs":
            row[col] = json.dumps(refs, separators=(",", ":"))
        elif col == "owner":
            row[col] = OWNER
        elif col == "status":
            row[col] = "verified_pinned_public_sources"
        else:
            row[col] = ""

    rows.append(row)
    with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header)
        w.writeheader()
        w.writerows(rows)

    verified = sum(1 for c in header if row.get(c) == "yes")
    print(f"wrote readiness row for {aid}")
    print(f"  {verified} checks verified; security_review_pass={row.get('security_review_pass')}; "
          f"affirmative_blocker={row.get('affirmative_blocker')}")
    print(f"  {len(refs)} pinned public sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
