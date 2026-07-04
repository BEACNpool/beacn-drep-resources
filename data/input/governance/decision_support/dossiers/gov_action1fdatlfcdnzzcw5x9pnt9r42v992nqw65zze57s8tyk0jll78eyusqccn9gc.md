# Deep-research dossier: Cardano Builder DAO

- action_id: `gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc`
- action_type: TreasuryWithdrawals
- requested: 20000000000000 lovelace
- drafted: 2026-07-04T16:06:27+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action id is gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc. Evidence: onchain: action header.
- Action type is TreasuryWithdrawals. Evidence: onchain: action header.
- Title is Cardano Builder DAO. Evidence: onchain: action header; anchor: body.title.
- Requested treasury amount is 20000000000000 lovelace. Evidence: onchain: action header.
- Proposed epoch is 639 and expires after epoch 646. Evidence: onchain: action header.
- On-chain DRep explicit ballot counts so far are yes=17, no=20, abstain=0, not stake-weighted. Evidence: onchain: DRep vote counts.
- Treasury flow over 36 epochs is inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492. Evidence: onchain: treasury flow.
- The anchor describes the Cardano Builder DAO as an ecosystem-wide, purpose-built, smart contract-governed funding mechanism to support projects advancing Cardano Vision 2030 through measurable ecosystem KPIs including monthly active users, monthly on-chain transactions, and TVL. Evidence: anchor: abstract.
- The proposal states the DAO has already distributed 11.1 M ADA across 34 proposals in 2 funding rounds. Evidence: anchor: CB DAO Track Record.
- The proposal states Round 1 had 38 voting members, 27 requesting members, funded 20 companies, achieved 83% participation in governance actions, and distributed 5,541,335 ADA. Evidence: anchor: CB DAO Track Record.
- The proposal states Round 2 had 18 new members joining, funded 14 companies, and had 88% participation among members. Evidence: anchor: CB DAO Track Record.
- The proposal states the DAO built Version 1 and Version 2 of a DAO KPI dashboard; Version 1 used self-reported KPI tracking and Version 2 moved toward KPI tracking tied directly to live on-chain Cardano data. Evidence: anchor: Alignment with the 2030 Vision KPI Framework.
- The proposal states funded projects are required to track monthly active users, TVL, and on-chain transactions. Evidence: anchor: Alignment with the 2030 Vision KPI Framework.
- The proposal names an Independent council as administrator, composed of members of the dRep DAO, to receive the treasury withdrawal, hold funds prior to deployment, and oversee disbursement in line with milestones in the referenced Milestone and Budget Document. Evidence: anchor: Administrator; anchor: references Milestone and Budget Document.
- The proposal states Cardano Yoda and Marco Grendel Moshi have put their names forward for the council and that one other non-affiliated active dRep will be added to conduct reviews. Evidence: anchor: Administrator.
- The proposal states ADA held by the administrator prior to further disbursement will be kept in one or more separate accounts auditable by the Cardano Community, will not be delegated to any stake pool operator, and will be delegated to the predefined abstain voting option. Evidence: anchor: Administrator.
- The proposal states all milestones will be dispersed from an independent multisig governed by assigned members of the dRep DAO, and that the Cardano Builder DAO only receives funds after milestone completion is validated and confirmed by administrator. Evidence: anchor: Administrator.
- The proposal states repayment would occur if DAO treasury funds remain unused or unallocated after completion of approved work, governance processes, or funding activities; unused portions would be returned to the Cardano Treasury. Evidence: anchor: Repayment.
- The proposal states the CB DAO returned 354,790 ADA of unused funds to the treasury after the first two governance rounds completed and provides an adastat transaction URL. Evidence: anchor: Repayment.
- The proposal states the Cardano Builder DAO previously received funding through the Cardano Treasury funding process. Evidence: anchor: prior funding question.
- The proposal states Clarity, the technical and business development team responsible for enabling Initiative DAOs, will not seek funding as a requesting member through any initiative DAOs. Evidence: anchor: prior funding question.
- The anchor references external documents and portals including CB DAO Reflections, Round 1 Retrospective, Round 2 Retrospective, Milestone and Budget Document, governance portals for rounds 1 and 2, and CB DAO Code of Conduct. Evidence: anchor: references.
- BEACN doctrine prioritizes treasury stewardship and downside protection above evidence quality and public-benefit ecosystem growth. Evidence: doctrine: values_hierarchy.md.
- BEACN doctrine rejects first-come-first-served budget models and adopts a rolling-window Net Change Limit framework. Evidence: doctrine: treasury_spending_doctrine.md.
- BEACN doctrine states TreasuryWithdrawals without a complete dossier are scored directionally with an explicit -0.10 caution penalty under the current soft gate, and incomplete diligence is recorded as explicit uncertainty. Evidence: doctrine: Dossier Gate Posture.
- BEACN doctrine states if ecosystem growth conflicts with treasury stewardship and evidence is weak, prefer ABSTAIN. Evidence: doctrine: values_hierarchy.md.
- BEACN doctrine states if treasury upside is plausible but non-verifiable, judge directionally on available public record with a caution penalty; in practice NO or ABSTAIN on thin asks. Evidence: doctrine: values_hierarchy.md.

