#!/usr/bin/env python3
"""Pull the anchor hash the CHAIN records for every vote BEACN has cast.

Why this is load-bearing.

The public site invites anyone to verify that BEACN's published reasoning is the reasoning it
committed to when it voted. That check is only meaningful if the hash it compares against comes
from the VOTE TRANSACTION — i.e. from the chain. If instead we hand the page a hash we computed
ourselves from the file we are serving today, the "check" degenerates into hashing a file and
comparing it to its own hash: it passes always, proves nothing, and is worse than no check at all
because it wears the costume of one.

That is exactly what nearly shipped on 2026-07-12. Re-running the engine on fresh evidence rewrote
every rationale, so `rationale_anchor_hash` became "today's hash of today's text" rather than "the
hash sitting in the vote tx". The anchored copies at /r/<hash>.md are content-addressed and
immutable, so the ORIGINAL reasoning is still served and still verifiable — but only if we look up
what the chain actually says.

So we ask the chain. db-sync's `voting_procedure` joins to `voting_anchor`, which stores the URL and
the blake2b-256 `data_hash` submitted with the vote. That hash is immutable and beyond BEACN's reach
to revise. Read-only query against the relay.

Writes: data/input/governance/onchain_vote_anchors.json
"""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CORE = REPO.parent / "beacn-drep-core"
OUT = REPO / "data" / "input" / "governance" / "onchain_vote_anchors.json"

# Identify BEACN's DRep from a transaction it actually submitted, rather than by matching a bech32
# string. db-sync renders the DRep id in the CIP-129 encoding, which is NOT the same string as the
# one in our config, and hand-converting between id encodings is precisely the class of mistake that
# has already corrupted votes in this system twice. A vote receipt's transaction_hash is a fact we
# hold; the chain will tell us whose vote it was.
def our_vote_txs() -> list[str]:
    txs = []
    for receipt in sorted((CORE / "data" / "output").glob("*/vote_receipt.json")):
        try:
            r = json.loads(receipt.read_text())
        except Exception:
            continue
        tx = r.get("transaction_hash")
        if r.get("submitted") and tx:
            txs.append(tx)
    return txs


def build_sql(tx_hashes: list[str]) -> str:
    quoted = ",".join(f"'{t}'" for t in tx_hashes)
    return f"""
select encode(ga_tx.hash,'hex') || '#' || gap.index,
       encode(t.hash,'hex'),
       v.vote::text,
       coalesce(va.url,''),
       coalesce(encode(va.data_hash,'hex'),'')
  from voting_procedure v
  join tx t                     on t.id  = v.tx_id
  join gov_action_proposal gap  on gap.id = v.gov_action_proposal_id
  join tx ga_tx                 on ga_tx.id = gap.tx_id
  left join voting_anchor va    on va.id = v.voting_anchor_id
 where v.drep_voter = (
        select v2.drep_voter from voting_procedure v2
          join tx t2 on t2.id = v2.tx_id
         where encode(t2.hash,'hex') in ({quoted})
           and v2.drep_voter is not null
         limit 1)
 order by t.id;
"""


def main() -> int:
    tx_hashes = our_vote_txs()
    if not tx_hashes:
        print("no submitted vote receipts found — cannot identify the DRep from its own votes")
        return 1
    print(f"identifying BEACN's DRep from {len(tx_hashes)} of its own vote transactions")
    SQL = build_sql(tx_hashes)
    remote = ("docker exec -i dbsync-mainnet-postgres "
              "psql -U postgres -d cexplorer -v ON_ERROR_STOP=1 -A -F '|' -t")
    p = subprocess.run(["ssh", "relay", remote], input=SQL, text=True,
                       capture_output=True, check=True)

    anchors: dict[str, dict] = {}
    for line in p.stdout.splitlines():
        parts = line.split("|")
        if len(parts) != 5:
            continue
        action_id, tx_hash, vote, url, data_hash = (x.strip() for x in parts)
        if not action_id or not tx_hash:
            continue
        # A DRep may vote more than once on an action (a revision). The LAST vote is the one that
        # counts on-chain, and it is the one whose anchor the public record must be checked against.
        anchors[action_id] = {
            "action_id": action_id,
            "transaction_hash": tx_hash,
            "vote": vote,
            "anchor_url": url or None,
            "anchor_hash": data_hash or None,
        }

    with_anchor = sum(1 for a in anchors.values() if a["anchor_hash"])
    OUT.write_text(json.dumps({
        "drep_identified_from": "BEACN's own submitted vote transactions, not a typed DRep id",
        "source": "db-sync voting_procedure + voting_anchor (relay, read-only)",
        "note": ("anchor_hash is the blake2b-256 the CHAIN records for each vote. It is the only "
                 "hash the public verifier may check the published rationale against; a hash we "
                 "recompute ourselves would make the check circular."),
        "votes": len(anchors),
        "votes_with_anchor": with_anchor,
        "anchors": anchors,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"on-chain votes: {len(anchors)}  with a rationale anchor: {with_anchor}")
    print(f"wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
