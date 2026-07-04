# Deep-research dossier: Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support

- action_id: `gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr`
- action_type: TreasuryWithdrawals
- requested: 1193000000000 lovelace
- drafted: 2026-07-04T16:11:31+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr is a TreasuryWithdrawals action titled "Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support" for 1193000000000 lovelace, proposed in epoch 638 and expiring after epoch 645. Source: action header; anchor: body.title; anchor: onChain.gov_action.rewards.
- The anchor authors list Intersect with ed25519 witness data and hashAlgorithm "blake2b-256". Source: anchor: authors; anchor: hashAlgorithm.
- The anchor says the request is "$298,250 (1,193,000 ADA)" to support Technical Steering Committee activities for 12 months. Source: anchor: body.motivation.
- The stated work packages are WP 1 community engagement and technical reports, WP 2 Parameter Committee/CIP editors/Hard Fork Working Group, and WP 3 a pilot independent technical review programme launching in 2027. Source: anchor: body.motivation.
- The anchor says technical workshops, the Security Council, and the Bug Bounty Programme are funded separately through the main Intersect budget and are not included in this request. Source: anchor: body.motivation.
- The anchor says all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury. Source: anchor: body.motivation.
- The anchor states execution of the work packages is contingent on approval of the IntersectMBO budget proposal. Source: anchor: body.motivation.
- The budget summary is WP 1 — 256,000 ADA; WP 2 — 832,000 ADA; WP 3 — 105,000 ADA; Total — 1,193,000 ADA. Source: anchor: Budget Summary.
- The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase. Source: anchor: Intersect Budget Process.
- The proposal states the requested amount does not, at time of submission, alone or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713. Source: anchor: Net Change Limit Compliance.
- The anchor names Appold as provider of independent audits and assurance, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment. Source: anchor: Audit & Oversight.
- The anchor states Intersect will continue milestone-based drawdowns, evidence-backed reporting, and transparent disclosures alongside external assurance. Source: anchor: Audit & Oversight.
- The anchor says the Technical Steering Committee has not received Cardano Treasury funding within the past 24 months, while Intersect and its committees have received funding through listed governance actions totaling 22,385,000 ADA. Source: anchor: Prior Treasury Funding Disclosure.
- The listed prior funding actions are 15,750,000 ADA for Intersect MBO, 750,000 ADA for Cardano Product Committee roadmap insights, and 5,885,000 ADA for OSC Budget Proposal. Source: anchor: Prior Treasury Funding Disclosure table.
- The 2026 Treasury Reserve Smart Contract stake address in the anchor is stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, matching the withdrawal reward address. Source: anchor: Intersect Budget Management Tooling; anchor: onChain.gov_action.rewards.
- The anchor states Intersect will use a single Treasury Reserve Smart Contract and one Project-Specific Smart Contract, with five Intersect admin roles, three Intersect leadership roles, and an Oversight Committee of six external independent third-party entities. Source: anchor: Specifics.
- The Oversight Committee entities named are Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl. Source: anchor: Specifics.
- The high-level smart contract permissions include multi-party authorization thresholds for TRSC Fund/PSSC Modify, TRSC Disburse, TRSC Pause and Resume, TRSC Sweep, and TRSC Reorganize. Source: anchor: Specifics.
- The anchor says the TRSC and PSSC cannot be staked with an SPO and are delegated to the auto-abstain predefined DRep. Source: anchor: Processes.
- The anchor says funding will be directed into the TRSC stake address upon enactment, then later transferred to the PSSC using the Fund action when the legal contract is prepared and the vendor is ready. Source: anchor: Processes.
- On-chain recipient history says stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v appears in 14 withdrawal proposals totaling 57273260000000 lovelace, first 2026-06-23 16:14:33 and last 2026-06-26 13:51:52. Source: onchain: recipient history.
- On-chain DRep vote counts so far are yes=35, no=11, abstain=5, explicit ballots and not stake-weighted. Source: onchain: DRep vote counts so far.
- Treasury flow over 36 epochs shows inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492. Source: onchain: treasury flow.
- BEACN doctrine prioritizes constitutional integrity/protocol safety, then treasury stewardship/downside protection, then evidence quality/reproducibility, then public-benefit ecosystem growth, then execution speed/social consensus momentum. Source: doctrine: values_hierarchy.md.
- BEACN doctrine rejects FCFS budget models and adopts a rolling-window Net Change Limit framework. Source: doctrine: treasury_spending_doctrine.md.
- BEACN doctrine says if ecosystem growth conflicts with treasury stewardship and evidence is weak, prefer ABSTAIN; if treasury upside is plausible but non-verifiable, apply a caution penalty and in practice NO or ABSTAIN on thin asks. Source: doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md.

