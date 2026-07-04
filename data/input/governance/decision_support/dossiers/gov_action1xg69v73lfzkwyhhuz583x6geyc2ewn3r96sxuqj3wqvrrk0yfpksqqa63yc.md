# Deep-research dossier: Scalus 2026: Maintenance, Dijkstra Readiness, Interoperability & Application Runtime

- action_id: `gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc`
- action_type: TreasuryWithdrawals
- requested: 2464844000000 lovelace
- drafted: 2026-07-04T15:57:49+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Governance action id is gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc.
- Action type is TreasuryWithdrawals.
- Title is "Scalus 2026: Maintenance, Dijkstra Readiness, Interoperability & Application Runtime".
- Treasury amount is 2464844000000 lovelace, corresponding to ₳2,464,844 in the anchor budget.
- Proposed epoch is 640 and the action expires after epoch 647.
- On-chain explicit DRep ballot counts so far are yes=8, no=4, abstain=2, not stake-weighted.
- On-chain treasury flow over 36 epochs is inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492.
- The proposal asks for ₳2,464,844, described as approximately $394,375 at $0.16/ADA, over 9 months, with no contingency.
- The proposal states the previous version was reduced from ₳8.5M / 12 months to approximately ₳2,464,844 / 9 months, with L1 node and third-party dependencies removed.
- The proposal funds maintenance, Dijkstra hard-fork readiness, interoperability, and a scoped application runtime.
- The proposal excludes a standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion.
- The proposal states delivery has three quarterly milestones over July 2026 - March 2027: M1 Q3 2026, M2 Q4 2026, and M3 Q1 2027.
- Budget distribution is Development & Engineering $315,000 / ₳1,968,750 / 79.9%; Product Management & Delivery $39,375 / ₳246,094 / 10.0%; Documentation & Developer Enablement $25,000 / ₳156,250 / 6.3%; Audits & Assurance $15,000 / ₳93,750 / 3.8%; total $394,375 / ₳2,464,844 / 100%.
- Development & Engineering breakdown is Maintenance 0.5 FTE / $78,750 / ₳492,188; Smart-contract platform & Dijkstra readiness 0.75 FTE / $118,125 / ₳738,280; Interoperability 0.25 FTE / $39,375 / ₳246,094; Application runtime 0.5 FTE / $78,750 / ₳492,188; total 2.0 FTE / $315,000 / ₳1,968,750.
- With Product Management & Delivery at 0.25 FTE, total staffing is 2.25 FTE over 9 months.
- The proposal states funding allocations use a market rate of $210,000 per FTE-year, approximately $100/hour, for senior software engineers and senior product leadership with deep DLT expertise.
- Administration uses SundaeSwap treasury-contracts framework with treasury.ak and vendor.ak validators, according to the anchor.
- The anchor states both SundaeSwap contracts have been independently audited by TxPipe and MLabs and are in production use on mainnet.
- Lantr Engineering is named as sole vendor.
- An independent oversight board is named with Chris Gianelloni, Matthias Benkort, and Riley Kilgore, with stated organizations/projects.
- No.Witness Labs is named as independent technical assurer, with quarterly technical reviews to be published.
- The proposal states an external financial auditor will scrutinize Scalus's finances and treasury management, with a goal to publish a report in Q2 2027.
- The permission scheme states disbursement requires Lantr + board majority; sweep early requires Lantr + any 1 board member; pause milestone requires any 1 board member; resume milestone requires board majority.
- The delegation policy states escrow funds enforce auto-abstain DRep delegation and no SPO delegation.
- The failsafe sweep states funds remaining after expiration sweep back to the Cardano Treasury automatically and cannot be overridden.
- Prior funding disclosed includes Catalyst F11 ₳200,000 received 100%, Catalyst F11 ₳128,000 received 100%, Catalyst F13 ₳100,000 received 100%, and 2025 Treasury Budget ₳657,692 received 100%.
- The anchor states all completed milestones were delivered and publicly reported, and the 2025 Treasury Budget allocation is completed.
- Reporting commitments include release updates, quarterly reports, a public transaction journal, and Scalus Club sessions every 1.5 months.
- Measurable adoption indicators include Dijkstra readiness, JVM interoperability, ecosystem reuse, developer reach, application runtime, and documentation/blueprints, with targets and measurement methods listed.
- The risk table identifies Market, Adoption, Technical, and Team risks, all with mitigations.
- The doctrine prioritizes treasury stewardship and downside protection above evidence quality and public-benefit ecosystem growth, after constitutional integrity and protocol safety.
- The doctrine says if ecosystem growth conflicts with treasury stewardship and evidence is weak, prefer ABSTAIN.
- The doctrine says if treasury upside is plausible but non-verifiable, judge directionally on the available public record with a caution penalty; in practice NO or ABSTAIN on thin asks.
- The doctrine states the current soft gate scores TreasuryWithdrawals directionally with an explicit -0.10 caution penalty when a complete dossier is missing.
- The doctrine says AI has collapsed marginal costs and requested ₳ per deliverable should decrease when work can be substantially accelerated by AI tooling.
- The doctrine adopts a rolling-window Net Change Limit framework using available(e) = NCL_annual - sum withdrawals(e - window_size ... e), with window_size = 73 epochs.
- The proposal's constitutionality checklist states it follows a recently established net-change limit of 350M and is within boundaries at submission.

