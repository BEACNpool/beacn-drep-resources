# Deep-research dossier: Bifrost: Unlocking Bitcoin DeFi on Cardano — Road to Mainnet (Phase 1 of 2)

- action_id: `gov_action1mlvplrdk2t7eyclqeca77ppmfq3sghkr5hdppjqhdqdd573r7q6qqms7jwt`
- action_type: TreasuryWithdrawals
- requested: 12332031000000 lovelace
- drafted: 2026-07-04T15:59:12+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action id is gov_action1mlvplrdk2t7eyclqeca77ppmfq3sghkr5hdppjqhdqdd573r7q6qqms7jwt. Evidence: onchain: action metadata.
- Action type is TreasuryWithdrawals. Evidence: onchain: action metadata.
- Title is "Bifrost: Unlocking Bitcoin DeFi on Cardano — Road to Mainnet (Phase 1 of 2)". Evidence: anchor: body.title; onchain: title.
- Requested treasury amount is 12332031000000 lovelace, equal to ₳12,332,031 as stated in the anchor. Evidence: onchain: treasury amount; anchor: abstract; anchor: Detailed Budget.
- Proposed epoch is 640 and expiry is after epoch 647. Evidence: onchain: action metadata.
- On-chain DRep vote counts so far are yes=2, no=0, abstain=0, explicit ballots and not stake-weighted. Evidence: onchain: DRep vote counts.
- Treasury flow over 36 epochs shows inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492. Evidence: onchain: treasury flow.
- The proposal says FluidTokens and Lantr Engineering request ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month delivery period from July 2026 to March 2027. Evidence: anchor: abstract; anchor: Detailed Budget.
- The proposal describes Phase 1 as taking Bifrost from working testnet to launch readiness, covering hardening, security audits, formal verification, ecosystem and partner readiness, stewardship, and economic foundations. Evidence: anchor: abstract; anchor: Roadmap & Budget overview.
- The proposal says public rollout and 24 months of operations are separated into a Phase 2 proposal in Q1 2027. Evidence: anchor: abstract; anchor: Phase 2 Launch & Operations.
- The proposal states that by the end of Phase 1, Bifrost will be an audited bridge running on Cardano mainnet in both custody modes, federated and SPO threshold, under controlled access. Evidence: anchor: abstract; anchor: M3 objective and deliverables.
- The proposal states Bifrost is currently funded through Catalyst Fund 14 for ₳739,000, with deliverables of Architecture, Testnet MVP, and Documentation, and a Dec 2025 - Aug 2026 timeline marked on track. Evidence: anchor: Catalyst Fund 14 table.
- Catalyst milestone status in the anchor says M1 and M2 are done and approved, M3 is submitted awaiting Catalyst signoff, M4 and M5 are on track for July 2026, and final reporting is on track for August 2026. Evidence: anchor: Catalyst milestone status.
- The anchor says the bridge is live and operational on testnet, with peg-in between Bitcoin Testnet4 and Cardano Preprod fully working and open to anyone, and gives transaction hash a43ce4586939509d0845bb9cf1e5a9b6242faca2b977d31b484d225b9c9ae6db. Evidence: anchor: Testnet live today.
- The anchor names SPOs BTBF, ADA North Pool, BCSH, EASY1, and DAVE as volunteers for the testnet release. Evidence: anchor: Working with SPOs.
- The anchor names Minswap, SundaeSwap, Masumi, Gravity, DeltaDefi, Liqwid, FluidTokens, and Vela Finance as Cardano applications that expressed interest in integrating Bifrost or fBTC. Evidence: anchor: Cardano dApps engagement.
- The Phase 1 budget overview allocates $1,363,750 / ₳8,523,438 / 76.0% to Bridge hardening & Security, $177,500 / ₳1,109,375 / 9.9% to Ecosystem readiness & partnerships, and $252,500 / ₳1,578,125 / 14.1% to Legal, stewardship & economy. Evidence: anchor: Budget overview.
- The detailed budget lists subtotal $1,793,750 / ₳11,210,938, refundable contingency $179,375 / ₳1,121,094, and total $1,973,125 / ₳12,332,031. Evidence: anchor: Detailed Budget.
- The detailed budget lists 52.5 FTE-months, fixed USD $875,000, engineering and product capacity priced at $210,000 per FTE-year, and $100/hour blended rate for senior DLT engineers and product leadership. Evidence: anchor: Detailed Budget; anchor: Pricing principles.
- The proposal says unspent contingency is returned to the Cardano Treasury at the end of the term. Evidence: anchor: Detailed Budget; anchor: Pricing principles.
- The proposal says a portion of requested ADA will be hedged into stable assets shortly after disbursement to protect delivery and security audits budget against adverse price movement. Evidence: anchor: Pricing principles.
- The proposal says Bifrost is open source under Apache 2.0 and has no bridge token, no founder allocation, and no built-in revenue claim on the protocol for the founding teams. Evidence: anchor: Public infrastructure.
- The proposal says the bridge will be held by an independent stewardship structure, a foundation or equivalent independent form, determined in Phase 1. Evidence: anchor: Public infrastructure; anchor: Ownership & stewardship.
- The proposal says fee revenue is denominated in fBTC and includes peg-in fee, peg-out fee, atomic-swap fast-lane fee, and sponsored transactions. Evidence: anchor: Revenue Model & Sustainability.
- The proposal describes a revenue waterfall: mechanism reserve, maintenance reserve, governance reserve, and surplus split between an SPO retainer pool and the Cardano Treasury with indicative default 35% / 65%, both in fBTC. Evidence: anchor: Revenue distribution.
- The proposal says the exact reserve target is set during Phase 1 hardening and gives an indicative reserve target of 12 months of mandatory operations plus 1 SPO retainer pool cycle, with surplus distribution pausing below a 6-month safety floor. Evidence: anchor: Revenue distribution.
- BEACN doctrine prioritizes treasury stewardship and downside protection above evidence quality and public-benefit ecosystem growth, after constitutional integrity and protocol safety. Evidence: doctrine: values_hierarchy.md.
- BEACN doctrine says TreasuryWithdrawals without a complete dossier are scored directionally under a soft gate with explicit uncertainty and a -0.10 caution penalty, and thin or unverifiable asks resolve in practice to NO or ABSTAIN. Evidence: doctrine: treasury_spending_doctrine.md.
- BEACN doctrine rejects first-come-first-served treasury models and adopts a rolling-window Net Change Limit framework. Evidence: doctrine: treasury_spending_doctrine.md.
- BEACN doctrine states that if work can be substantially accelerated by AI tooling, the budget should reflect post-AI costs, not legacy labor models. Evidence: doctrine: treasury_spending_doctrine.md.

