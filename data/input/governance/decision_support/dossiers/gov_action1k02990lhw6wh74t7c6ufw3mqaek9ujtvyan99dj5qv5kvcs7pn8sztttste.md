# Deep-research dossier: Withdraw 540,750 ada for by TxPipe Dolos: Maintaining Cardano's Lightweight D...

- action_id: `gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste`
- action_type: TreasuryWithdrawals
- requested: 540750000000 lovelace
- drafted: 2026-07-04T16:09:06+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action id is gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste; action type is TreasuryWithdrawals; proposed epoch is 638 and expires after epoch 645. Evidence: onchain: action header.
- The on-chain treasury withdrawal amount is 540750000000 lovelace, equal to 540,750 ada. Evidence: onchain: action header; anchor: onChain.gov_action.rewards.
- The anchor title is "Withdraw 540,750 ada for by TxPipe Dolos: Maintaining Cardano's Lightweight D...". Evidence: anchor: body.title.
- The anchor says the withdrawal funds "Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2." Evidence: anchor: body.abstract.
- The anchor says the Treasury Withdrawal was submitted by Intersect on behalf of the vendor and that the abstract, motivation, and rationale were sourced from the approved vendor proposal submitted as part of the Intersect budget process. Evidence: anchor: body.abstract.
- The anchor says the proposal requests 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time maintainer for Dolos over 12 months at an annual rate of $105,000 USD. Evidence: anchor: motivation.
- The anchor budget summary lists WP1 - Dolos Maintenance and Enhancement at 525,000 ADA, Intersect Budget Administration fee at 15,750 ADA, and total at 540,750 ADA. Evidence: anchor: rationale Budget Summary.
- The anchor says Dolos is a lightweight Cardano data node built in Rust, connects directly to the Cardano network, indexes ledger primitives, and exposes five query interfaces including Mini-Blockfrost HTTP, UTxO-RPC gRPC, Mini-Kupo, and an Ouroboros N2C unix socket compatible with Cardano-cli, Ogmios, and other tooling. Evidence: anchor: motivation.
- The anchor reports Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors. Evidence: anchor: motivation.
- The anchor says the maintainer work covers essential codebase maintenance, community support, and AI-friendly documentation and integration resources. Evidence: anchor: motivation.
- The anchor says Dolos aligns to Pillar 2 focus area A.3 Developer Experience, specifically open-source incentives for maintenance of core Cardano SDKs, frameworks, and infrastructure. Evidence: anchor: rationale Strategic Pillar Alignment.
- The anchor says the proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase. Evidence: anchor: rationale Intersect Budget Process.
- The anchor says the requested amount does not, at time of submission, on its own or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713, and does not exceed TREASURY-02a at submission. Evidence: anchor: rationale Net Change Limit Compliance.
- The on-chain context says the recipient stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v appears in 14 withdrawal proposals totalling 57273260000000 lovelace, first 2026-06-23 16:14:33 and last 2026-06-26 13:51:52. Evidence: onchain: recipient history.
- The on-chain context says DRep explicit vote counts so far are yes=46, no=5, abstain=2, not stake-weighted. Evidence: onchain: DRep vote counts so far.
- The on-chain context says 36-epoch treasury inflow is 158838297854652 lovelace, enacted withdrawals are 361435336000000 lovelace, with ratio 2.275492. Evidence: onchain: treasury flow.
- The anchor identifies the 2026 Treasury Reserve Smart Contract stake address as stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v. Evidence: anchor: rationale Intersect Budget Management Tooling.
- The anchor says Intersect will use a single Treasury Reserve Smart Contract and one Project-Specific Smart Contract; administration includes five Intersect admin roles and three Intersect leadership roles, with an Oversight Committee of six external independent third-party entities. Evidence: anchor: rationale Specifics.
- The anchor names the Oversight Committee as Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl. Evidence: anchor: rationale Specifics.
- The anchor lists high-level authorization rules for TRSC Fund and PSSC Modify, TRSC Disburse, TRSC Pause and Resume, TRSC Sweep, and TRSC Reorganize. Evidence: anchor: rationale Specifics.
- The anchor says upon enactment funding will be directed into the TRSC stake address, later withdrawn into a UTxO at the TRSC payment address, and when the legal contract is prepared and the vendor is ready, transferred using the Fund action to the PSSC. Evidence: anchor: rationale Processes.
- The anchor says all milestones will be outlined within the metadata. Evidence: anchor: rationale Processes.
- The anchor says a dashboard at treasury.sundae.fi is available for community audit and tracking metrics for the withdrawn ada and on-chain verification. Evidence: anchor: rationale Processes.
- The anchor says audit and oversight costs are included in overhead, the Intersect administration fee covers administrative oversight, and independent oversight will be provided through Intersect and technically capable third-party, including reporting obligations and milestone-based disbursement controls. Evidence: anchor: rationale Audit & Oversight.
- The anchor says TxPipe has received funding through 30 Project Catalyst proposals across Funds 9 through 14, with 26 successfully delivered and 4 under development and on schedule. Evidence: anchor: rationale Prior Treasury Funding Disclosure.
- The anchor says TxPipe received open-source maintenance funding through Intersect's 2025 budget cycle for Pallas, Dolos, and UTxO RPC, all being delivered on schedule. Evidence: anchor: rationale Prior Treasury Funding Disclosure.
- BEACN doctrine prioritizes treasury stewardship and downside protection above evidence quality, public-benefit ecosystem growth, and execution speed, while constitutional integrity and protocol safety are highest. Evidence: doctrine: values_hierarchy.md.
- BEACN doctrine says if ecosystem growth conflicts with treasury stewardship and evidence is weak, prefer ABSTAIN; if treasury upside is plausible but non-verifiable, judge directionally with a caution penalty under the soft gate. Evidence: doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md.
- BEACN doctrine rejects first-come-first-served budget models and adopts a rolling-window Net Change Limit framework. Evidence: doctrine: treasury_spending_doctrine.md.
- BEACN doctrine says when evaluating TreasuryWithdrawals, if work can be substantially accelerated by AI tooling, the budget should reflect post-AI costs, not legacy labor models. Evidence: doctrine: treasury_spending_doctrine.md.

