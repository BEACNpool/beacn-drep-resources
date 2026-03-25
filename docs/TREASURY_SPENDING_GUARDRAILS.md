# Treasury Spending Guardrails (BEACN)

## Policy intent
- NCL is treated as an upper bound approved by governance, not a target to fully consume.
- Maintain reserve headroom for uncertainty and emergencies.
- Evaluate sustainability against observed inbound treasury fee flow.

## Decision checks (required in treasury rationale)
1. **NCL context**
   - Proposal impact as a share of current NCL envelope.
2. **Inflow/outflow sustainability**
   - Compare projected outflow trajectory vs recent inbound fee flow.
3. **Reserve posture**
   - Show resulting reserve headroom after recommended outflows.
4. **Exceptional overspend justification**
   - If outflow materially exceeds inflow trend, require explicit public-interest case + mitigation plan.
5. **Fee-positive/fee-recovery notes**
   - Document whether proposal has credible fee-recovery or treasury-positive effects.

## Reproducibility requirements
Any treasury sustainability claim must include:
- source tip (block hash/height/time),
- query reference,
- output hash,
- on-chain references used in calculation.

## Notes
This policy is conservative by design and aligned to treasury stewardship. It does not ban strategic spending.