## INFERENCES (analyst reasoning, labeled)
- The requested ₳2,464,844 is about 0.681% of the 36-epoch enacted withdrawals figure of 361,435,336,000,000 lovelace, based on supplied on-chain amounts.
- The 36-epoch treasury flow ratio of 2.275492 indicates enacted withdrawals exceeded inflow over that window; under BEACN doctrine this is relevant to treasury stewardship and downside protection.
- The proposal has comparatively strong financial extraction detail because it provides total ask, USD reference, ADA conversion, category allocation, FTE assumptions, workstream breakdown, milestone period, and escrow/payment controls.
- The proposal has partial but not complete cost-benefit clarity: it names ecosystem reuse, adoption indicators, and target metrics, but supplied material does not provide independently verified ROI, benchmark results, or demand validation beyond anchor assertions.
- Execution risk appears medium from the supplied record because the scope includes Dijkstra readiness and a new scoped runtime, while the proposal narrows prior scope, phases work by milestone, and provides oversight, assurance, reporting, and risk mitigations.
- Technical risk appears medium because Dijkstra specifications may land late or change, and the runtime is a first scoped release; the anchor itself labels that Dijkstra timing risk as medium likelihood and medium impact.
- Governance risk appears low to medium from the record because escrow, board controls, third-party assurance, transaction journaling, and automatic sweep are specified, but the record does not provide the actual signed escrow instance, board acceptance evidence, or audit reports for this action.
- Treasury exposure risk appears medium because the ask is material and on-chain withdrawals exceeded inflow over the supplied 36-epoch window, but the proposal uses milestone escrow, no contingency, a failsafe sweep, and refund/sweep paths.
- The proposal's named alternatives include not funding removed scope items in this action: standalone L1 node, full Gummiworm L2 integration, broad formal verification, and advanced devnet expansion.
- Partial funding could be reasoned from the anchor's separable workstreams and milestones, but no explicit partial-funding option or reduced withdrawal amount is specified in the supplied governance action.
- Deferral could reduce uncertainty around Dijkstra final specifications and allow review of early adoption evidence, but the anchor states Dijkstra readiness is intended ahead of or aligned to the hard-fork timeline.

