# Deep-research dossier: Withdraw 3,810,423 ada for Mithril Protocol

- action_id: `gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y`
- action_type: TreasuryWithdrawals
- requested: 3810423000000 lovelace
- drafted: 2026-07-04T16:21:54+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action id gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8s24l0u4y is a TreasuryWithdrawals action titled "Withdraw 3,810,423 ada for Mithril Protocol". Evidence: action header; anchor: body.title.
- The requested treasury amount is 3810423000000 lovelace, shown in the action header and anchor onChain gov_action rewards value. Evidence: action header; anchor: onChain.gov_action.rewards.
- The anchor says the Treasury Withdrawal funds Mithril Protocol and was submitted by Intersect on behalf of the vendor, with Abstract, Motivation and Rationale sourced from the approved vendor proposal in the Intersect budget process. Evidence: anchor: abstract.
- The anchor identifies Intersect as author and includes an ed25519 witness with publicKey 05568f86955e65c1a59df5ac1985449b167c3828dccd00b3da9df36a1cf1c743. Evidence: anchor: authors.
- The anchor states Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain. Evidence: anchor: motivation.
- The anchor states the proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase. Evidence: anchor: Intersect Budget Process.
- The anchor states the requested amount does not, at time of submission, on its own or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713. Evidence: anchor: Net Change Limit Compliance.
- The budget summary lists Mithril Protocol Continuous Development at 3,699,440 ADA, Intersect Budget Administration fee at 110,983 ADA, and Total at 3,810,423 ADA. Evidence: anchor: Budget Summary.
- The anchor says audit and oversight costs are included within the overhead applied to this proposal, and the Intersect administration fee covers administrative oversight. Evidence: anchor: Audit & Oversight.
- The anchor says independent oversight will be provided through Intersect and technically capable third-party, including reporting obligations and milestone-based disbursement controls. Evidence: anchor: Audit & Oversight.
- The anchor states Teragone has not previously received direct funding from Cardano treasury or community governance programs. Evidence: anchor: Prior Treasury Funding Disclosure.
- The anchor states Teragone has been involved in Mithril for several years through close collaboration with Input Output Global (IOG), which has funded the project to date. Evidence: anchor: Prior Treasury Funding Disclosure.
- The anchor describes the proposal as a transition from IOG-funded development to a community-governed funding model via Intersect. Evidence: anchor: Prior Treasury Funding Disclosure.
- The anchor says Intersect will use the treasury management smart contract framework developed by Sundae Labs, with a new 2026 instance mirroring the 2025 budget-cycle contracts. Evidence: anchor: Intersect Budget Management Tooling.
- The anchor lists the 2026 Treasury Reserve Smart Contract stake address as stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v. Evidence: anchor: Intersect Budget Management Tooling.
- The on-chain recipient history says stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v appears in 14 withdrawal proposals totaling 57273260000000 lovelace, first 2026-06-23 16:14:33 and last 2026-06-26 13:51:52. Evidence: onchain: recipient history.
- The on-chain DRep vote counts so far are yes=49, no=4, abstain=3, as explicit ballots and not stake-weighted. Evidence: onchain: DRep vote counts so far.
- The 36-epoch treasury flow shows inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492. Evidence: onchain: treasury flow.
- BEACN doctrine ranks treasury stewardship and downside protection above evidence quality and public-benefit ecosystem growth, after constitutional integrity and protocol safety. Evidence: doctrine: values_hierarchy.md.
- BEACN doctrine rejects first-come-first-served budget models and adopts a rolling-window Net Change Limit framework. Evidence: doctrine: treasury_spending_doctrine.md.
- BEACN doctrine says incomplete diligence is recorded as explicit uncertainty and thin or unverifiable asks resolve in practice to NO or ABSTAIN under the soft gate. Evidence: doctrine: Dossier Gate Posture.
- BEACN doctrine says if work can be substantially accelerated by AI tooling, the budget should reflect post-AI costs, not legacy labor models. Evidence: doctrine: Foundational Axiom.

