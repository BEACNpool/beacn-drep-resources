# Deep-research dossier: Strike Finance Liquidity Deployment

- action_id: `gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj`
- action_type: TreasuryWithdrawals
- requested: 9000000000000 lovelace
- drafted: 2026-07-04T16:23:07+00:00 by gpt-5.5 (machine draft — **pending human review**)
- status: drafted_pending_review — `dossier_complete` stays 'no' until approved

## FACTS (document/on-chain supported)
- Action type is TreasuryWithdrawals for title "Strike Finance Liquidity Deployment" with action id gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj. Evidence: onchain: action header; anchor: body.title.
- The requested treasury amount is 9000000000000 lovelace, equivalent to 9000000 ADA. Evidence: onchain: treasury amount; anchor: rationale Terms table requested amount.
- The proposed epoch is 637 and the action expires after epoch 644. Evidence: onchain: action header.
- The anchor describes a 12-month productive treasury deployment, not grant funding. Evidence: anchor: abstract; anchor: rationale Terms, Deployment, and Yield.
- The proposal says the deployed ADA will be sold for USDM, Cardano's fiat-backed stablecoin, to provide stablecoin-denominated liquidity. Evidence: anchor: abstract; anchor: rationale Terms, Deployment, and Yield.
- The proposal models ADA at 0.15 USD, making 9000000 ADA approximately 1350000 USDM, and models 10% USD-denominated APR producing approximately 135000 USD / 900000 ADA-equivalent annual yield. Evidence: anchor: abstract; anchor: rationale Terms, Deployment, and Yield.
- The proposal states modeled estimates are not guaranteed returns. Evidence: anchor: abstract; anchor: rationale Terms, Deployment, and Yield.
- The proposal states realized yield from the first six months will be returned to the Cardano Treasury at month 6, and 100% of treasury-owned deployed assets, including remaining principal and realized yield, will be returned at month 12. Evidence: anchor: abstract; anchor: rationale Terms, Deployment, and Yield.
- The proposed administrator is an independent council composed of Rami from Snek, Phil from Surf, and James from Moneta/Monetra; the anchor uses both spellings. Evidence: anchor: abstract; anchor: rationale Administration, Custody, and Oversight.
- The proposal states Strike Finance will not have unilateral custody or control of treasury assets. Evidence: anchor: abstract; anchor: rationale Terms table; anchor: rationale Administration, Custody, and Oversight.
- The proposal states any ADA held by the administrator before deployment will be kept in one or more separate auditable accounts, not delegated to any stake pool operator, and delegated to the predefined abstain voting option. Evidence: anchor: motivation Liquidity Flywheel; anchor: rationale Administration, Custody, and Oversight.
- The proposal states holding account(s) will be published prior to on-chain submission. Evidence: anchor: rationale Administration, Custody, and Oversight.
- The proposal says Strike V2 is live on mainnet with public performance history and has undergone several unofficial reviews; it says Christian Schmitz is conducting an official audit expected to be finalized by July 1, 2026, with the report to be published upon completion. Evidence: anchor: rationale Independent Audit and Assurance.
- The anchor references independent third-party assurance reports for deployment confirmation, month-6 yield distribution, and month-12 return of funds. Evidence: anchor: rationale Independent Audit and Assurance.
- The proposal states Strike Finance has never received Cardano Treasury funding or any related ecosystem treasury program funding, including within the last 24 months. Evidence: anchor: rationale Previous Treasury Funding.
- The proposal lists primary risks: ADA price appreciation risk, USDM depeg, custody, liquidity, redemption risk, smart contract risk, yield underperformance, and custody and operational risk around multisig coordination. Evidence: anchor: rationale Risk Summary.
- The proposal says governance review is triggered if drawdown exceeds 8%, if reporting is missed for two consecutive monthly cycles, or if any unresolved custody, accounting, stablecoin, redemption, or smart contract concern arises; mandatory review at 10% drawdown. Evidence: anchor: rationale Risk Summary.
- The early termination table states that drawdown of the treasury-owned position exceeding 20% triggers mandatory review and multisig signers may vote to wind down, with review within 7 days of breach. Evidence: anchor: rationale Early Termination and Return of Funds.
- The early termination table states missed reporting for two consecutive monthly cycles without remedy allows multisig signers to vote to wind down, with wind-down decision within 14 days. Evidence: anchor: rationale Early Termination and Return of Funds.
- In wind-down, the proposal states positions are exited in an orderly manner, treasury-owned assets are returned to the designated administrator account, and an audited reconciliation report is published within 30 days. Evidence: anchor: rationale Early Termination and Return of Funds.
- The proposal states monthly public transparency reports will cover deployment status, liquidity utilization, volume, open interest, realized and unrealized profit and loss, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks or deviations. Evidence: anchor: rationale Reporting and Value to Cardano.
- The anchor contains no external references in its references array. Evidence: anchor: references [].
- On-chain DRep vote counts so far are yes=49, no=29, abstain=9, explicit ballots not stake-weighted. Evidence: onchain: DRep vote counts.
- Treasury flow over 36 epochs shows inflow 158838297854652 lovelace, enacted withdrawals 361435336000000 lovelace, ratio 2.275492. Evidence: onchain: treasury flow.
- BEACN doctrine prioritizes treasury stewardship and downside protection above evidence quality and public-benefit ecosystem growth. Evidence: doctrine: values_hierarchy.md.
- BEACN doctrine says if treasury upside is plausible but non-verifiable, judge directionally on the available public record with a caution penalty; in practice NO or ABSTAIN on thin asks. Evidence: doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md Dossier Gate Posture.
- BEACN doctrine rejects first-come-first-served treasury budgeting and adopts a rolling-window Net Change Limit framework. Evidence: doctrine: treasury_spending_doctrine.md Spending Model.
- BEACN doctrine states proposals are funded by DRep approval weight, descending, within available budget rather than by submission order. Evidence: doctrine: treasury_spending_doctrine.md Prioritization.

