# Deep-research dossier: Withdraw 1,162,746 ada for MLabs Core Tool Maintenance & Enhancement: Plutarc...

- action_id: `gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8svfsvefn`
- action_type: TreasuryWithdrawals
- requested: 1162746000000 lovelace
- drafted: 2026-07-04T16:14:19+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action id is gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8svfsvefn; action type is TreasuryWithdrawals; proposed epoch is 638; expires after epoch 645.
- The title is "Withdraw 1,162,746 ada for MLabs Core Tool Maintenance & Enhancement: Plutarc...".
- The on-chain treasury amount is 1162746000000 lovelace, equal to 1,162,746 ada.
- The anchor names Intersect as the author and states the Treasury Withdrawal is submitted by Intersect on behalf of the vendor.
- The anchor says the withdrawal funds "MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply."
- The proposal seeks annual funding for maintenance and enhancement of Plutarch and Ply.
- The anchor describes Plutarch as a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC.
- The anchor describes Ply as helping serialize Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- The anchor states MLabs counted at least 26 teams building with Plutarch and Ply in the motivation section.
- The anchor also states MLabs conservatively counted at least 15 teams building with Plutarch and Ply in the rationale section.
- The proposal priority order is: 1. Critical breakages and serious vulnerabilities; 2. Protocol-era and hard-fork compatibility; 3. Bug fixes, correctness improvements, and optimizations; 4. Documentation, examples, technical blog posts, and developer-experience improvements.
- The anchor states Plutarch scripts rank among the smallest in MLabs' public cross-language benchmark suite while requiring comparatively low on-chain compute and memory.
- The anchor states the funding period is expected to cover ongoing Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land during the funding period.
- The anchor says the proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- The anchor says the requested amount does not, at time of submission, on its own or in aggregate, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- Budget table: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience is 1,128,880 ADA; Intersect Budget Administration fee is 33,866 ADA; total is 1,162,746 ADA.
- Prior treasury funding disclosure lists MLabs Core Tool Maintenance & Enhancement: Plutarch; MLabs Research towards Tooling for Elliptical Curves - GrumpleStiltSkin; and MLabs Core Tool Maintenance & Enhancement: Cardano.nix.
- The anchor states Plutarch/Ply were previously funded through Project Catalyst: Fund9 project id 900157 USD 73,040; Fund13 project id 1300141 ADA 487,679; Fund13 project id 1300144 ADA 57,370.
- The anchor states MLabs also previously received ADA 70,000 from Intersect to update Plutarch for Conway-era features.
- The anchor identifies the 2026 Treasury Reserve Smart Contract stake address as stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v.
- The on-chain context says stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v appears in 14 withdrawal proposals totalling 57273260000000 lovelace, first 2026-06-23 16:14:33, last 2026-06-26 13:51:52.
- The anchor onChain reward entry sends value "1162746000000" to key "stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v".
- The anchor onChain deposit is "100000000000" lovelace and reward_account is "stake1uyvjdz9rxsfsmv44rtk75k2rqyqskrga96dgdfrqjvjjpwsefcjnp".
- On-chain DRep vote counts so far are yes=32, no=11, abstain=3, explicit ballots and not stake-weighted.
- Treasury flow over 36 epochs is inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492.
- The anchor says Intersect will use a single Treasury Reserve Smart Contract and one Project-Specific Smart Contract.
- The anchor says Intersect management consists of five admin roles and three Intersect leadership roles.
- The anchor says an Oversight Committee of six external independent third-party entities will provide checks and balances: Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, and Eternl.
- The anchor states all milestones will be outlined within the metadata after funding is transferred to the Project-Specific Smart Contract.
- The anchor says a dashboard is available at treasury.sundae.fi for community audit and tracking metrics related to the withdrawn ada, also immutably verifiable on chain.
- BEACN doctrine prioritizes constitutional integrity and protocol safety first, treasury stewardship and downside protection second, evidence quality and reproducibility third, public-benefit ecosystem growth fourth, and execution speed and social consensus momentum fifth.
- BEACN doctrine rejects first-come-first-served budget models and adopts a rolling-window Net Change Limit framework.
- BEACN doctrine says if ecosystem growth conflicts with treasury stewardship and evidence is weak, prefer ABSTAIN; if rapid action conflicts with protocol safety, prefer NO or ABSTAIN until risk is reduced.
- BEACN doctrine says for TreasuryWithdrawals without a complete dossier, the soft gate scores directionally with an explicit -0.10 caution penalty on top of the base treasury penalty and conservative reasoning lean.
- BEACN doctrine states AI has collapsed marginal costs for code, documentation, research, and creative output by 10-100x and that requested ada per deliverable should decrease when work can be substantially accelerated by AI tooling.