## INFERENCES (analyst reasoning, labeled)
- INFERENCE: The proposal has a clear high-level budget split, but the supplied anchor does not provide milestone amounts, detailed labor assumptions, deliverable acceptance criteria, or payment schedule for the 3,699,440 ADA continuous-development work package.
- INFERENCE: Because the same TRSC stake address appears in 14 withdrawal proposals totaling 57273260000000 lovelace, this action is part of a broader Intersect treasury-management flow rather than an isolated recipient history for Mithril alone.
- INFERENCE: The anchor provides governance-process validation through the Intersect Hydra Voting threshold, but the supplied record does not independently verify the referenced Hydra vote, audit reports, smart-contract repository, or dashboard contents.
- INFERENCE: The stated transition from IOG-funded development to community-governed funding indicates continuity of an existing project rather than a newly initiated protocol effort.
- INFERENCE: The 36-epoch treasury flow ratio 2.275492 indicates enacted withdrawals exceeded inflow over that window, which is relevant to BEACN treasury-stewardship doctrine.
- INFERENCE: The smart-contract role thresholds and named Oversight Committee reduce unilateral-control risk if implemented as described, but the supplied text alone does not prove deployment configuration or signer identities.
- INFERENCE: The proposal’s public-benefit case is strongest on infrastructure utility and decentralization goals, while cost-benefit verification is weak because the supplied record lacks measurable outputs tied to the requested amount.

## UNCERTAINTY (cannot be verified from the record)
- The supplied material does not include a detailed statement of work for Mithril Protocol Continuous Development beyond the single 3,699,440 ADA work package.
- The supplied material does not include milestone-by-milestone deliverables, acceptance criteria, dates, payment gates, or a full disbursement schedule.
- The supplied material does not provide vendor legal contract terms, refund terms, clawback mechanics, or remedies for non-delivery.
- The supplied material does not verify the external references, including Hydra Voting results, audit reports, smart-contract source repository, Smart Contract Guide, or dashboard contents.
- The supplied material does not identify whether the requested budget reflects post-AI cost assumptions required by BEACN doctrine.
- The supplied material does not provide a comparative quote, competing provider proposal, or alternative implementation plan for Mithril continuous development.
- The supplied material does not state whether partial funding was considered or how a partial award would change scope.
- The supplied material does not provide runway calculations for Mithril or explain how long the requested 3,810,423 ADA funds operations.
- The supplied material does not provide current treasury available capacity under BEACN’s rolling-window equation, only the provided 36-epoch flow and the anchor’s NCL assertion.
- The supplied material does not independently verify that Teragone has not received prior direct Cardano treasury or community-governance funding; it only records the proposal’s disclosure.

## Proposal Summary
_grounded: yes_

This TreasuryWithdrawals action requests 3810423000000 lovelace, described in the anchor as 3,810,423 ADA, to fund Mithril Protocol. The proposal is submitted by Intersect on behalf of the vendor. The anchor frames Mithril as infrastructure for rapid, trustless verification of Cardano state through stake-based threshold multi-signatures, reducing reliance on full-chain synchronization and centralized indexers or hosted APIs. The budget is split into 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for an Intersect Budget Administration fee. The anchor states the proposal passed the 2026 Intersect Budget Process Hydra Voting phase at the required 67% support threshold and does not breach the 350M Net Change Limit at submission.

Evidence refs: anchor: body.title; anchor: abstract; anchor: motivation; anchor: Strategic Pillar Alignment; anchor: Intersect Budget Process; anchor: Net Change Limit Compliance; anchor: Budget Summary; anchor: onChain.gov_action.rewards; action header: Treasury amount

## Budget Analysis
_grounded: yes_

The supplied budget is high-level: 3,699,440 ADA for Mithril Protocol Continuous Development, 110,983 ADA for Intersect Budget Administration fee, total 3,810,423 ADA. The anchor says audit and oversight costs are included within the overhead and that the administration fee covers administrative oversight. It also says reporting obligations and milestone-based disbursement controls will exist, but it does not provide milestone amounts, acceptance criteria, payment timing, labor rates, vendor margins, or a cost-benefit model. BEACN doctrine requires treasury stewardship and warns that work accelerated by AI should reflect post-AI costs; the supplied record does not show whether the requested amount was benchmarked against that standard. The 36-epoch treasury flow supplied for context shows inflow 158838297854652 lovelace and enacted withdrawals 361435336000000 lovelace, ratio 2.275492, which is relevant downside context for any additional withdrawal.

Evidence refs: anchor: Budget Summary; anchor: Audit & Oversight; doctrine: Values Hierarchy; doctrine: Foundational Axiom: AI Has Collapsed Marginal Costs; onchain: treasury flow

## Feasibility Assessment
_grounded: yes_

The anchor supports feasibility at the level of continuity and operational pathway. It states Teragone has worked on Mithril for several years through collaboration with IOG, which funded the project to date, and describes this request as a transition to a community-governed funding model via Intersect. It states funds will be directed into the Treasury Reserve Smart Contract stake address after enactment, then transferred to a Project-Specific Smart Contract when the legal contract is prepared and the vendor is ready. It also says all milestones will be outlined within the metadata. Feasibility remains only partially verifiable from the supplied record because the actual legal contract, milestone metadata, technical roadmap, delivery schedule, staffing plan, and external references are not included in the supplied text.