## INFERENCES (analyst reasoning, labeled)
- The proposal is structured as a reversible liquidity deployment rather than a permanent grant, but that reversibility depends on market, stablecoin, custody, smart contract, and operational conditions identified in the proposal itself.
- Selling ADA for USDM shifts treasury exposure from ADA price exposure to stablecoin and strategy exposure; the proposal explicitly recognizes underperformance versus holding ADA if ADA appreciates significantly.
- The record provides extensive self-reported operating metrics and modeled returns, but because the anchor has an empty references array and no supplied external audit/report documents, independent verification is not available inside this record.
- The on-chain 36-epoch withdrawal ratio of 2.275492 indicates enacted withdrawals exceeded inflows during that window; under BEACN doctrine this increases relevance of treasury stewardship and downside protection for any additional withdrawal.
- The requested 9000000000000 lovelace equals about 5.665% of the 36-epoch treasury inflow figure of 158838297854652 lovelace supplied in the on-chain context.
- The proposal names mechanisms for oversight, reporting, and wind-down, but it does not include executable custody terms, multisig address details, legal contract text, or published holding accounts in the supplied material.

## UNCERTAINTY (cannot be verified from the record)
- The supplied record does not verify Strike's claimed cumulative volume, trade count, user count, revenue, liquidity provider profit, Cardano trading activity share, V2 metrics, vault APR, Sharpe ratio, drawdown, TVL, or depositor count outside the proposal text.
- The supplied record does not include the expected July 1, 2026 audit report or confirm whether it was completed or published.
- The supplied record does not include the independent third-party assurance providers, report templates, engagement terms, or completed assurance reports.
- The supplied record does not include the designated administrator holding account(s), multisig address, signer threshold, key management process, or enforceable custody agreement.
- The supplied record does not show how ADA-to-USDM conversion would be executed, over what time window, through which venues, or with what market-impact controls beyond the statement that it will be orderly.
- The supplied record does not verify USDM liquidity, redemption capacity, depeg risk controls, issuer risk, or concentration limits.
- The supplied record does not define how 'Treasury retains ownership throughout deployment' is legally or technically enforced once ADA is sold for USDM and deployed.
- The supplied record does not provide a complete Net Change Limit calculation, current NCL value, or DRep approval weight needed to verify the claim that the proposal fits within the current 2026 Net Change Limit.
- The supplied record does not identify other named providers of comparable liquidity deployment services, except centralized exchanges, other chains, DeFiLlama rankings/leaderboards, and the Cardano-native Strike Finance mechanism.
- The supplied record contains an inconsistency in the administrator name spelling: James from Moneta in the abstract and James from Monetra in the rationale.

