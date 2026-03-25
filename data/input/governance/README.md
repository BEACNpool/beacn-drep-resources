# Governance datasets

These files are exported from `skills/cardano-gov/data/proposals.db` and intended for reproducible querying of historical and current governance actions.

Files:
- `governance_actions_all.csv` — full proposal/action history snapshot
- `governance_actions_active.csv` — active subset for current decision queue
- `governance_treasury_recipients.csv` — exploded treasury recipients by action
- `governance_action_flags.csv` — exploded proposal flags by action
- `governance_poll_runs.csv` — poll history from ingestion process
- `governance_export_manifest.json` — source DB hash + output file hashes + row counts
