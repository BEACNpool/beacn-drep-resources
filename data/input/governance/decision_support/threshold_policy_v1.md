# Threshold Policy v1 (Decision Readiness)

## Goal
Reduce avoidable abstentions without lowering governance standards.

## Directional output policy
- If `readiness_score >= 0.70` and no hard blockers: directional vote required (`YES` or `NO`).
- If `0.50 <= readiness_score < 0.70`: directional vote allowed only when risk profile is complete and financial clarity is sufficient for action type.
- If `readiness_score < 0.50`: default conservative outcome (`ABSTAIN` / `NEEDS_MORE_INFO`).

## Hard blockers (force non-directional)
- Missing canonical action identity or malformed action type.
- Missing anchor evidence with no verified fallback packet.
- Unresolved critical governance ambiguity (ratification threshold/conflicting rules unresolved).

## Treasury-specific guardrails
Directional vote should require:
- Budget envelope clarity.
- Milestone + acceptance criteria clarity.
- Disbursement controls (gates/escrow/clawback).
- Sustainability path clarity (including fee recovery assumptions where relevant).

## Diplomatic rationale standard
For any conservative recommendation, rationale must include:
- explicit missing evidence,
- concrete path to confidence,
- professional tone (critique proposal quality, not proposers).