## Proposal Summary
_grounded: yes_

The action requests 9000000000000 lovelace / 9000000 ADA for a 12-month Strike Finance V2 liquidity deployment. The proposal says this is not grant funding: ADA would be sold for USDM, deployed as stablecoin-denominated liquidity, modeled at ADA = 0.15 USD for approximately 1350000 USDM, and expected under modeled assumptions to generate approximately 900000 ADA-equivalent annual yield. The stated structure returns first-six-month realized yield at month 6 and returns 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12. Administration is assigned to an independent council named as Rami from Snek, Phil from Surf, and James from Moneta/Monetra, with Strike Finance not having unilateral custody or control.

Evidence refs: onchain: action header; anchor: abstract; anchor: rationale Terms, Deployment, and Yield; anchor: rationale Administration, Custody, and Oversight

## Budget Analysis
_grounded: yes_

The request is 9000000000000 lovelace. The proposal provides one allocation line: V2 USDM liquidity, 9000000 ADA sold for USDM, to support scalable execution depth and stablecoin markets. It models the conversion at ADA = 0.15 USD, approximately 1350000 USDM, and a 10% USD-denominated APR generating approximately 135000 USD / 900000 ADA-equivalent in annual yield. The proposal states these are modeled estimates, not guaranteed returns. It says the proposal fits within the current 2026 Net Change Limit, but the supplied record does not provide the current NCL value or full rolling-window calculation. On-chain 36-epoch treasury flow shows inflow 158838297854652 lovelace and enacted withdrawals 361435336000000 lovelace, ratio 2.275492. The requested amount is approximately 5.665% of the supplied 36-epoch inflow figure. The document contains milestone-like returns at month 6 and month 12, but it does not show staged treasury disbursement gates before deployment.

Evidence refs: onchain: treasury amount; onchain: treasury flow; anchor: abstract allocation table; anchor: rationale Terms, Deployment, and Yield; anchor: rationale Net Change Limit; doctrine: treasury_spending_doctrine.md Rolling Window NCL

## Feasibility Assessment
_grounded: yes_

The proposal supports feasibility with claimed existing Strike and V2 traction: cumulative trading volume, trade count, unique traders, revenue, liquidity provider profit, V2 volume/trade/user metrics, and vault performance history. It states Strike V2 is live on mainnet and that public performance history exists. It also defines success metrics for 12 months: 30-day volume from 50000000 USD to 1000000000 USD, traders from 2528 to 5000, and annualized revenue run rate from approximately 172000 USD to 5000000 USD. However, the supplied record does not independently verify the claimed historical metrics, does not provide external references, and does not include the official audit report expected by July 1, 2026.

Evidence refs: anchor: motivation Demonstrated Demand; anchor: motivation V2 Liquidity and Trading Activity; anchor: motivation Strike Liquidity Provider Vault; anchor: rationale Strike's Organic Growth; anchor: rationale Success Metrics; anchor: rationale Independent Audit and Assurance; anchor: references []

## Risk Analysis
_grounded: yes_