## INFERENCES (analyst reasoning, labeled)
- The proposal has a clearer-than-minimal financial structure because it provides a 3-line work-package budget, a 12-month period, named oversight/audit arrangements, milestone-based drawdowns, and a return-of-unspent-funds statement; however, it does not provide line-item labor rates, unit costs, milestone amounts, or detailed deliverable acceptance criteria in the supplied anchor text.
- The main execution dependency visible in the record is that the work packages are contingent on approval of the IntersectMBO budget proposal; the supplied materials do not show whether that condition has already been satisfied.
- The recipient address concentration is relevant to treasury exposure because the same stake address appears in 14 withdrawal proposals totaling 57273260000000 lovelace, but the supplied on-chain context does not state whether those proposals are duplicates, related Intersect budget tranches, enacted, pending, or rejected.
- The proposal’s strongest documented mitigations are treasury smart-contract controls, named external oversight entities, Appold assurance, milestone-based drawdowns, evidence-backed reporting, and a stated refund path for unspent funds.
- The budget can be decomposed into partial-funding units using the proposal’s own work packages, but the supplied materials do not state that partial on-chain approval is procedurally available for this action as submitted.

## UNCERTAINTY (cannot be verified from the record)
- The supplied anchor does not include detailed line-item costs, labor assumptions, hourly rates, vendor identity beyond Intersect submitting on behalf of the vendor, or unit pricing for reports, event attendance, committee work, or technical reviews.
- The supplied record does not verify the underlying Hydra vote result, audit report contents, Appold engagement terms, smart-contract source code, or linked dashboard state; it only lists references and describes them.
- The supplied record does not establish whether the IntersectMBO budget proposal contingency has been met.
- The supplied record does not show milestone schedule, milestone payment amounts, acceptance criteria, reporting cadence, or specific deliverables for each work package beyond high-level descriptions.
- The supplied record does not show whether the requested ADA/USD conversion rate is fixed, when it was set, or how exchange-rate variance will be handled.
- The supplied on-chain recipient history does not identify how many of the 14 withdrawal proposals are enacted, pending, rejected, overlapping, or tied to the same budget program.
- The supplied treasury flow covers 36 epochs, while BEACN doctrine discusses a 73-epoch rolling window; the record does not provide the full 73-epoch withdrawal sum or current available NCL capacity under BEACN’s model.
- The supplied materials do not provide independent evidence that the Technical Steering Committee has not received treasury funding in the prior 24 months beyond the proposal’s own disclosure.
- The supplied materials do not quantify expected benefits, avoided losses, KPI baselines, or measurable impact targets attributable to this 1,193,000 ADA request.

## Proposal Summary
_grounded: yes_

This action requests withdrawal of 1,193,000 ADA, stated as $298,250, for 12 months of Intersect Technical Steering Committee support. The work is organized into three work packages: WP 1 community-facing technical coordination and technical reports, WP 2 protocol governance and evolution through the Parameter Committee, CIP editors, and Hard Fork Working Group, and WP 3 a pilot independent technical review programme launching in 2027. The proposal states that workshops, the Security Council, and the Bug Bounty Programme are outside this request and funded through the main Intersect budget. Execution is stated to be contingent on approval of the IntersectMBO budget proposal.

Evidence refs: anchor: body.title; anchor: body.motivation; anchor: Budget Summary

## Budget Analysis
_grounded: yes_

The anchor provides a work-package budget totaling 1,193,000 ADA: WP 1 is 256,000 ADA, WP 2 is 832,000 ADA, and WP 3 is 105,000 ADA. It states the request is $298,250 (1,193,000 ADA), spans 12 months, does not breach the applicable 350M NCL at submission, and that all unspent funds will be returned to the Cardano treasury. It also states milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and Appold assurance. The supplied text does not provide line-item cost buildup, milestone payment amounts, rates, named vendor contract terms, or quantified cost-benefit analysis.

