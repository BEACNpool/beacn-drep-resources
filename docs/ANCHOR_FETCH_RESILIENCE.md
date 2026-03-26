# Anchor Fetch Resilience

`fetch_anchor_documents.py` now uses layered retrieval to improve anchor coverage.

## Resilience layers
1. **IPFS gateway chain** (multiple gateways, configurable via `IPFS_GATEWAYS`).
2. **Content-negotiation profiles** (rotating `Accept` headers).
3. **Optional mirror adapters** via `ANCHOR_MIRRORS`.
4. **Cache index** (`anchor_cache_index.json`) to reuse known-good files.
5. **Retry on 429** honoring `Retry-After` when present.

## Environment variables
- `IPFS_GATEWAYS` (comma-separated)
  - Example: `https://ipfs.io/ipfs/,https://dweb.link/ipfs/,https://cloudflare-ipfs.com/ipfs/`
- `ANCHOR_MIRRORS` (comma-separated base URLs)
  - Example: `https://anchors.beacn.example/fetch?url=`

## Secondary-source integration
A mirror endpoint can proxy alternate providers (including Cardano Foundation governance APIs) and return canonical anchor content. Configure that endpoint in `ANCHOR_MIRRORS`.

## Output additions
`anchor_documents_index.csv` now includes:
- `source_url` (original URL from action snapshot)
- `request_profile` (which header profile succeeded)
- `fetch_status=ok_cached` when reused from local cache

`anchor_documents_manifest.json` includes runtime config + cache path for auditability.