## INFERENCES (analyst reasoning, labeled)
- The request is large relative to recent treasury flow context: ₳12,332,031 is about 7.76% of the stated 36-epoch inflow of 158838297854652 lovelace, and recent enacted withdrawals exceed inflow by a 2.275492 ratio. This is an arithmetic inference from onchain figures.
- The proposal provides a detailed budget and milestone structure, but payment gates are not explicitly tied to on-chain or escrowed milestone disbursements in the supplied text. This affects extraction of milestone payment gates.
- The contingency refund path is partially evidenced because the anchor states unspent contingency returns to the Treasury, but the supplied text does not specify the operational mechanism, enforcement path, escrow, or clawback procedure.
- The proposal creates a recurring funding dependency because it explicitly separates public launch and 24 months of operations into a Phase 2 proposal estimated at $1.3M in Q1 2027.
- The proposal’s public-benefit case is substantively documented, but many claimed external market facts, security comparisons, integration interest, and testnet status are not independently verified within the supplied record beyond proposer statements.
- The security and technical risk surface is high because the proposal concerns a Bitcoin-Cardano bridge, threshold custody, audits, formal verification, watchtowers, SPO coordination, and real BTC under controlled mainnet access; the anchor itself frames audits, formal verification, bug bounty, and penetration testing as necessary before public launch.
- The governance risk is medium to high because the long-term stewardship structure, jurisdiction, governance charter, fee parameters, reserve targets, and distribution bounds are not finalized at proposal time and are Phase 1 deliverables.
- The treasury exposure risk is medium to high because funding is requested in ADA at a $0.16/ADA reference rate, the proposal plans stable-asset hedging after disbursement, and recent treasury outflows exceed inflows in the supplied on-chain window.