## INFERENCES (analyst reasoning, labeled)
- The proposal is for ongoing maintenance rather than a one-time build, because the anchor describes Year 2 maintenance, a 12-month part-time maintainer, and continuation after the existing contract closes.
- The requested 540,750 ada consists of 525,000 ADA project cost plus 15,750 ADA Intersect administration fee; the 525,000 ADA aligns with the stated 420,000 ADA base plus 105,000 ADA contingency reserve.
- The supplied material provides some execution controls, including smart-contract roles, oversight committee participation, reporting obligations, and milestone-based disbursement controls, but does not provide the actual milestone schedule or payment amounts per milestone.
- The recipient-history concentration is materially larger than this individual action because the same TRSC stake address appears in 14 withdrawal proposals totalling 57273260000000 lovelace; however, the supplied material indicates this is a shared Intersect 2026 Treasury Reserve Smart Contract address, not necessarily a single-vendor wallet.
- The budget is only partially analyzable from the supplied material because it gives total ADA amounts and a USD annual rate but does not provide ADA/USD conversion assumptions, time allocation detail, contingency release conditions, or per-deliverable pricing.
- The proposal has public-benefit characteristics under the doctrine because the anchor frames Dolos as open-source developer infrastructure and an alternative to full-node chain-data access.
- Under BEACN doctrine, the AI-friendly documentation component raises a cost scrutiny issue because the doctrine says AI-accelerated work should reflect post-AI costs; the anchor does not break out the cost of that component.
- The treasury-flow context indicates recent enacted withdrawals exceeded 36-epoch inflow by a ratio of 2.275492, which is relevant to BEACN's treasury stewardship and downside-protection doctrine.

## UNCERTAINTY (cannot be verified from the record)
- The supplied material does not include the full vendor proposal from the Hydra voting link, only the anchor's extracted summary and references.
- The supplied material does not verify the reported GitHub statistics, release activity, contributor count, or current Dolos adoption beyond the anchor statement.
- The supplied material does not include the actual legal contract, milestone metadata, milestone acceptance criteria, payment schedule, or refund/clawback terms.
- The supplied material does not state how the 105,000 ADA contingency reserve can be used, released, or returned if unused.
- The supplied material does not provide ADA/USD conversion assumptions for the stated $105,000 USD annual rate or the 420,000 ADA base request.
- The supplied material does not state whether the maintainer is named, what part-time fraction is expected, or what hours or service levels are required.
- The supplied material does not include independent technical assessment of Dolos, dependency risk, security posture, operational uptime, or compatibility requirements.
- The supplied material does not include stake-weighted governance support, only explicit DRep ballot counts.
- The supplied material does not verify the referenced external documents, audit reports, dashboards, or smart-contract guide content; only their labels and URIs are present in the anchor.
- The supplied material does not identify alternative providers for Dolos maintenance other than TxPipe, nor alternative funding mechanisms beyond Intersect process, Project Catalyst history, smart-contract disbursement, not funding, partial funding, or deferral as governance choices.

## Proposal Summary
_grounded: yes_

This TreasuryWithdrawals action requests 540750000000 lovelace / 540,750 ada for Dolos by TxPipe, described as Year 2 maintenance of a lightweight Cardano data node. The anchor states the request funds a part-time maintainer over 12 months, with work covering maintenance, community support, and AI-friendly documentation/integration resources. Intersect submitted the withdrawal on behalf of the vendor after the proposal met the stated 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase.

Evidence refs: onchain: action header; anchor: body.abstract; anchor: motivation; anchor: rationale Intersect Budget Process; anchor: onChain.gov_action.rewards

## Budget Analysis
_grounded: yes_