## INFERENCES (analyst reasoning, labeled)
- Inference: The proposal is for maintenance of existing open-source developer infrastructure, not creation of a new end-user application, because the anchor frames Plutarch and Ply as developer-facing smart contract tools used by project teams.
- Inference: The record supports ecosystem relevance, but with inconsistent adoption counts: the same anchor reports at least 26 teams in motivation and at least 15 teams in rationale.
- Inference: Budget granularity is low beyond two top-level lines; the anchor provides a single work-package total plus administration fee, but not labor rates, staff allocation, quarter-by-quarter costs, or deliverable-level pricing.
- Inference: Milestone-based disbursement controls are asserted, but the actual milestone schedule is not included in the supplied anchor text; this limits reproducibility of execution tracking from the supplied record alone.
- Inference: The shared TRSC recipient history shows this address is an Intersect treasury reserve aggregation address across multiple proposals, so the 14-proposal total is treasury exposure context for the reserve mechanism rather than vendor-specific funding history.
- Inference: Prior funding disclosure makes double-funding review relevant, but the supplied record does not show prior deliverables, completion evidence, remaining obligations, or overlap analysis with the current annual maintenance scope.
- Inference: The proposal names oversight entities and signing thresholds, which supports governance-control extraction; however, the dossier cannot verify their operational readiness, identities, or actual signing behavior from the supplied documents alone.
- Inference: Under BEACN doctrine, the 36-epoch treasury flow ratio of 2.275492 and the 57,273,260,000,000 lovelace recipient-address proposal total are material treasury-stewardship context even though the anchor asserts NCL compliance at submission.
- Inference: The AI-cost doctrine is relevant because the work package includes documentation, examples, technical blog posts, bug fixes, correctness improvements, and optimizations, but the supplied proposal does not disclose assumptions about AI-assisted cost reduction.

## UNCERTAINTY (cannot be verified from the record)
- The supplied material does not include the full approved vendor proposal beyond the anchor summary.
- The supplied material does not include the legal contract, vendor contract terms, payment schedule, acceptance criteria, clawback terms, refund path, or termination rights.
- The supplied material does not include actual milestone metadata, even though the anchor says milestones will be outlined within metadata.
- The supplied material does not include staff names, staffing levels, hourly rates, day rates, estimated hours, quarterly budget allocation, or cost basis for the 1,128,880 ADA work package.
- The supplied material does not verify the MLabs benchmark results, the public benchmark methodology, or current benchmark freshness; it only reports the anchor's claim and URL.
- The supplied material does not reconcile the anchor's two adoption counts of at least 26 teams and at least 15 teams.
- The supplied material does not provide evidence of prior Catalyst or Intersect-funded deliverables, completion status, outcomes, or remaining maintenance obligations.
- The supplied material does not show whether the proposed work overlaps with prior Plutarch/Ply funding or separately funded Cardano.nix, GrumpleStiltSkin, or Conway-era work.
- The supplied material does not provide independent technical review of Plutarch/Ply code health, vulnerability backlog, issue backlog, release cadence, or maintainer bus factor.
- The supplied material does not provide alternative provider quotes, competing maintenance bids, or a comparison with other smart-contract tooling maintenance mechanisms.
- The supplied material does not verify the smart contract audits referenced by URI; the references are listed but their contents are not supplied here.
- The supplied material does not provide stake-weighted voting support; only explicit ballot counts are supplied.
- The supplied material does not state whether future recurring funding will be needed after this annual period.

## Proposal Summary
_grounded: yes_

This TreasuryWithdrawals action requests 1,162,746 ada, or 1162746000000 lovelace, for MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply. Intersect submits the withdrawal on behalf of the vendor. The proposal frames Plutarch as a Haskell eDSL for efficient Cardano smart contracts compiled to UPLC and Ply as serialization tooling for Plutarch scripts and CIP-57 blueprint-style artifacts. The planned priority order is critical breakages and serious vulnerabilities; protocol-era and hard-fork compatibility; bug fixes, correctness improvements, and optimizations; then documentation, examples, technical blog posts, and developer-experience improvements. The budget table has two lines: 1,128,880 ADA for the work package and 33,866 ADA for the Intersect Budget Administration fee, totaling 1,162,746 ADA. Funds are directed to the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v.

Evidence refs: anchor: body.title; anchor: body.abstract; anchor: body.motivation; anchor: rationale Budget Summary; anchor: body.onChain.gov_action.rewards; onchain: action summary

## Budget Analysis
_grounded: yes_

The supplied budget is high-level rather than granular. It identifies 1,128,880 ADA for WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience and 33,866 ADA for the Intersect Budget Administration fee, for a total of 1,162,746 ADA. The anchor asserts that the request does not breach the applicable 350M Net Change Limit at submission. The on-chain treasury context shows recent 36-epoch enacted withdrawals of 361435336000000 lovelace against inflow of 158838297854652 lovelace, ratio 2.275492. The recipient stake address appears in 14 withdrawal proposals totaling 57273260000000 lovelace. The anchor discloses prior Plutarch/Ply Catalyst funding of USD 73,040, ADA 487,679, ADA 57,370, and ADA 70,000 from Intersect for Conway-era Plutarch work, but does not provide overlap analysis, completion evidence, or detailed cost basis for the current request.