The proposal identifies material risks: earning less than modeled, drawdown, underperforming a simple hold-ADA strategy, ADA price appreciation after sale to USDM, USDM depeg/custody/liquidity/redemption risk, smart contract risk, yield underperformance from market conditions, and custody/operational risk around multisig coordination. It provides monitoring and intervention triggers: governance review above 8% drawdown, mandatory review at 10% drawdown, review or wind-down options after missed reporting for two consecutive monthly cycles, and a wind-down process if drawdown exceeds 20%. BEACN doctrine places treasury stewardship and downside protection above public-benefit ecosystem growth, and says plausible but non-verifiable treasury upside should receive caution when evidence is thin. The proposal contains risk mitigations, but supplied evidence does not include audit completion, multisig implementation details, assurance reports, or stablecoin risk documentation.

Evidence refs: anchor: rationale Risk Summary; anchor: rationale Early Termination and Return of Funds; anchor: rationale Independent Audit and Assurance; anchor: rationale Administration, Custody, and Oversight; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md Dossier Gate Posture

## Alternatives Analysis
_grounded: yes_

Not funding would preserve treasury ADA and avoid the identified risks of ADA sale, USDM exposure, smart contract risk, yield underperformance, and custody/operational risk; doctrine supports treasury downside protection when evidence is weak or non-verifiable. Partial funding is not explicitly proposed in the anchor, but the proposal's own causal theory is liquidity depth, so a smaller deployment would be an unverified variant with potentially lower market impact and lower treasury exposure; the record does not model partial sizes. Other providers or mechanisms named in the supplied record are centralized exchanges, competing blockchain ecosystems/other chains, DeFiLlama perpetual futures leaderboard protocols, and Strike Finance itself; no specific alternative Cardano-native provider is named. Deferral would allow waiting for the expected official audit report, published holding accounts, multisig details, assurance-provider details, and fresher public performance reports; doctrine permits directional decisions under a soft gate but still requires explicit uncertainty when diligence is incomplete.

Evidence refs: anchor: motivation Liquidity Growth Context; anchor: rationale Market Context; anchor: rationale Independent Audit and Assurance; anchor: references []; doctrine: values_hierarchy.md; doctrine: treasury_spending_doctrine.md Dossier Gate Posture

## Failure Mode Analysis
_grounded: yes_

Failure modes described or implied by the supplied material include: modeled yield not realized; drawdown in the treasury-owned position; ADA appreciating after conversion to USDM, causing underperformance versus holding ADA; USDM depeg, liquidity, redemption, or custody problems; smart contract failure; missed monthly reporting; unresolved custody, accounting, stablecoin, redemption, or smart contract concerns; and multisig coordination or operational failure. The proposal's remedies include governance review triggers, mandatory review thresholds, possible wind-down by multisig signers, orderly exit of positions, return of treasury-owned assets net of realized losses, and an audited reconciliation report within 30 days. The supplied record does not verify whether these remedies are legally binding or technically enforceable.

Evidence refs: anchor: rationale Risk Summary; anchor: rationale Early Termination and Return of Funds; anchor: rationale Reporting and Value to Cardano; anchor: rationale Administration, Custody, and Oversight

## Community Impact
_grounded: yes_

The proposal claims community/ecosystem benefits from deeper Cardano-native perpetual futures liquidity: better execution, larger position capacity, trader retention, more on-chain activity, fee generation, treasury yield, and reduced migration of derivatives demand to centralized exchanges or other chains. It also states monthly public transparency reports will be provided. The supplied record substantiates that these benefits are claimed and gives proposed metrics, but it does not independently verify that the deployment will cause the stated ecosystem effects.

Evidence refs: anchor: motivation Liquidity Flywheel; anchor: rationale Reporting and Value to Cardano; anchor: rationale Success Metrics; anchor: rationale Market Context

---
_Machine-drafted from admitted public inputs only (pinned anchor document, exported
governance CSVs, db-sync metrics). Attestation in the sidecar receipt. This draft does
NOT lower the engine's treasury bar until a human approves it via
`build_deep_research_dossiers.py --approve`._
