# Deep-research dossier: Se7en Labs: Daedalus Wallet Maintenance and Improvements 2026-2027

- action_id: `gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j`
- action_type: TreasuryWithdrawals
- requested: 1785333000000 lovelace
- drafted: 2026-07-04T16:05:10+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action id is gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j; action type is TreasuryWithdrawals; proposed epoch is 639 and expires after 646.
- Anchor title is "Se7en Labs: Daedalus Wallet Maintenance and Improvements 2026-2027".
- The on-chain reward entry requests 1785333000000 lovelace to stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v; the budget table total is 1,785,333 ADA.
- The proposal describes Daedalus as Cardano's only full-node desktop wallet, running an embedded Cardano node and deriving wallet and governance data directly from chain without third-party APIs or trusted backends.
- The proposal states opt-in telemetry shows approximately 4,000 monthly active users and says the true count is meaningfully higher because privacy-conscious full-node users are less likely to opt in.
- The proposed work covers three areas in the abstract: Protocol Maintenance; Ecosystem Expansion; and User Support.
- The proposal states Protocol Maintenance includes node upgrades and hard fork readiness for Leios, Peras, and Nested Transactions, with a compatible release at least 2 weeks before every mainnet hard fork.
- The proposal states Ecosystem Expansion includes Keystone and Flex hardware wallet support, CIP-30 dApp connector, and Japanese localisation.
- The proposal states User Support includes responsive support for Daedalus users, dedicated attention to the Japanese community, and keeping Daedalus fully translated for Japanese users.
- The proposal states Daedalus is free and open-source under Apache License 2.0 and that Se7en Labs does not monetize Daedalus usage or capture customer relationships, subscription revenue, token value, or IP exclusivity from this work.
- The proposal states funded outputs include source code, build tooling, documentation, and release artifacts as public assets under Apache 2.0.
- The proposal says the team assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril Snapshot Bootstrap, UTxO-HD / LSM Backend, Apple Silicon builds, the drt Release CLI, and Nix Build Modernization since then.
- The proposal lists in-progress work as DRep Selection Dashboard, Ouroboros Genesis support, hardware wallet support for newer devices, Electron upgrade, and partial Mithril sync.
- The proposal states Se7en Labs has operated under a direct IOG contract for Daedalus maintenance since January 2026, closing August 31, 2026.
- The proposal states Se7en Labs has not received ada from the Cardano Treasury within the last 24 months.
- The proposal scope includes node and wallet backend currency, security and dependency maintenance, hard fork integration, Leios/Peras/Nested Transactions readiness, binary signing continuity, platform and localisation, hardware wallet support, CIP-30 dApp connector, user-facing CIP implementations, user support, and architecture assessment.
- The Risk Register lists ADA/USD exchange rate volatility as High likelihood and High impact, mitigated by prompt conversion to USD-backed stablecoins and USD-denominated labor costs invoiced at spot rate.
- The Risk Register lists cardano-node upstream API changes as Medium likelihood and High impact, mitigated by time-and-materials engagement and established working relationship with upstream IOG engineers.
- The Risk Register lists Leios/Peras complexity underestimate as Medium likelihood and Medium impact, mitigated by time-and-materials removing fixed-price risk.
- The Risk Register lists platform dependency changes as Low likelihood and High impact, mitigated by maintaining IOG binary signing and using the drt toolchain.
- The Risk Register lists team continuity over 12-month contract as Low likelihood and High impact, mitigated by founding-member continuity and documented processes in drt and Nix build infrastructure.
- Success metrics include compatible releases at least 2 weeks before each mainnet hard fork, cardano-node no more than 2 major versions behind mainnet recommended, 100% signed official releases, all four platform builds passing CI in every stable release, timely critical security fixes, Keystone and Flex support, CIP-30 stable release, maintained support including Japanese responses, full Japanese translation, and architecture assessment by Q3 2027.
- Milestones include Hard Fork Integration duration 6 weeks, Ongoing Maintenance duration 52 weeks, Leios/Peras Readiness duration 26 weeks, Hardware Wallet Support duration 12 weeks, CIP-30 dApp Connector duration 20 weeks, User Support duration 52 weeks, and Architecture Assessment duration 8 weeks.
- Budget summary line items are: Team 1,666,667 ADA; Test Hardware 33,333 ADA; Financial Audit 33,333 ADA; Intersect Budget Administration fee 52,000 ADA; Total 1,785,333 ADA.
- The budget text states any unspent labor, hardware, and audit budget is returned to the treasury.
- The proposal says audit and oversight costs are included within overhead, the Intersect administration fee covers administrative oversight, and independent oversight will be provided through Intersect and technically capable third-party, including reporting obligations and milestone-based disbursement controls.
- The proposal says Intersect serves as administrator and independent milestone verifier, monitors use of funds, confirms acceptance criteria, and authorizes disbursements.
- The proposal says funds are disbursed monthly against verified work and held by Intersect in a dedicated account auditable by the Cardano Community before monthly disbursement to Se7en Labs.
- The proposal says Intersect will use the treasury management smart contract framework developed by Sundae Labs, with a 2026 Treasury Reserve Smart Contract and one Project-Specific Smart Contract.
- The proposal names the Oversight Committee as Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl.
- On-chain recipient history says stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v appears in 14 withdrawal proposals totalling 57273260000000 lovelace, first 2026-06-23 16:14:33 and last 2026-06-26 13:51:52.
- On-chain DRep vote counts so far are yes=40, no=6, abstain=1, explicit ballots and not stake-weighted.
- Treasury flow over 36 epochs is inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492.
- BEACN doctrine prioritizes treasury stewardship and downside protection above evidence quality and reproducibility, public-benefit ecosystem growth, and execution speed/social consensus momentum, while constitutional integrity and protocol safety rank first.
- BEACN doctrine rejects first-come-first-served budget models and adopts a rolling-window Net Change Limit framework.
- BEACN doctrine states that for TreasuryWithdrawals without complete dossier, the current soft gate scores directionally with an explicit -0.10 caution penalty; incomplete diligence is recorded as explicit uncertainty.
- BEACN doctrine's AI cost axiom says requested ADA per deliverable should decrease where work can be substantially accelerated by AI tooling, and budgets should reflect post-AI costs rather than legacy labor models.

