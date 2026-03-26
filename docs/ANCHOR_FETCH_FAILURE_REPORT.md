# Anchor Fetch Failure Report (latest)

Generated: 2026-03-26
Dataset: `data/input/governance/anchor_documents_index.csv`

## Summary
- Total actions: 94
- Anchor fetch success: 92 (97.87%)
- Failures: 2 (both `http_error:404`)

## Failed actions

1) `gov_action1fvgw27fjpr9c7g582mszzyez0jgkqgjgatzdnyngrg8wwc9kcn3qqxtz8r7`
- source_url: `https://raw.githubusercontent.com/theeldermillenial/2025-liquidity-budget/refs/heads/master/withdrawal-1/data.jsonld`
- error: `HTTP Error 404: Not Found`
- likely cause: upstream path moved/removed in repository
- remediation: pin immutable commit-hash URL or mirror snapshot in anchor cache service

2) `gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw`
- source_url: `https://raw.githubusercontent.com/IntersectMBO/governance-actions/refs/heads/main/mainnet/2024-10-21-ppu/metadata.jsonld`
- error: `HTTP Error 404: Not Found`
- likely cause: branch/path drift in source repository
- remediation: pin immutable commit-hash URL or route via governance mirror endpoint

## Recommended next controls
- Prefer immutable (commit-pinned) raw GitHub URLs for anchors where possible.
- Add mirror rewrites for known brittle GitHub `refs/heads/*` anchor patterns.
- Keep ABSTAIN policy active when anchor remains unfetchable/unpinned.
