# DRep Vote History (On-chain, Relay-sourced)

This directory stores historical DRep voting records extracted from relay db-sync.

## Layout
- `latest/drep_vote_history.csv` — latest normalized snapshot for downstream analytics.
- `latest/manifest.json` — latest snapshot metadata.
- `<timestamp>/relay_drep_votes_raw.csv` — raw SQL export from relay.
- `<timestamp>/drep_vote_history.csv` — normalized rows with `action_id` mapping.
- `<timestamp>/manifest.json` — per-snapshot counts and paths.

## Normalized schema
- `snapshot_at_utc`
- `action_id`
- `action_tx_hash`
- `cert_index`
- `drep_id`
- `vote`
- `vote_tx_hash`
- `vote_time_utc`
- `vote_epoch`
- `vote_slot`

## Source
- Relay host: `relay`
- Postgres container: `dbsync-mainnet-postgres`
- DB: `cexplorer`
- Tables used: `voting_procedure`, `gov_action_proposal`, `drep_hash`, `tx`, `block`

## Refresh command
```bash
python3 scripts/export_drep_vote_history.py
```