## INFERENCES (analyst reasoning, labeled)
- The requested 20000000000000 lovelace equals 20,000,000 ADA if using the standard 1 ADA = 1,000,000 lovelace conversion; this conversion is arithmetic from the supplied lovelace amount, not separately stated in the anchor.
- The action requests a large treasury withdrawal relative to the supplied 36-epoch treasury inflow: 20000000000000 / 158838297854652 is approximately 12.5914%. This is arithmetic from on-chain figures.
- The action would add to a recent context where enacted withdrawals over 36 epochs already exceed inflow by a ratio of 2.275492, so treasury-stewardship scrutiny is material under BEACN doctrine.
- The proposal provides governance, custody, milestone, and repayment mechanisms at a high level, but the referenced Milestone and Budget Document content is not supplied in the record; detailed milestone amounts, dates, and acceptance criteria cannot be verified here.
- The proposal’s KPI theory is aligned with the doctrine’s public-benefit ecosystem growth value, but the supplied anchor does not provide independently verifiable outcome data for prior funded projects beyond aggregate funding/governance participation claims and claimed dashboard evolution.
- The named administrator structure reduces some custody and disbursement ambiguity relative to a direct unrestricted transfer, but one council seat is not yet named in the supplied anchor.
- Because the supplied material says the DAO only receives funds after milestone completion is validated and confirmed by administrator, the proposal contains milestone payment gating at a conceptual level; however, detailed gate criteria are outside the supplied text.
- The repayment language creates a stated refund path for unused or unallocated funds, but the supplied material does not define enforcement mechanics beyond the stated commitment and prior-return claim.

## UNCERTAINTY (cannot be verified from the record)
- The supplied record does not include the contents of the referenced Milestone and Budget Document, so budget line items, milestone schedule, milestone acceptance criteria, per-category allocations, and runway assumptions cannot be verified.
- The supplied record does not include the referenced retrospectives, governance portal records, code of conduct, or developer documentation; claims relying on those external references are not independently verified in this dossier.
- The supplied record does not verify the adastat transaction details for the stated 354,790 ADA return; only the proposal’s claim and URL are present.
- The supplied record does not provide recipient address history, administrator wallet addresses, multisig policy details, signatory threshold, legal entity details, or enforcement contracts for repayment.
- The supplied record does not identify the third non-affiliated active dRep administrator.
- The supplied record does not quantify expected KPI improvements, target MAU, transaction, or TVL outcomes, or time horizons for those outcomes.
- The supplied record does not show whether prior distributed 11.1 M ADA produced measured ecosystem growth, only that funds were distributed and KPI tracking existed according to the proposal.
- The supplied record does not specify whether the requested 20000000000000 lovelace is intended for one funding round, multiple rounds, operating costs, grants, administrator costs, or reserves.
- The supplied record does not provide a comparison to alternative funding mechanisms other than references to traditional community funding mechanisms, Initiative DAOs, smart contract-governed DAO allocation, and BEACN doctrine’s NCL/DRep approval framework.

## Proposal Summary
_grounded: yes_

Cardano Builder DAO requests 20000000000000 lovelace through a TreasuryWithdrawals action proposed in epoch 639 and expiring after epoch 646. The anchor describes the DAO as a smart contract-governed funding mechanism for builders advancing Vision 2030 KPIs: monthly active users, monthly on-chain transactions, and TVL. The proposal claims prior operation across 2 rounds, 34 funded proposals, 11.1 M ADA distributed, and a 354,790 ADA return of unused funds. The proposed administrator is an Independent council of dRep DAO members, with Cardano Yoda and Marco Grendel Moshi named and one additional non-affiliated active dRep to be added. Funds are described as held before deployment, disbursed from an independent multisig after milestone completion is validated, and unused/unallocated funds are to be returned to the Cardano Treasury.

Evidence refs: onchain: action header; anchor: abstract; anchor: CB DAO Track Record; anchor: Administrator; anchor: Repayment

## Budget Analysis
_grounded: yes_

The on-chain request is 20000000000000 lovelace. The supplied anchor does not include a budget table or allocation breakdown; it only references a separate Milestone and Budget Document whose contents are not supplied. The proposal gives prior funding figures: 11.1 M ADA distributed across 34 proposals in 2 rounds; Round 1 distributed 5,541,335 ADA; and 354,790 ADA was allegedly returned unused after the first two governance rounds. The 36-epoch treasury context shows inflow 158838297854652 lovelace and enacted withdrawals 361435336000000 lovelace, ratio 2.275492. Arithmetic inference: the requested amount is approximately 12.5914% of the supplied 36-epoch inflow. BEACN doctrine requires treasury stewardship and downside protection and rejects FCFS-style depletion, favoring rolling-window NCL scrutiny.