## INFERENCES (analyst reasoning, labeled)
- The requested withdrawal is for maintenance of an existing public infrastructure asset rather than a new proprietary product, based on the proposal's open-source/public-assets framing and listed maintenance scope.
- The budget has line-item totals and monthly disbursement language, but it does not provide hourly rates, named staffing allocation, FTE count, or per-milestone budget allocation; this limits cost reasonableness testing from supplied records.
- Because the recipient stake address is the Intersect/Sundae reserve address identified in the anchor and also appears in 14 withdrawal proposals totalling 57273260000000 lovelace, the on-chain recipient history likely reflects the shared treasury administration contract rather than Se7en Labs-specific recipient history; this is an inference from matching addresses and the anchor's process description.
- The proposal contains several verifiable future success metrics tied to public GitHub repositories and chain state, but supplied documents do not include independent evidence verifying prior shipped deliverables, MAU telemetry, or cost benchmarks.
- The time-and-materials structure plus monthly disbursement and return-of-unspent-funds language reduces fixed-price overrun risk in the proposal's own design, but leaves total labor cost discipline dependent on Intersect verification and contract controls not included in full in the supplied text.
- The treasury-flow context indicates recent enacted withdrawals exceed recent inflow over the supplied 36-epoch window, which is relevant under BEACN's treasury stewardship doctrine, but the supplied record does not provide the full 73-epoch rolling NCL computation.

