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