Evidence refs: onchain: action header; onchain: treasury flow; anchor: CB DAO Track Record; anchor: Repayment; anchor: references Milestone and Budget Document; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md

## Feasibility Assessment
_grounded: yes_

The anchor supports a basic feasibility case by claiming the DAO has already run 2 funding rounds, funded 34 proposals, distributed 11.1 M ADA, run governance processes with 83% and 88% participation rates in Rounds 1 and 2 respectively, created/amended governing documents, elected a board, added third-party assurance, implemented merit-based proposal review, and executed treasury withdrawals on-chain. It also claims KPI dashboard work progressed from self-reported tracking to tracking tied to live on-chain Cardano data. However, operational details required to validate current execution capacity, exact milestone schedule, administrator multisig parameters, and KPI verification methodology are not supplied.

Evidence refs: anchor: CB DAO Track Record; anchor: Alignment with the 2030 Vision KPI Framework; anchor: Administrator

## Risk Analysis
_grounded: yes_

Treasury exposure is material because the action requests 20000000000000 lovelace while the supplied 36-epoch treasury flow already shows enacted withdrawals exceeding inflow by a ratio of 2.275492. Governance/custody risk is partially addressed by the proposed Independent council, separate auditable accounts, no SPO delegation, abstain voting delegation, independent multisig, milestone validation by administrator, and repayment language for unused or unallocated funds. Execution and measurement risk remain because detailed milestones, budget allocation, acceptance criteria, administrator wallet/signatory details, and quantified KPI targets are not present in the supplied record. BEACN doctrine says thin or non-verifiable treasury upside should receive a caution penalty and incomplete diligence should be recorded as uncertainty.

Evidence refs: onchain: treasury flow; onchain: action header; anchor: Administrator; anchor: Repayment; doctrine: Dossier Gate Posture; doctrine: values_hierarchy.md

## Alternatives Analysis
_grounded: yes_

Not funding: under BEACN doctrine, protecting the treasury is a valid fail-safe when evidence is thin or downside protection is insufficient; the doctrine states voting NO protects the treasury and does not spend it. Partial funding: the supplied record does not describe a partial-funding option or lower requested amount, but the presence of milestones and administrator-controlled disbursement implies funding could be staged if governance supplied a different amount or mechanism; this is an inference, not a documented option. Other providers or mechanisms named in the record: the anchor contrasts CB DAO with traditional community funding mechanisms and mentions Initiative DAOs enabled by Clarity; BEACN doctrine names rolling-window NCL and DRep approval threshold as treasury allocation mechanisms. The proposal also references smart contract-governed DAO allocation as its mechanism. Deferral: the supplied record supports deferral as an evidence-quality response because the Milestone and Budget Document and linked retrospectives are not included; BEACN doctrine says if data freshness or anchor integrity is degraded, do not force directional confidence, and weak evidence against treasury stewardship can support ABSTAIN.

Evidence refs: anchor: motivation; anchor: prior funding question; anchor: references Milestone and Budget Document; doctrine: Dossier Gate Posture; doctrine: treasury_spending_doctrine.md; doctrine: values_hierarchy.md

## Failure Mode Analysis
_grounded: yes_

Identified failure modes from supplied material and doctrine include: treasury overdraw pressure if large withdrawals continue while 36-epoch enacted withdrawals exceed inflow; weak verification if KPI claims remain narrative or self-reported rather than tied to live on-chain data; governance/custody concentration if administrator details, multisig thresholds, or the third council member remain unspecified; milestone ambiguity because the referenced milestone/budget document is not supplied; and FCFS/queue depletion risk addressed generally by BEACN doctrine’s rejection of first-come-first-served spending. The proposal’s stated mitigations are administrator custody, auditable separate accounts, abstain voting delegation, independent multisig, milestone validation, KPI tracking, and repayment of unused/unallocated funds.

Evidence refs: onchain: treasury flow; anchor: Alignment with the 2030 Vision KPI Framework; anchor: Administrator; anchor: Repayment; anchor: references Milestone and Budget Document; doctrine: treasury_spending_doctrine.md

## Community Impact
_grounded: yes_

The anchor’s community-impact thesis is that funding experienced builders through a DAO can increase Cardano usage, monthly active users, monthly transactions, and TVL. It claims prior ecosystem adoption through more than 50 established Cardano projects participating in funding decisions as described by official Cardano developer documentation, but the referenced documentation is not supplied. It also claims 20 companies were funded in Round 1 and 14 in Round 2. The supplied record does not verify downstream user, transaction, or TVL impact from those funded companies.

Evidence refs: anchor: abstract; anchor: motivation; anchor: Alignment with the 2030 Vision KPI Framework; anchor: CB DAO Track Record

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