## UNCERTAINTY (cannot be verified from the record)
- No independent repository commits, release artifacts, telemetry reports, support-channel records, or IOG contract documents are supplied to verify the proposal's claims about prior shipped Daedalus work, approximately 4,000 monthly active users, or current in-progress work.
- The supplied material does not include the full legal contract, monthly invoice format, milestone metadata, disbursement schedule by amount, clawback enforcement mechanics beyond return-of-unspent-budget statements, or exact conditions for refunding spent but disputed funds.
- The supplied material does not provide hourly rates, FTE count, role allocation, salary assumptions, vendor quotes for hardware, audit quote, or cost comparison to alternate maintainers.
- The supplied material does not verify the external references' contents, audits, GitHub repositories, or smart contract guide; only their labels and URIs are present in the anchor.
- The supplied material does not show whether other providers bid for Daedalus maintenance, whether IOG could continue funding, whether Intersect or another entity could run a competitive procurement, or whether a smaller maintenance-only scope was priced.
- The supplied material does not provide stake-weighted voting status, only explicit ballot counts.
- The supplied material does not show whether the 350M Net Change Limit claim is correct beyond the proposal's own assertion and the supplied 36-epoch treasury-flow summary.
- The supplied material does not show exact proposed contract start date or whether the treasury-funded contract begins before or after the IOG contract closes on August 31, 2026.
- The supplied material does not specify whether AI tooling affects the requested labor budget or how post-AI cost expectations were considered.

## Proposal Summary
_grounded: yes_

This TreasuryWithdrawals action requests 1785333000000 lovelace, shown in the budget as 1,785,333 ADA, for Se7en Labs to maintain and improve Daedalus Wallet during 2026-2027. The scope covers ongoing protocol and dependency maintenance, hard fork readiness, Leios/Peras/Nested Transactions readiness, binary signing continuity, Windows/macOS/Linux platform support, Japanese localisation and support, Keystone and Flex hardware wallet support, CIP-30 dApp connector implementation, user-facing CIP implementations, user support, and an architecture assessment. The proposal frames Daedalus as Cardano's only full-node desktop wallet and as Apache 2.0 open-source public infrastructure. It states Intersect will administer funds, verify milestones, and disburse monthly against verified work through Sundae Labs treasury-management smart contracts.

Evidence refs: anchor: body.title; anchor: body.onChain.gov_action.rewards; anchor: abstract; anchor: Nature of This Proposal; anchor: Scope of Work; anchor: Milestones; anchor: Budget Summary; anchor: Administration and Oversight; anchor: Intersect Budget Management Tooling

## Budget Analysis
_grounded: yes_

The budget table totals 1,785,333 ADA: 1,666,667 ADA for Maintenance and Improvements, 33,333 ADA for Test Hardware, 33,333 ADA for Financial Audit, and 52,000 ADA for the Intersect Budget Administration fee. The text states CI infrastructure and binary signing costs are covered under the approved Cardano Node Maintenance budget, and that any unspent labor, hardware, and audit budget is returned to the treasury. Funds are described as held by Intersect in a dedicated auditable account and disbursed monthly against verified work. The record does not provide hourly rates, FTEs, staffing mix, per-milestone budget allocation, hardware quotes, audit quote, or independent cost benchmark. Under BEACN doctrine, the request should be viewed through treasury stewardship and the post-AI cost axiom, but the supplied proposal does not show how AI-driven cost compression was considered.

Evidence refs: anchor: Budget Summary; anchor: Administration and Oversight; anchor: Audit & Oversight; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md Foundational Axiom: AI Has Collapsed Marginal Costs

## Feasibility Assessment
_grounded: yes_

The proposal identifies a team track record, prior Daedalus responsibility under an IOG contract beginning January 2026, and claimed shipped work including Mithril Snapshot Bootstrap, UTxO-HD / LSM Backend, Apple Silicon builds, drt Release CLI, and Nix Build Modernization. It also states the team has capabilities across Haskell/cardano-node integration, Electron/React frontend, Nix build systems, release engineering, and QA. Milestones have durations and acceptance criteria, including releases at least 2 weeks before mainnet hard forks and specific deliverables for hardware wallet support, CIP-30, user support, and architecture assessment. Feasibility is not independently verifiable from the supplied record because no repository evidence, release artifacts, staffing plan, or external validation is included.

Evidence refs: anchor: Track Record; anchor: Proven Capabilities; anchor: Scope of Work; anchor: Success Metrics; anchor: Milestones; uncertainty: independent verification missing

## Risk Analysis
_grounded: yes_