Evidence refs: anchor: rationale Net Change Limit Compliance; anchor: rationale Prior Treasury Funding Disclosure; anchor: rationale Budget Summary; onchain: recipient history; onchain: treasury flow

## Feasibility Assessment
_grounded: yes_

The record supports feasibility at a general capability level: the tools already exist, the proposal describes current ecosystem use, and it names maintenance categories tied to Cardano ledger, Plutus, UPLC, and protocol-era evolution. The anchor says MLabs counted at least 26 teams in one section and at least 15 teams in another, and says Plutarch/Ply were previously funded through Catalyst and Intersect. The execution mechanism is described through Intersect's TRSC/PSSC framework, oversight committee, signing thresholds, and future milestone metadata. Feasibility is not fully reproducible from the supplied record because it does not include a work plan, named maintainers, schedule, staffing assumptions, acceptance tests, release targets, or actual milestone definitions.

Evidence refs: anchor: body.motivation; anchor: rationale Strategic Pillar Alignment; anchor: rationale Prior Treasury Funding Disclosure; anchor: rationale Intersect Budget Management Tooling; anchor: rationale Processes

## Risk Analysis
_grounded: yes_

The proposal identifies ecosystem risk if Plutarch and Ply fall behind ledger and Plutus/UPLC evolution: adopters may face more friction, migration risk, uncertainty, expensive stack migrations, bespoke workarounds, or avoidable rewrites. Treasury risks in the supplied record include limited budget granularity, missing milestone details, absence of clawback/refund terms, and inability to verify prior-funded deliverables from the supplied documents. Governance-control mitigations are present at the mechanism level: external oversight committee, multi-role sign-off thresholds for TRSC/PSSC actions, non-staking/non-SPO delegation details, and a public dashboard. BEACN doctrine adds treasury-stewardship caution where evidence is incomplete, rejects FCFS spending, and requires quality gates under rolling-window NCL reasoning.

Evidence refs: anchor: rationale Strategic Pillar Alignment; anchor: rationale Intersect Budget Management Tooling; anchor: rationale Specifics; anchor: rationale Processes; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Alternatives Analysis
_grounded: yes_

Not funding is a doctrine-recognized treasury-protection path when evidence is weak or treasury stewardship conflicts with ecosystem growth; the supplied record indicates the consequence claimed by the proposer would be higher maintenance friction, migration risk, workarounds, or rewrites for Plutarch/Ply users. Partial funding is not specified in the anchor, but the budget has a separable administration fee and one work package; the supplied record does not provide sub-work-package pricing that would allow a grounded partial-scope amount. Other named mechanisms in the record include prior Project Catalyst funding, prior Intersect funding, the Intersect Budget Process Hydra Voting route, and Intersect's TRSC/PSSC treasury management framework. Other named providers or oversight participants in the record include Sundae Labs, Cardano Foundation, Dquadrant, NMKR, Sundial, Eternl, and Sundae Labs' smart contract framework, but the supplied material does not name an alternative provider to maintain Plutarch/Ply. Deferral is supported as a doctrine-consistent option where data freshness, anchor integrity, evidence quality, or protocol safety concerns prevent directional confidence; the supplied record does not state the operational effect of deferral beyond the proposal's general claim that ongoing maintenance is needed.

Evidence refs: anchor: rationale Strategic Pillar Alignment; anchor: rationale Budget Summary; anchor: rationale Prior Treasury Funding Disclosure; anchor: rationale Intersect Budget Process; anchor: rationale Intersect Budget Management Tooling; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Failure Mode Analysis
_grounded: yes_

Documented or doctrine-relevant failure modes include: Plutarch/Ply falling behind Cardano ledger and Plutus/UPLC evolution; existing adopters facing friction, migration risk, bespoke workarounds, or rewrites; treasury capacity pressure under recent withdrawals; quality inversion or land-rush dynamics under FCFS models; and weak evidence causing treasury upside to be non-verifiable. Mechanism-level operational failures addressed by the anchor include unilateral control or administrative errors, mitigated through multi-party authorization thresholds and an external oversight committee. Failure modes not resolved in the supplied record include lack of detailed milestone acceptance criteria, unclear clawback/refund path, uncertain overlap with prior funding, and unverified technical backlog or security posture.

Evidence refs: anchor: rationale Strategic Pillar Alignment; anchor: rationale Specifics; doctrine: treasury_spending_doctrine.md; doctrine: values_hierarchy.md; onchain: treasury flow

## Community Impact
_grounded: yes_

The proposal claims public-benefit impact through maintenance of open-source smart contract tooling used by Cardano builders. It states Plutarch and Ply are developer-facing tools for writing, compiling, serializing, testing, and maintaining production on-chain applications, and says they indirectly support DeFi, RWAs, payments, games, and other applications that depend on reliable and efficient smart contracts. The impact evidence is directional, not independently verified in the supplied record: the anchor gives internal MLabs counts of at least 26 and at least 15 teams but does not list teams, usage metrics, downloads, repository activity, or user testimonials in the supplied text.

Evidence refs: anchor: body.motivation; anchor: rationale Strategic Pillar Alignment

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