The on-chain amount is 540750000000 lovelace. The anchor budget table breaks this into 525,000 ADA for WP1 - Dolos Maintenance and Enhancement and 15,750 ADA for the Intersect Budget Administration fee, total 540,750 ADA. The motivation separately states 420,000 ADA plus a 105,000 ADA contingency reserve for a 12-month part-time maintainer at an annual rate of $105,000 USD. The record does not provide ADA/USD conversion assumptions, part-time fraction, per-milestone allocations, contingency release rules, unused-contingency treatment, or deliverable-level pricing. Under BEACN doctrine, the AI-friendly documentation component is relevant to cost scrutiny because AI-accelerated work should reflect post-AI costs, but the anchor does not price that component separately.

Evidence refs: anchor: rationale Budget Summary; anchor: motivation; anchor: rationale Audit & Oversight; doctrine: treasury_spending_doctrine.md Foundational Axiom

## Feasibility Assessment
_grounded: yes_

The anchor presents feasibility support through prior project activity metrics, open-source status, continuing maintenance from a previous cycle, prior funding disclosure, and described maintenance scope. It states Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors; it also states TxPipe has 26 delivered Catalyst proposals and 4 on schedule, plus 2025 Intersect maintenance funding for Pallas, Dolos, and UTxO RPC being delivered on schedule. The supplied material does not independently verify those claims or provide the actual milestone plan, staffing details, or acceptance criteria.

Evidence refs: anchor: motivation; anchor: rationale Prior Treasury Funding Disclosure; anchor: rationale Processes

## Risk Analysis
_grounded: yes_

Execution risk evidence includes a 12-month maintenance scope, dependency on legal contract preparation and vendor readiness before transfer to the PSSC, and unspecified milestone metadata to be outlined later. Governance/treasury custody risk evidence includes use of a TRSC and PSSC, multi-party authorization thresholds, and an Oversight Committee named in the anchor. Treasury exposure context includes the same TRSC recipient appearing in 14 withdrawal proposals totalling 57273260000000 lovelace and 36-epoch enacted withdrawals of 361435336000000 lovelace versus inflow of 158838297854652 lovelace. The record does not include actual contract terms, clawback/refund mechanics, or independent verification of smart-contract security beyond referenced audit labels/URIs.

Evidence refs: anchor: rationale Intersect Budget Management Tooling; anchor: rationale Specifics; anchor: rationale Processes; anchor: rationale Audit & Oversight; onchain: recipient history; onchain: treasury flow

## Alternatives Analysis
_grounded: yes_

Not funding is an available treasury-protection alternative under BEACN doctrine where evidence is weak or downside protection dominates, but the supplied proposal does not discuss a no-funding path. Partial funding could mean funding less than the requested 540,750 ADA, excluding some or all of the 105,000 ADA contingency reserve, or funding only a shorter maintenance period; however, these partial-funding mechanisms are not proposed in the anchor and no reduced scope is documented. Other named mechanisms/providers in the supplied record include prior Project Catalyst funding, Intersect's 2025 and 2026 budget processes, the Intersect/Sundae Labs smart-contract treasury management framework, and the named Oversight Committee entities; no alternate Dolos maintainer provider is named. Deferral is possible under doctrine when risk or evidence gaps remain, but the anchor frames the grant as beginning after the existing contract closes to avoid interruption, so deferral may conflict with the stated continuity goal. These are analytical alternatives from the record and doctrine, not vote recommendations.

Evidence refs: anchor: motivation; anchor: rationale Prior Treasury Funding Disclosure; anchor: rationale Intersect Budget Process; anchor: rationale Intersect Budget Management Tooling; anchor: rationale Specifics; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Failure Mode Analysis
_grounded: yes_

Documented or inferable failure modes from the supplied material include: maintenance deliverables cannot be assessed because milestone metadata is not included in the supplied record; contingency reserve use may be hard to evaluate because release and return conditions are absent; treasury concentration may be opaque because the shared TRSC recipient aggregates many withdrawal proposals; legal contract preparation or vendor readiness could delay PSSC funding; and BEACN doctrine flags systemic risks from first-come-first-served or weak-evidence treasury spending. The anchor provides some mitigations through smart-contract controls, oversight committee checks, dashboard tracking, reporting obligations, and milestone-based disbursement controls, but the supplied material does not include rollback, clawback, or refund procedures.

Evidence refs: anchor: rationale Processes; anchor: rationale Specifics; anchor: rationale Audit & Oversight; onchain: recipient history; doctrine: treasury_spending_doctrine.md

## Community Impact
_grounded: yes_

The anchor describes Dolos as open-source developer infrastructure that provides resource-efficient access to Cardano chain data through multiple protocols without running a full node. It says maintenance supports usability, reliability, protocol compatibility, bug fixing, documentation, issue triage, external contribution review, ecosystem-feedback enhancements, public communication, and AI-driven development workflows. The record does not quantify current users, downstream dependencies, uptime, performance, or economic impact.

Evidence refs: anchor: motivation; anchor: rationale Strategic Pillar Alignment

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