The proposal includes a risk register with five identified risks and mitigations: ADA/USD exchange rate volatility, cardano-node upstream API changes, Leios/Peras complexity underestimate, platform dependency changes, and team continuity over the 12-month contract. Treasury exposure is material because the action requests 1,785,333 ADA and the supplied 36-epoch treasury-flow context shows enacted withdrawals of 361435336000000 lovelace versus inflow of 158838297854652 lovelace, a ratio of 2.275492. The recipient stake address appears in 14 withdrawal proposals totaling 57273260000000 lovelace; based on the anchor, that appears to be a shared treasury reserve contract address rather than a Se7en Labs direct recipient, but the concentration is still operationally relevant to administration risk. BEACN doctrine emphasizes treasury stewardship and downside protection, and rejects first-come-first-served spending in favor of rolling-window NCL discipline.

Evidence refs: anchor: Risk Register; anchor: body.onChain.gov_action.rewards; anchor: Budget Summary; anchor: Intersect Budget Management Tooling; onchain: recipient history; onchain: treasury flow (36 epochs); doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md Spending Model: Rolling Window NCL

## Alternatives Analysis
_grounded: yes_

Not funding would preserve treasury funds but, according to the proposal, could leave Daedalus users exposed if Daedalus falls behind on protocol compatibility, because incompatible Daedalus versions cannot sync the chain. Partial funding could target maintenance-only work, hard fork readiness, security/dependency maintenance, or user support before lower-priority expansion work such as CIP-30, hardware wallet additions, or architecture assessment; however, the proposal argues the minimum maintenance team is not significantly smaller or cheaper than the team needed to also ship lightweight feature work, and it does not provide separate pricing by milestone. Named other providers or mechanisms in the record include the existing IOG contract through August 31, 2026, Intersect administration, Sundae Labs treasury-management smart contracts, and the Oversight Committee entities; the record does not state that any of these are alternative delivery vendors for Daedalus maintenance. Deferral could allow independent verification of prior deliverables, telemetry, costs, and NCL status, but could compress the timeline before the IOG contract closes on August 31, 2026 and before future protocol transitions named in the proposal.

Evidence refs: anchor: Expected Value; anchor: Budget Summary; anchor: Prior Treasury Funding Disclosure; anchor: Administration and Oversight; anchor: Intersect Budget Management Tooling; anchor: Specifics; doctrine: treasury_spending_doctrine.md Dossier Gate Posture; uncertainty: alternative providers and cost comparison missing

## Failure Mode Analysis
_grounded: yes_

Identified failure modes from the supplied record include ADA price volatility increasing effective budget risk, upstream cardano-node API changes increasing scope, Leios/Peras complexity exceeding expectations, platform signing or notarization changes disrupting releases, and team continuity issues during the contract year. Additional inferred failure modes are: milestone verification may be too coarse if monthly disbursement criteria are not specific; cost control may be weak without hourly/FTE detail; public-benefit claims may be overstated if MAU telemetry is not independently verified; and shared treasury smart-contract administration could become an operational bottleneck because the same reserve stake address appears across multiple withdrawal proposals. The supplied proposal includes mitigations for the named risks, but not for all inferred diligence gaps.

Evidence refs: anchor: Risk Register; anchor: Administration and Oversight; anchor: Success Metrics; onchain: recipient history; uncertainty: missing contract and cost details

## Community Impact
_grounded: yes_

The proposal claims community impact through maintenance of a free Apache 2.0 full-node desktop wallet, preservation of self-sovereign full-node access, support for Japanese localisation and Japanese-language users, hardware wallet support for security-conscious ADA holders, and CIP-30 access to dApps without switching to a browser wallet. It also claims Daedalus has approximately 4,000 monthly active users from opt-in telemetry. These impacts are substantively described in the anchor, but the supplied record does not independently verify telemetry, Japanese support demand, or expected increase in transactions or dApp use.

Evidence refs: anchor: abstract; anchor: Nature of This Proposal; anchor: Expected Value; anchor: motivation; anchor: KPI Alignment; anchor: Success Metrics; uncertainty: telemetry and impact verification missing

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