## UNCERTAINTY (cannot be verified from the record)
- The supplied record does not include independent verification of the stated 4,642 commits, 32 releases, 12 contributors, 20,000+ monthly Scalus.js downloads, or 150+/month Scalus JVM download baseline.
- The supplied record does not include the referenced IPFS annexes as separately retrievable documents beyond text embedded in the anchor excerpt, and the Annex 2 text appears truncated at the end.
- The supplied record does not include the prior DRep feedback record for the previous proposal, only the proposer's characterization of that feedback.
- The supplied record does not include direct evidence that MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, or YaciDevKit currently embed Scalus components, beyond the anchor's statements.
- The supplied record does not include source code, technical benchmarks, conformance test outputs, audit reports, or third-party technical review reports for this 2026 proposal.
- The supplied record does not include evidence that the named oversight board members, No.Witness Labs, or the future financial auditor have formally accepted the roles for this action.
- The supplied record does not include the actual escrow contract address, initialized vendor contract terms, payment schedule dates, or on-chain script parameters for this action.
- The supplied record does not include stake-weighted DRep vote status, SPO/CC status, or ratification probability.
- The supplied on-chain context gives a 36-epoch treasury flow window, while the doctrine's rolling NCL model uses a 73-epoch window; available 73-epoch NCL capacity cannot be computed from the supplied material.
- The supplied record does not verify whether the proposal's stated NCL of 350M is the currently operative parameter beyond the anchor's checklist statement.
- The supplied record does not quantify AI-assisted productivity effects for this work, so the doctrine's AI-cost axiom cannot be applied numerically from the record.
- The supplied record does not show whether the treasury recipient has other recent non-disclosed funding outside the listed Catalyst and 2025 Treasury items.

## Proposal Summary
_grounded: yes_

This TreasuryWithdrawals action requests 2464844000000 lovelace / ₳2,464,844 for Scalus 2026, described as a 9-month continuation from July 2026 to March 2027. The stated work is maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a first scoped application runtime. The proposal describes itself as a reduced resubmission from a prior ₳8.5M / 12-month version, removing a standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion. Delivery is organized into three quarterly milestones with public reporting, oversight board disbursement controls, third-party assurance, and SundaeSwap escrow administration.

Evidence refs: anchor: title; anchor: abstract; anchor: Scope / What Treasury Funds; anchor: Milestones & Deliverables; anchor: What changed since the previous proposal; anchor: Administration; onchain: action type and treasury amount

## Budget Analysis
_grounded: yes_

The total ask is ₳2,464,844, stated as $394,375 at $0.16/ADA, with no contingency. The budget table allocates $315,000 / ₳1,968,750 / 79.9% to Development & Engineering, $39,375 / ₳246,094 / 10.0% to Product Management & Delivery, $25,000 / ₳156,250 / 6.3% to Documentation & Developer Enablement, and $15,000 / ₳93,750 / 3.8% to Audits & Assurance. The engineering workstream table totals 2.0 FTE, and total staffing with product management is 2.25 FTE over 9 months. The methodology states a $210,000 per FTE-year rate, approximately $100/hour. The proposal includes milestone-based escrow, independent co-signing, quarterly reports, public transaction journaling, and automatic sweep of remaining funds after expiration. The supplied on-chain context shows 36-epoch treasury inflow of 158838297854652 lovelace and enacted withdrawals of 361435336000000 lovelace, ratio 2.275492, which is relevant under BEACN's treasury stewardship doctrine.

Evidence refs: anchor: Budget; anchor: Development & Engineering Breakdown; anchor: Administration; anchor: Reporting; anchor: Failsafe Sweep; onchain: treasury flow; doctrine: Values Hierarchy; doctrine: Spending Model: Rolling Window NCL

## Feasibility Assessment
_grounded: yes_

The proposal provides a phased delivery plan: M1 covers continuity and Dijkstra preview, M2 covers interoperability and Dijkstra conformance, and M3 covers Dijkstra readiness and runtime consolidation. It also lists measurable adoption indicators and workstream readiness criteria in Annex 1. Feasibility is supported in the record by claims of prior open-source delivery, prior milestone completion, existing reuse, named team leads, and a narrowed scope. However, independent verification of delivery history, current dependency reuse, benchmarks, and acceptance by oversight/assurance parties is not present in the supplied material. Dijkstra timing remains a stated risk because specifications may land late or change during delivery.

Evidence refs: anchor: Milestones & Deliverables; anchor: Measurable Adoption Indicators; anchor: Annex 1: Detailed Scope and Workstreams; anchor: Lantr Engineering Team; anchor: Prior Treasury Funding Disclosure; anchor: Risks & Mitigations

## Risk Analysis
_grounded: yes_

