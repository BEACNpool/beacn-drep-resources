# Resource Intelligence Plan (Action-Specific Learning)

Goal: make the bot faster and smarter at finding the most relevant evidence for each governance action type.

## Principles
- Relevance first: every action type has a playbook of prioritized resources.
- Public only: all sources must be admitted through the resource registry.
- Reproducible: generated indices/manifests are versioned and hashable.
- Conservative: low evidence depth triggers `NEEDS_MORE_INFO` / `ABSTAIN`.

## Resource discovery flow
1. Detect action type from governance snapshot.
2. Load `registries/action_resource_playbooks.csv`.
3. Gather high-priority resources for that action type (`priority <= 2`).
4. Add medium-priority context resources (`priority == 3`) if needed.
5. Build `data/input/governance/action_resource_index.json` for core.
6. Core uses this index to focus evidence extraction before recommendation.

## Cadence recommendation
- Every 6 hours: refresh governance snapshots.
- Daily at 01:00 UTC: refresh action-resource index.
- Weekly: review source quality and add/remove resources via PR.

## Qualification for adding resources
- Source must improve action-specific evidence depth.
- Source must be public and replayable.
- Source must include stable reference (URL/path + hashable content).
- Change must be committed and documented.
