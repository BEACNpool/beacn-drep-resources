# Security

## Baseline
- Never commit secrets or credentials.
- Keep `.env` and token files out of git.
- Treat data publication credentials as high-impact assets.

## Threat model (resources repo)
- If an attacker controls source endpoints or mirror services, they can attempt data poisoning.
- If a publishing token is compromised, they can push fake indexes/manifests.

## Controls
- Pin and hash fetched anchor content.
- Keep fetch provenance (`source_url`, `anchor_url`, profile used, fetch status).
- Prefer deterministic export scripts and signed release commits/tags.
- Restrict write/publish credentials with least privilege.

## Incident response
1. Revoke compromised credentials.
2. Freeze publication jobs.
3. Re-fetch from trusted mirrors/gateways and compare hashes.
4. Publish correction with scope and receipts.