## UNCERTAINTY (cannot be verified from the record)
- The supplied record does not independently verify the testnet URL, transaction hash, Catalyst status, SPO participation, dApp interest, audits history, team track record, or claimed prior Catalyst delivery.
- The supplied record does not include recipient address history, prior treasury withdrawal history for FluidTokens or Lantr Engineering, legal identities, corporate documents, or contract terms.
- The anchor text is truncated after the Ownership & stewardship section, so any omitted reporting, annex, or disbursement details cannot be assessed.
- The supplied material does not show an escrow arrangement, milestone-payment contract, refund enforcement mechanism, or clawback path for non-delivery.
- The supplied material does not name external audit firms for Phase 1, formal verification providers, bug bounty platform, or committed partners for mainnet launch.
- The proposal says some fee schedules, reserve targets, stewardship form, jurisdiction, and governance parameters are provisional or to be determined during Phase 1.
- The supplied material does not provide a complete Net Change Limit value for the relevant rolling window, so budget capacity under BEACN’s doctrine cannot be fully computed.
- The supplied material does not quantify expected Phase 2 ask in ADA, only an estimated $1.3M for Launch & Operations in Q1 2027.
- The supplied material does not provide deterministic evidence that claimed BTC TVL, wallet, transaction, dApp integration, or revenue projections are achievable.
- The supplied material does not specify what happens if audits fail, critical findings are not remediated, adoption is below projections before Phase 2, or the stewardship structure cannot be established.

## Proposal Summary
_grounded: yes_

This TreasuryWithdrawals action requests 12332031000000 lovelace for "Bifrost: Unlocking Bitcoin DeFi on Cardano — Road to Mainnet (Phase 1 of 2)." The anchor states the requested amount as ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for July 2026 through March 2027. Phase 1 is described as a nine-month effort to harden a Catalyst-funded Bitcoin-Cardano bridge from testnet toward audited controlled-access mainnet readiness, including audits, formal verification, partner readiness, stewardship setup, and economic-model hardening. Public launch and 24 months of operations are excluded and deferred to a Phase 2 proposal in Q1 2027.

Evidence refs: onchain: action metadata; onchain: treasury amount; anchor: body.title; anchor: abstract; anchor: Roadmap & Budget overview; anchor: Detailed Budget

## Budget Analysis
_grounded: yes_

The Phase 1 budget is detailed at workstream and line-item level. The budget overview totals $1,793,750 / ₳11,210,938 before contingency and $1,973,125 / ₳12,332,031 after a $179,375 / ₳1,121,094 refundable contingency. Workstream allocation is $1,363,750 / ₳8,523,438 for Bridge hardening & Security, $177,500 / ₳1,109,375 for Ecosystem readiness & partnerships, and $252,500 / ₳1,578,125 for Legal, stewardship & economy. The detailed budget lists 52.5 FTE-months, $875,000 fixed USD, and a $210,000 per FTE-year / $100/hour blended pricing assumption. The anchor states that unspent contingency returns to the Cardano Treasury and that part of the ADA will be hedged into stable assets after disbursement. The record does not specify escrow, milestone payment mechanics, or enforceable clawback beyond unspent contingency. On-chain context shows recent 36-epoch enacted withdrawals of 361435336000000 lovelace against inflow of 158838297854652 lovelace, ratio 2.275492, which is relevant under BEACN treasury stewardship doctrine.

Evidence refs: anchor: Budget overview (Phase 1); anchor: Detailed Budget; anchor: Pricing principles; onchain: treasury flow; doctrine: treasury_spending_doctrine.md

## Feasibility Assessment
_grounded: yes_

The anchor supplies a feasibility narrative: prior Catalyst Fund 14 funding of ₳739,000, a stated testnet deployment on Bitcoin Testnet4 and Cardano Preprod, milestone status through Catalyst, named volunteer SPOs, named dApps expressing interest, and component maturity from Catalyst scope to Phase 1 needs. Phase 1 deliverables are organized into M1 hardening and audit readiness, M2 audits and mainnet preparation, and M3 private mainnet audited and running. Acceptance evidence includes public commits, published documentation, audit reports, test coverage, runbooks, public transaction hashes, a transparency portal, a stewardship charter, and a published hardened economic model. Feasibility remains dependent on unverified proposer claims in the supplied anchor because the record provided here does not independently validate testnet state, SPO participation, dApp commitments, team capacity, or external audit availability.

Evidence refs: anchor: Catalyst Fund 14; anchor: Catalyst milestone status; anchor: Testnet live today; anchor: Working with SPOs; anchor: Cardano dApps engagement; anchor: Component maturity; anchor: Milestones and deliverables

## Risk Analysis
_grounded: yes_

