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

---

## Abstain-focused context build plan (from latest simulation outputs)

Source snapshot used:
- `beacn-drep-core/data/output/public/vote_rationale_report.json`
- `beacn-drep-resources/data/input/governance/anchor_documents_index.csv`

### Current abstain inventory
- Total actions: 95
- Abstain actions: 18

Abstain reason split:
- `RISK_HIGH`: 8
- `CONTEXT_THIN_ANCHOR_UNPINNED`: 7
- `DREP_DISTRIBUTION_MISSING`: 1
- `RULE_THRESHOLD_UNMET`: 1
- `None` (legacy scaffold item): 1

### What it takes to convert abstains into vote-ready context

#### 1) `CONTEXT_THIN_ANCHOR_UNPINNED` (7 actions) — highest-volume blocker
Needed to move to confident YES/NO:
- Pin anchor docs for each action (deterministic local snapshot + hash already modeled).
- Add fetch adapters for `ipfs://` anchors and 404 fallback paths.
- Re-run rationale generation after pinning so evidence depth and context scoring refresh.

Actions in this bucket:
- `gov_action13qr78nhrhetywapvx2wpm63y9uxpc2dc45zsu9gkncasxqhuhltqqqfu32x`
- `gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpcdq823y`
- `gov_action19uhuy5uame2s60yrh6n8cyds8ps5q7tkh05dqlzmpcfy429p9w4qq5ll3g0`
- `gov_action1fvgw27fjpr9c7g582mszzyez0jgkqgjgatzdnyngrg8wwc9kcn3qqxtz8r7`
- `gov_action1n9hdlcmshrj3hee4g8n4fxdgrprpxp0r03l6psd3j0evtpck0nrsqm57age`
- `gov_action1q0m8z7glm9cprucwf44hdjdfra8khnakpm3hu5ueh929hvljw4aqqzuxfxz`
- `gov_action1vrkk4dpuss8l3z9g4uc2rmf8ks0f7j534zvz9v4k85dlc54wa3zsqq68rx0`

#### 2) `RISK_HIGH` (8 actions) — highest-confidence conservatism blocker
Needed to move to confident YES/NO:
- Build targeted risk context profiles (recipient, delivery history, governance/process risk, implementation readiness).
- For protocol-level actions, add technical impact notes (node/operator burden, rollback risk, upgrade criticality).
- For committee/constitutional actions, add trust + governance process evidence (track record, conflicts, mandate clarity).

Actions in this bucket:
- `gov_action10ueqgzwenxr39le68n0se9peu92r7gm2846xwehh3u0ahc0qd0uqqyljxu5`
- `gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw`
- `gov_action169kllwhfmp488je5x5rwvufd08p8sztdcf0ghf5sp6ey2gnjdwaqql47xry`
- `gov_action1aw809r9gpk7eemt02alszw7lceyf0505uvntavm62rakkckr3nxsqd54zm8`
- `gov_action1fpqwxp2kxvnntr8hpkh9q9djm78ccdww7qlhg5safugh4stmcwzqql5lauu`
- `gov_action1n5sn54mgf47a7men2ryq6ppx88kta4wvenz2qkl4f9v6ppje8easqxwm88m`
- `gov_action1pvv5wmjqhwa4u85vu9f4ydmzu2mgt8n7et967ph2urhx53r70xusqnmm525`
- `gov_action1zhuz5djmmmjg8f9s8pe6grfc98xg3szglums8cgm6qwancp4eytqqmpu0pr`

#### 3) `DREP_DISTRIBUTION_MISSING` (1 action)
Needed to move to confident YES/NO:
- Refresh/repair DRep distribution snapshot for this action.
- Confirm coverage in governance export so vote distribution signal is non-empty.

Action:
- `gov_action1k2jertppnnndejjcglszfqq4yzw8evzrd2nt66rr6rqlz54xp0zsq05ecsn`

#### 4) `RULE_THRESHOLD_UNMET` (1 action)
Needed to move to confident YES/NO:
- Add richer domain-specific context for treasury value/risk tradeoffs so score clears a directional threshold.
- Requires recipient risk profile + deliverable quality evidence, not just anchor presence.

Action:
- `gov_action1uhzd06a26qavzflvrx3gvcz6rzxkl6su2ns8t3seef5e8dl6nlgsqcgtufg`