Evidence refs: anchor: Prior Treasury Funding Disclosure; anchor: Intersect Budget Management Tooling; anchor: Processes; anchor: references

## Risk Analysis
_grounded: yes_

The main treasury risk is the size and aggregation context of the withdrawal. The requested amount is 3810423000000 lovelace, and the same TRSC stake address appears in 14 withdrawal proposals totaling 57273260000000 lovelace. The supplied 36-epoch treasury flow shows enacted withdrawals exceeding inflow by a ratio of 2.275492. The anchor describes controls through TRSC/PSSC smart contracts, five Intersect admin roles, three Intersect leadership roles, and a six-entity Oversight Committee consisting of Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial and Eternl. It lists authorization thresholds for TRSC Fund/PSSC Modify, TRSC Disburse, TRSC Pause and Resume, TRSC Sweep, and TRSC Reorganize. Those controls address unilateral-control and administrative-error risks if implemented as described, but the supplied record does not independently verify contract code, deployment configuration, signer control, audit findings, or enforceable remedies. Evidence risk remains material because many verification items are references rather than included records.

Evidence refs: anchor: onChain.gov_action.rewards; anchor: Intersect Budget Management Tooling; anchor: Specifics; anchor: Processes; onchain: recipient history; onchain: treasury flow; doctrine: Treasury stewardship and downside protection; doctrine: Dossier Gate Posture

## Alternatives Analysis
_grounded: yes_

Not funding is an available treasury-preservation alternative under BEACN doctrine when evidence is thin or unverifiable, and the doctrine explicitly prioritizes treasury stewardship above ecosystem growth when evidence quality is weak. Partial funding is not specified in the anchor: the supplied record gives only the total 3,810,423 ADA request and two budget lines, with no reduced-scope option or partial-award mapping. Other named providers or mechanisms in the record are IOG, which funded Mithril to date; Intersect, which submits and administers the withdrawal; Teragone, described as the vendor with Mithril experience; and the Sundae Labs smart-contract framework used for treasury management. The supplied record does not include a competing provider proposal or alternate procurement mechanism. Deferral is supported by doctrine as a way to avoid forcing directional confidence when data freshness, anchor integrity, or evidence coverage is insufficient; in this record, deferral would target missing milestone metadata, payment gates, contract terms, cost benchmarks, and verification of referenced audits and voting records.

Evidence refs: anchor: Budget Summary; anchor: Prior Treasury Funding Disclosure; anchor: Intersect Budget Management Tooling; anchor: references; doctrine: Values Hierarchy; doctrine: Dossier Gate Posture; doctrine: Spending Model: Rolling Window NCL

## Failure Mode Analysis
_grounded: yes_

BEACN doctrine identifies treasury failure modes including land rush, quality inversion, perverse incentives, and budget cliff under first-come-first-served models. The on-chain recipient history shows the same TRSC stake address in 14 withdrawal proposals totaling 57273260000000 lovelace over 2026-06-23 16:14:33 to 2026-06-26 13:51:52, which is relevant to aggregation and queue-pressure analysis. For this action, execution failure modes include non-delivery of continuous-development work, delayed legal contracting before PSSC funding, inadequate milestone metadata, inability to verify external oversight, and mismatch between requested amount and independently verifiable deliverables. Control failure modes include incorrect TRSC/PSSC administration, signer coordination failure, or oversight entities verifying administrative actions without discretion over governance decisions. The supplied anchor names authorization thresholds and a dashboard for community audit, but it does not include the underlying metadata, contract state, audit content, or operational history needed to close these failure modes from the supplied record alone.

Evidence refs: doctrine: Why Not FCFS-Annual-Reset; doctrine: Rolling Window NCL; onchain: recipient history; anchor: Specifics; anchor: Processes; anchor: Audit & Oversight

## Community Impact
_grounded: yes_

The anchor claims public ecosystem impact through faster, trustless verification of Cardano state, lower onboarding friction, and reduced dependency on centralized indexers and hosted APIs. It says Mithril can support exchanges, wallets, monitoring, bridges, light wallets, full wallets, light clients, and community-built tools. It aligns the proposal fully with Infrastructure & Research Excellence and Adoption & Utility, and partially with Community & Ecosystem Growth. These are stated benefits, not independently measured outcomes in the supplied record; no adoption targets, current usage metrics, user counts, or ecosystem dependency analysis are included.

Evidence refs: anchor: motivation; anchor: Strategic Pillar Alignment

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