Evidence refs: anchor: body.motivation; anchor: Budget Summary; anchor: Net Change Limit Compliance; anchor: Audit & Oversight

## Feasibility Assessment
_grounded: yes_

The proposal describes existing or named operational mechanisms: Intersect administration, a 2026 Treasury Reserve Smart Contract, one Project-Specific Smart Contract, named Oversight Committee entities, multi-party authorization thresholds, Appold assurance, a dashboard, and milestone-based drawdowns. The work scope includes ongoing committee support and a 2027 pilot technical review programme. Feasibility is only partially evidenced because the supplied record does not include staffing commitments, detailed schedule, milestone acceptance criteria, vendor contract, or verification that the IntersectMBO budget contingency has been satisfied.

Evidence refs: anchor: Specifics; anchor: Processes; anchor: Audit & Oversight; anchor: body.motivation

## Risk Analysis
_grounded: yes_

Documented downside controls include multi-party TRSC/PSSC authorization, six named external oversight entities, Appold assurance, milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and a stated refund path for unspent funds. Documented risk factors include the explicit contingency on IntersectMBO budget approval, limited budget granularity, absence of detailed milestone economics in the supplied anchor, and recipient-address concentration shown by 14 withdrawal proposals totaling 57273260000000 lovelace. BEACN doctrine treats treasury stewardship and evidence quality as high-priority considerations and applies caution where upside is plausible but non-verifiable.

Evidence refs: anchor: body.motivation; anchor: Audit & Oversight; anchor: Specifics; anchor: Processes; onchain: recipient history; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Alternatives Analysis
_grounded: yes_

Not funding is a doctrine-recognized treasury-protection path where evidence is weak or unverifiable, though the doctrine language frames deterministic outcomes elsewhere and this dossier does not recommend a vote. Partial funding can be analyzed using the proposal’s own work packages: WP 1 at 256,000 ADA, WP 2 at 832,000 ADA, and WP 3 at 105,000 ADA, but the record does not state that this submitted on-chain action can be partially approved. Other named providers or mechanisms in the record include Appold for assurance, Sundae Labs smart-contract tooling, the Oversight Committee entities, and separately funded Intersect mechanisms for workshops, the Security Council, and the Bug Bounty Programme. Deferral is relevant under doctrine where data freshness, anchor integrity, risk, or evidence gaps prevent directional confidence; the concrete deferral triggers visible here would be unresolved IntersectMBO budget contingency, missing milestone economics, and missing independent verification of linked audit/vote materials.

Evidence refs: anchor: Budget Summary; anchor: Audit & Oversight; anchor: Specifics; anchor: body.motivation; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Failure Mode Analysis
_grounded: yes_

Supplied-material failure modes include: the IntersectMBO budget proposal is not approved despite this action depending on it; high-level work packages prove too coarse to verify spend against deliverables; the 2027 pilot review programme is delayed or underspecified; external assurance identifies control weaknesses or unsupported milestone evidence; recipient-address aggregation increases treasury exposure if multiple related withdrawals are enacted close together; and the 36-epoch treasury flow ratio of 2.275492 signals recent enacted withdrawals exceeding inflow over that window. The anchor’s stated mitigations are multi-party smart-contract controls, external oversight, Appold assurance, milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and return of unspent funds.

Evidence refs: anchor: body.motivation; anchor: Audit & Oversight; anchor: Specifics; anchor: Processes; onchain: recipient history; onchain: treasury flow

## Community Impact
_grounded: yes_

The proposal claims community impact through technical experts attending major ecosystem events, technical reports on topics such as throughput improvements, finality protocols, governance improvements, quantum resistance, economic utility, and partner chains, and independent technical evaluations intended to support DRep decision-making. It links WP3 to informed DRep participation and cites a 2030 strategy goal of over 70 % DRep participation. The supplied record does not provide baseline participation data, expected number of reports, target audiences, event list beyond examples, or measurable outcomes attributable to this funding.

Evidence refs: anchor: body.motivation; anchor: Pillar 2: Adoption & Utility; anchor: Pillar 3: Governance; anchor: Pillar 4: Community & Ecosystem Growth

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