The anchor identifies four remaining risks: Market risk that ADA price decline below the reference rate compresses the real delivery budget; Adoption risk that adoption may not grow much in 9 months; Technical risk that Dijkstra specifications land late or change; and Team risk from a lean team. The proposal gives mitigations for each, including the $0.16/ADA reference rate, possible conversion to stable assets, no contingency, maintenance/Dijkstra/interoperability value independent of new adoption, developer-preview and conformance paths when final specs are unavailable, and access to a broader network of Scala engineers. BEACN doctrine adds that treasury stewardship and downside protection outrank public-benefit ecosystem growth, and the supplied 36-epoch flow shows withdrawals exceeded inflow over that window. Risk controls include escrow, board disbursement signatures, pause/resume controls, technical assurance, financial audit, public reporting, public transaction journal, auto-abstain DRep delegation, no SPO delegation, and automatic sweep.

Evidence refs: anchor: Risks & Mitigations; anchor: Administration; anchor: Permission Scheme; anchor: Delegation Policy; anchor: Failsafe Sweep; anchor: Reporting; onchain: treasury flow; doctrine: Values Hierarchy; doctrine: Treasury Spending Doctrine

## Alternatives Analysis
_grounded: yes_

Not funding: the proposal itself states the funded work is intended to maintain Scalus, prepare for Dijkstra, improve interoperability, and validate a scoped runtime; not funding would leave those proposed activities unfunded in this action. Partial funding: the supplied governance action does not present a partial-funding option, but the record separates scope by milestones, categories, and workstreams, which makes partial funding conceptually possible though not specified as an executable alternative here. Other providers or mechanisms named in the record: the competitive landscape names Aiken and Plutarch for smart contract development, Yaci Dev Kit for development environment/devnet comparison, Hardhat and Foundry as Ethereum references, and Balius as a Cardano application-framework comparison; the proposal also names existing tools and ecosystems such as MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit. Deferral: deferral could wait for more Dijkstra specification certainty, independent verification of adoption and reuse claims, or initialized escrow/oversight evidence; the record also says the proposal is timed for Dijkstra readiness and July 2026 - March 2027 delivery. Doctrine-relevant alternative: BEACN's framework permits directional scoring from available evidence, with caution on thin or non-verifiable asks, and prioritizes treasury stewardship where evidence is weak.

Evidence refs: anchor: Scope / What Treasury Funds; anchor: Milestones & Deliverables; anchor: Budget; anchor: Annex 2: Competitive Landscape; anchor: Risks & Mitigations; doctrine: Dossier Gate Posture; doctrine: Values Hierarchy

## Failure Mode Analysis
_grounded: yes_

Document-supported failure modes include ADA price decline compressing the real delivery budget, adoption not growing materially within 9 months, late or changing Dijkstra specifications shifting final compatibility work, and key-person disruption in a lean team. Governance/administration failure modes addressed by the record include delivery faltering, which can be met by board co-signing controls and pause capability, and unused funds after expiration, which are stated to sweep automatically back to the Treasury. The doctrine adds treasury-level failure modes from FCFS-style spending: land rush, quality inversion, perverse incentives, and budget cliff; BEACN's rolling-window NCL doctrine is designed to counter those. Unverified failure modes remain around whether the escrow instance, board participation, technical assurance, and financial audit are already operational for this action.

Evidence refs: anchor: Risks & Mitigations; anchor: Permission Scheme; anchor: Failsafe Sweep; anchor: Administration; doctrine: Why Not FCFS-Annual-Reset; doctrine: Rolling Window NCL

## Community Impact
_grounded: yes_

The proposal frames Scalus as open-source Cardano infrastructure under Apache 2.0, reused directly and indirectly across protocols, applications, and tooling. Named direct users or built-on systems include Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm. Named tooling reuse includes MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit. The proposal states educational and community channels include documentation, tutorials, examples, Web2/JVM developer materials, Scalus Club, Cardano Development Hours, Google Summer of Code 2025 mentorship, and UZH Blockchain Summer School collaborations in 2025 and 2026. Impact metrics are enabling rather than direct: the anchor says TVL, monthly transactions, and active users would come from protocols and applications built on Scalus, not from this proposal itself. These community-impact claims are mostly proposer-stated and not independently verified in the supplied record.

Evidence refs: anchor: Motivation; anchor: Cardano 2030 Alignment; anchor: Long-term sustainability through Open Source; anchor: Measurable Adoption Indicators; anchor: Reporting; anchor: Lantr Engineering Team

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
