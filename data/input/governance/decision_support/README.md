# Decision Support Inputs (Abstain Burn-down)

Purpose: provide structured, auditable context so the core engine can move from avoidable `ABSTAIN` to confident `YES`/`NO`.

Files:
- `vote_readiness_matrix.csv` — per-action gating checklist with pass/fail fields.
- `financial_sustainability_profiles.csv` — treasury/financial viability markers.
- `risk_mitigation_registry.csv` — risk domains + mitigation evidence markers.
- `threshold_policy_v1.md` — scoring and directional-threshold policy used by these sheets.

Design principles:
- Conservative by default, but decisive when minimum evidence is present.
- Diplomatically explainable to community readers.
- Reproducible and machine-checkable.

Recommended usage order:
1. Resolve anchor fetch defects.
2. Fill readiness/risk/financial rows for abstain actions first.
3. Re-run core and compare abstain deltas by reason code.