The proposal itself identifies a security-sensitive domain: BTC custody, threshold signing, federated fallback, watchtowers, Cardano smart contracts, Bitcoin Taproot scripts, FROST/Schnorr, DKG ceremony, audits, formal verification, penetration testing, and bug bounty. Technical risk is therefore substantively present in the record, and the proposed mitigations are also named. Governance risk remains because the stewardship structure, jurisdiction, fee governance, reserve target, and some economic parameters are Phase 1 outputs rather than pre-existing settled facts. Treasury risk is material under the supplied on-chain context because recent enacted withdrawals exceed inflow over the stated 36-epoch window, and this action requests ₳12,332,031 with an additional Phase 2 funding path later. The anchor mentions stable-asset hedging after disbursement, which may protect delivery budget but also introduces treasury exposure and execution details not fully specified in the supplied text.

Evidence refs: anchor: How Bifrost works; anchor: Milestones and deliverables; anchor: Revenue Model & Sustainability; anchor: Ownership & stewardship; anchor: Pricing principles; onchain: treasury flow; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Alternatives Analysis
_grounded: yes_

Not funding is covered by doctrine as a treasury-protective option when evidence is weak or downside protection dominates ecosystem growth; it would avoid this ₳12,332,031 withdrawal but would also leave the proposal’s stated testnet-to-mainnet Phase 1 unfunded from this action. Partial funding is not directly offered as a mechanism in the action text, but the record separates Phase 1 from Phase 2 and decomposes Phase 1 by milestones and workstreams, so a partial-funding concept could map only to supplied components such as hardening/security, ecosystem readiness, or legal/stewardship; no alternate partial amount or reduced acceptance scope is specified. Other providers or mechanisms named in the record include Catalyst Fund 14, FluidTokens, Lantr Engineering, Cardano Foundation, Intersect, external audit firms not named by name, public bug bounty platform not named by name, dApp integrations, SPO participation, SDK/white-label distribution, and fee-funded operations after adoption. Deferral is explicitly present as a doctrine-compatible option where risk or evidence is insufficient, and the proposal itself defers public launch and 24 months of operations to Phase 2 in Q1 2027; deferring Phase 1 would wait for more Catalyst completion evidence, testnet verification, stewardship details, audit commitments, or NCL capacity information, none of which is fully supplied here.

Evidence refs: anchor: Roadmap & Budget overview; anchor: Phase 2 - Adoption plan; anchor: Detailed Budget; anchor: Ownership & stewardship; anchor: Catalyst Fund 14; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Failure Mode Analysis
_grounded: yes_

The supplied material supports several proposal-specific failure modes: audits or formal verification reveal critical issues that delay or block mainnet readiness; SPO threshold coordination fails and the federated fallback is needed; stewardship form, jurisdiction, or charter cannot be completed before Phase 2; economic model assumptions require revision; partner or SPO interest does not convert into commitments; adoption underperforms the Base case; reserves fall below the 6-month safety floor, causing surplus distribution to pause; and below-Base adoption for two consecutive quarters triggers a course-correction review. The supplied text names some mitigations, including audits, formal verification, penetration testing, bug bounty, controlled-access private mainnet, monitoring, observability, incident-response drills, stewardship governance, and reserve policy. The record does not provide detailed rollback mechanics, insurance, emergency shutdown authority, user compensation rules, or non-delivery clawback.

Evidence refs: anchor: Milestones and deliverables; anchor: How Bifrost works; anchor: Revenue Model & Sustainability; anchor: Phase 2 - Adoption plan; anchor: Component maturity

## Community Impact
_grounded: yes_

The anchor frames Bifrost as public infrastructure for Cardano and BTC holders, with claimed benefits to Cardano TVL, transactions, active users, dApp addressable market, SPO revenue roles, and Bitcoin-holder access to Cardano DeFi. It states there is no bridge token, no founder allocation, open-source Apache 2.0 code, public accountability, and independent stewardship. It also claims alignment with Cardano 2030 KPIs and pillars, with Base Q2 2029 targets of 1,200 BTC TVL, approximately 600K annual transactions, 3,000 fBTC-holding wallets, and fee-funded surplus to Treasury. These are proposal claims and projections in the supplied record, not independently verified outcomes.

Evidence refs: anchor: Public infrastructure; anchor: Benefits for the ecosystem; anchor: Cardano 2030 alignment; anchor: Adoption targets; anchor: Revenue Model & Sustainability

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
