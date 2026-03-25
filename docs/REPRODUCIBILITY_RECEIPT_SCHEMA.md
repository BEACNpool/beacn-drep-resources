# Reproducibility Receipt Schema (Governance Analytics)

Use this schema for every analytics artifact derived from relay/midnight tables.

```json
{
  "artifact_id": "string",
  "generated_at_utc": "ISO-8601",
  "source": {
    "mode": "dbsync|koios|blockfrost|mixed",
    "network": "cardano-mainnet",
    "node": "relay|midnight|other",
    "tip": {
      "block_no": 0,
      "block_hash": "hex",
      "block_time": "ISO-8601"
    }
  },
  "query": {
    "sql_path": "repo-relative path",
    "params": {"window_days": 365}
  },
  "outputs": [
    {
      "path": "repo-relative path",
      "rows": 0,
      "sha256": "hex"
    }
  ],
  "onchain_refs": {
    "action_tx_hashes": ["hex"],
    "vote_tx_hashes": ["hex"],
    "anchor_hashes": ["hex"]
  },
  "notes": "plain-language caveats"
}
```

## Minimum publication rule
- Do **not** publish decision claims without a corresponding receipt.
- Do **not** publish off-chain claims as if they were on-chain receipts.