#### 5) Legacy `None` abstain code (1 action)
Needed to move to confident YES/NO:
- Eliminate placeholder/scaffold rationale path for legacy item and run it through current scoring path.

Action:
- `ga_0001`

### Practical minimum work package (no architecture changes)
1. Fix anchor fetch coverage (`ipfs://` + fallback) and re-pin missing anchors.
2. Fill three context resources already planned here:
   - `treasury_recipient_risk_profiles`
   - `parameter_impact_notes`
   - `hardfork_readiness_signals`
3. Refresh DRep distribution snapshot coverage for missing action(s).
4. Re-run rationale simulation and compare abstain deltas by `abstain_reason_code`.

---

## 14-abstain burn-down checklist (current)

Target outcome: keep conservative standards, but reduce avoidable abstains by adding evidence quality, not by loosening doctrine.

### A) `RISK_HIGH` (8 actions)
Actions:
- `gov_action10ueqgzwenxr39le68n0se9peu92r7gm2846xwehh3u0ahc0qd0uqqyljxu5`
- `gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw`
- `gov_action169kllwhfmp488je5x5rwvufd08p8sztdcf0ghf5sp6ey2gnjdwaqql47xry`
- `gov_action1aw809r9gpk7eemt02alszw7lceyf0505uvntavm62rakkckr3nxsqd54zm8`
- `gov_action1fpqwxp2kxvnntr8hpkh9q9djm78ccdww7qlhg5safugh4stmcwzqql5lauu`
- `gov_action1n5sn54mgf47a7men2ryq6ppx88kta4wvenz2qkl4f9v6ppje8easqxwm88m`
- `gov_action1pvv5wmjqhwa4u85vu9f4ydmzu2mgt8n7et967ph2urhx53r70xusqnmm525`
- `gov_action1zhuz5djmmmjg8f9s8pe6grfc98xg3szglums8cgm6qwancp4eytqqmpu0pr`

What to add:
- Risk profile fields per action type (execution/governance/financial/technical).
- Mitigation signals (milestones, independent assurance, clawbacks, audit gates).
- Hardfork/parameter readiness notes from reproducible public sources.

### B) `RULE_THRESHOLD_UNMET` (4 actions)
Actions:
- `gov_action13qr78nhrhetywapvx2wpm63y9uxpc2dc45zsu9gkncasxqhuhltqqqfu32x`
- `gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpcdq823y`
- `gov_action1n9hdlcmshrj3hee4g8n4fxdgrprpxp0r03l6psd3j0evtpck0nrsqm57age`
- `gov_action1uhzd06a26qavzflvrx3gvcz6rzxkl6su2ns8t3seef5e8dl6nlgsqcgtufg`

What to add:
- Stronger budget proportionality evidence and delivery-accountability markers.
- Explicit sustainability/fee-recovery clarity markers for treasury actions.
- Action-type-specific threshold calibration checks (same guardrails, better fit).

### C) `CONTEXT_THIN_ANCHOR_UNPINNED` (1 action)
Action:
- `gov_action1fvgw27fjpr9c7g582mszzyez0jgkqgjgatzdnyngrg8wwc9kcn3qqxtz8r7`

What to add:
- Recover canonical anchor via fallback chain (ipfs gateways + mirrored sources).
- If unavailable, build a secondary evidence packet and mark confidence penalty explicitly.

### D) `DREP_DISTRIBUTION_MISSING` (1 action)
Action:
- `gov_action1k2jertppnnndejjcglszfqq4yzw8evzrd2nt66rr6rqlz54xp0zsq05ecsn`

What to add:
- Repair distribution snapshot coverage and add fallback behavior when this dataset is absent.

### E) Known fetch defects affecting abstains
Fix/retry these first:
- `gov_action1286ft23r7jem825s4l0y5rn8sgam0tz2ce04l7a38qmnhp3l9a6qqn850dw` (404)
- `gov_action169kllwhfmp488je5x5rwvufd08p8sztdcf0ghf5sp6ey2gnjdwaqql47xry` (timeout)
- `gov_action1n5sn54mgf47a7men2ryq6ppx88kta4wvenz2qkl4f9v6ppje8easqxwm88m` (timeout)

Success criteria for this checklist:
- abstain count drops only when evidence coverage improves,
- every remaining abstain has a specific, publishable reason code,
- rationale language remains diplomatic and constructive for community readers.
