#!/usr/bin/env python3
import csv
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registries"
OUT = ROOT / "data" / "input" / "governance"


def load_csv(path: Path):
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    registry = load_csv(REG / "resource_registry.csv")
    playbook = load_csv(REG / "action_resource_playbooks.csv")

    approved = {r["resource_id"]: r for r in registry if (r.get("status") or "").lower() == "approved"}

    by_type = {}
    for row in playbook:
        if (row.get("enabled") or "true").lower() != "true":
            continue
        rid = row.get("resource_id")
        if rid not in approved:
            continue
        action_type = (row.get("action_type") or "all").lower()
        entry = {
            "priority": int(row.get("priority") or 99),
            "resource_id": rid,
            "source_url": approved[rid].get("source_url"),
            "format": approved[rid].get("format"),
            "query_hint": row.get("query_hint", ""),
            "why_it_matters": row.get("why_it_matters", ""),
        }
        by_type.setdefault(action_type, []).append(entry)

    for k in by_type:
        by_type[k] = sorted(by_type[k], key=lambda x: (x["priority"], x["resource_id"]))

    out = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_files": {
            "resource_registry": str((REG / "resource_registry.csv").relative_to(ROOT)),
            "action_playbook": str((REG / "action_resource_playbooks.csv").relative_to(ROOT)),
        },
        "action_resource_index": by_type,
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "action_resource_index.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"action_types": len(by_type), "output": str((OUT / 'action_resource_index.json').relative_to(ROOT))}))


if __name__ == "__main__":
    main()
