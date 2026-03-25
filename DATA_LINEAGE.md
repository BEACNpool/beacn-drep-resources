# Data Lineage

This document defines the authoritative provenance chain from on-chain data to the CSV snapshots used by the BEACN DRep decision engine.

## Source-of-Truth Path

```
Cardano mainnet
  → Relay node (10.30.0.6)
  → db-sync → PostgreSQL (cexplorer database)
  → export_from_postgres.py
  → CSV snapshots in this repo (data/input/governance/)
  → governance_export_manifest.json (hashes + timestamps)
```

## Fallback Path

```
Cardano mainnet
  → Koios API (via Cloudflare worker at koios.beacn.workers.dev)
  → cardano-gov polling bot (every 4 hours)
  → proposals.db (SQLite)
  → export_proposals_to_resources.py
  → same CSV snapshots + manifest
```

## Freshness SLA

- **Target:** snapshots refreshed every 6 hours
- **Maximum staleness:** 21600 seconds (6 hours)
- **Enforcement:** the decision engine checks `governance_export_manifest.json` timestamp. If data is older than the threshold, the engine forces ABSTAIN on all actions with a stale-data explanation.
- **Failure behavior:** if export fails, no CSVs are updated. The manifest retains the old timestamp, and the engine detects staleness on next run.

## Provenance Verification

Every `governance_export_manifest.json` includes:

| Field | Purpose |
|-------|---------|
| `generated_at_utc` | When this snapshot was produced |
| `source` | `postgresql_dbsync` or `sqlite_cardano_gov` |
| `source_db_sha256` | Hash of the source database (SQLite only) |
| `tip.block_no` | Latest block in db-sync at export time (PostgreSQL only) |
| `tip.slot_no` | Latest slot in db-sync at export time (PostgreSQL only) |
| `totals` | Row counts per output file |
| `outputs[].sha256` | SHA-256 hash of each output CSV |

An external auditor can:
1. Check `generated_at_utc` against the engine's `freshness.snapshot_time` in rationale.json
2. Verify CSV hashes match `outputs[].sha256`
3. Compare `tip.block_no` against public block explorers to confirm recency
4. Re-run the exporter against the same database to reproduce identical CSVs

## Schema Stability

CSV schemas are defined in `CSV_SCHEMAS.md`. Schema changes require:
1. Update `CSV_SCHEMAS.md`
2. Update `RESOURCE_ADMISSION_POLICY.md` if new resource types are added
3. Update `registries/resource_registry.csv` with new resource entries
4. Commit with changelog entry

Column additions are backward-compatible. Column removals or renames are breaking changes and require a version bump in the resource registry.
