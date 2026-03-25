# Governance Data Relevance Map (Relay db-sync)

Purpose: document which relay tables are most useful for DRep decision support, what each can prove, and how to cite them reproducibly.

## High-value tables

### `public.gov_action_proposal`
- **What it gives:** canonical governance action records (type, tx, status epochs, anchor linkage).
- **Use in decisions:** proposal lifecycle status, action classification, governance chronology.
- **Reference keys:** `(tx_hash, cert_index)` and derived `action_id`.

### `public.treasury_withdrawal`
- **What it gives:** treasury withdrawal recipients and amounts linked to governance actions.
- **Use in decisions:** repeated recipient detection, total requested by recipient, concentration risk.
- **Reference keys:** `gov_action_proposal_id`, `stake_address_id`, `amount`.

### `public.voting_procedure`
- **What it gives:** on-chain votes (DRep/SPO/CC) per governance action.
- **Use in decisions:** support/divergence context, voter concentration, temporal voting patterns.
- **Reference keys:** `gov_action_proposal_id`, `voter_role`, `vote`, `tx_id`.

### `public.drep_hash`
- **What it gives:** normalized DRep identifiers.
- **Use in decisions:** stable DRep-level historical comparison.
- **Reference keys:** `id`, `view`.

### `public.voting_anchor`
- **What it gives:** anchor URL/hash referenced by votes/actions.
- **Use in decisions:** source integrity and proposal evidence traceability.
- **Reference keys:** `url`, `data_hash`, `type`.

### `public.tx` + `public.block`
- **What they give:** immutable tx/block hashes and timestamps.
- **Use in decisions:** reproducible receipts and timing chronology.
- **Reference keys:** tx hash, block hash, epoch, slot, block time.

## Secondary/optional tables
- `public.delegation_vote` for DRep delegation dynamics (helpful for context, not direct vote quality).
- `public.off_chain_vote_*` for off-chain governance metadata quality checks.

## Evidence taxonomy (important)
- **On-chain evidence:** action/vote/treasury flows/timing (db-sync/Koios/Blockfrost reproducible).
- **Off-chain evidence:** team identity, delivery claims, milestone narratives.
- Never present off-chain claims as on-chain facts.

## Reproducibility requirements for every published analytic claim
1. Query text (SQL) committed in repo.
2. Query params (time window, filters) committed.
3. Snapshot context (tip block hash/number/time).
4. Output hash + row count.
5. On-chain references (tx hashes/action ids) included in artifact.
