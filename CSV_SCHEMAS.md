# CSV Schemas

## registries/resource_registry.csv
- resource_id (string, unique)
- domain (governance|treasury|drep|other)
- action_type (string or `all`)
- source_name (string)
- source_url (URL or repo path)
- format (CSV|JSON|TXT)
- refresh_policy (manual|daily|epoch|other)
- license (string)
- status (approved|deprecated|blocked)

## data/input/governance/governance_actions_sample.csv
- action_id, action_type, epoch, proposer, anchor_url, status

## data/input/treasury/treasury_withdrawals_sample.csv
- action_id, requested_ada, recipient, purpose, evidence_url

## data/input/drep/drep_vote_history_sample.csv
- drep_id, action_id, vote, confidence, recorded_at (ISO-8601)


## data/input/governance/governance_actions_all.csv
- action_id, tx_hash, cert_index, action_type, status
- proposed_epoch, expiration_epoch
- deposit_lovelace, return_address
- anchor_url, anchor_hash, proposer_address
- treasury_amount_lovelace
- drep_yes_pct, drep_no_pct, drep_abstain_pct
- spo_yes_pct, spo_no_pct, spo_abstain_pct
- cc_yes, cc_no, cc_abstain
- flag_score, first_seen, last_updated

## data/input/governance/governance_actions_active.csv
- same schema as `governance_actions_all.csv`

## data/input/governance/governance_treasury_recipients.csv
- action_id, stake_address, amount_lovelace

## data/input/governance/governance_action_flags.csv
- action_id, flag, severity, detail

## data/input/governance/governance_poll_runs.csv
- id, timestamp, source, proposals_found, new_proposals, errors
