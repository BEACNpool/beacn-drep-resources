# Missing Context & Resource Gaps (Training Phase)

_Last generated: 2026-03-25_

This is an **internal training artifact** (not external policy). Purpose: document what context is still missing when the bot abstains, and map each gap to concrete resource additions.

## Current latest simulation snapshot
- YES: 68
- NO: 9
- ABSTAIN: 18

## Abstain driver categories observed
1. **High risk flags triggered conservative abstain**
   - Meaning: current risk context is too thin to justify YES/NO.
   - Missing context: recipient/project risk context, implementation readiness details, contradiction resolution notes.

2. **No DRep distribution available**
   - Meaning: comparative signal unavailable or sparse for some actions.
   - Missing context: refreshed/complete vote-distribution and cohort snapshots.

3. **Unknown/new action-type rubric (e.g., HardForkInitiation variants)**
   - Meaning: no explicit scoring rubric exists for this exact type key.
   - Missing context: action-type normalization mapping + dedicated rubric inputs.

4. **Remote source not pinned for strict replay**
   - Meaning: source exists but is not yet snapshot-pinned locally.
   - Missing context: deterministic pinned capture in repo data paths.

## New resource additions (registry stage)
- `gov_anchor_documents` (anchor doc snapshots) — pipeline implemented (`scripts/fetch_anchor_documents.py`), currently partial fetch success.
- `gov_action_metadata_expanded` (enriched action metadata)
- `treasury_recipient_risk_profiles` (recipient risk context)
- `parameter_impact_notes` (parameter-change context)
- `hardfork_readiness_signals` (hardfork readiness context)

### Current anchor fetch status (latest run)
- actions_total: 94
- fetched_ok: 17
- failed: 77
- Note: many anchors require additional fetch adapters (headers/content negotiation or alternate source retrieval).

## How these map to abstain reduction
- High-risk abstains -> improve with `treasury_recipient_risk_profiles`, `hardfork_readiness_signals`, `parameter_impact_notes`
- Missing distribution -> improve with fresher `top_drep_votes_snapshot` + poll run coverage
- Unknown type abstains -> improve with `gov_action_metadata_expanded` + core action-type normalization
- Replay pinning abstains -> improve with `gov_anchor_documents` pinned snapshots

## Immediate implementation order
1. Build `gov_anchor_documents` snapshot pipeline (highest impact for evidence depth).
2. Build `gov_action_metadata_expanded` from existing governance exports.
3. Build `treasury_recipient_risk_profiles` for treasury withdrawals.
4. Extend core action-type normalizer for hardfork variants.
5. Re-run simulation and compare abstain reason counts.
