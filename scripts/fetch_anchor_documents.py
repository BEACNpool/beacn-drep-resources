#!/usr/bin/env python3
import csv
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = Path(__file__).resolve().parents[1]
GOV = ROOT / "data" / "input" / "governance"
ACTIONS = GOV / "governance_actions_all.csv"
ANCHOR_DIR = GOV / "anchors"
INDEX_CSV = GOV / "anchor_documents_index.csv"
MANIFEST = GOV / "anchor_documents_manifest.json"


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def slug(s: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", s.strip())
    return s[:140] or "anchor"


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _ipfs_gateway_prefixes() -> list[str]:
    env = os.environ.get("IPFS_GATEWAYS", "").strip()
    if env:
        vals = [x.strip() for x in env.split(",") if x.strip()]
        return [v if v.endswith("/") else v + "/" for v in vals]
    return [
        "https://ipfs.io/ipfs/",
        "https://dweb.link/ipfs/",
        "https://gateway.pinata.cloud/ipfs/",
        "https://cloudflare-ipfs.com/ipfs/",
    ]


def candidate_urls(url: str) -> list[str]:
    u = (url or "").strip()
    if not u:
        return []
    if u.startswith("ipfs://"):
        target = u[len("ipfs://"):].lstrip("/")
        return [g + target for g in _ipfs_gateway_prefixes()]
    return [u]


def fetch_bytes(url: str, timeout: int = 20) -> tuple[int, bytes, str, str]:
    last_err = None
    for cand in candidate_urls(url):
        try:
            req = Request(cand, headers={"User-Agent": "beacn-drep-resources/anchor-fetcher"})
            with urlopen(req, timeout=timeout) as resp:
                status = getattr(resp, "status", 200)
                ctype = resp.headers.get("Content-Type", "")
                return int(status), resp.read(), ctype, cand
        except (HTTPError, URLError) as e:
            last_err = e
            continue

    if last_err:
        raise last_err
    raise URLError("no candidate URLs")


def main():
    if not ACTIONS.exists():
        raise SystemExit(f"missing actions csv: {ACTIONS}")

    ANCHOR_DIR.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(ACTIONS.open(newline="", encoding="utf-8")))
    out_rows = []

    # de-duplicate by URL to reduce fetch load
    fetched_by_url = {}

    for r in rows:
        aid = r.get("action_id", "")
        url = (r.get("anchor_url") or "").strip()
        ahash = (r.get("anchor_hash") or "").strip()

        if not url:
            out_rows.append({
                "action_id": aid,
                "anchor_url": "",
                "anchor_hash": ahash,
                "fetch_status": "missing_url",
                "http_status": "",
                "content_type": "",
                "file_path": "",
                "file_sha256": "",
                "content_bytes": "0",
                "fetched_at_utc": now_utc(),
                "error": "",
            })
            continue

        if url in fetched_by_url:
            cached = fetched_by_url[url].copy()
            cached["action_id"] = aid
            cached["anchor_hash"] = ahash
            out_rows.append(cached)
            continue

        ts = now_utc().replace(":", "").replace("-", "")
        fname = f"{slug(aid)}-{ts}.bin"
        rel_path = f"data/input/governance/anchors/{fname}"
        abs_path = ROOT / rel_path

        result = {
            "action_id": aid,
            "anchor_url": url,
            "anchor_hash": ahash,
            "fetch_status": "ok",
            "http_status": "",
            "content_type": "",
            "file_path": rel_path,
            "file_sha256": "",
            "content_bytes": "0",
            "fetched_at_utc": now_utc(),
            "error": "",
        }

        try:
            status, content, ctype, fetched_url = fetch_bytes(url)
            result["anchor_url"] = fetched_url
            result["http_status"] = str(status)
            result["content_type"] = ctype
            result["content_bytes"] = str(len(content))
            result["file_sha256"] = sha256_bytes(content)
            abs_path.write_bytes(content)
        except HTTPError as e:
            result["fetch_status"] = "http_error"
            result["http_status"] = str(e.code)
            result["error"] = str(e)
            result["file_path"] = ""
        except URLError as e:
            result["fetch_status"] = "url_error"
            result["error"] = str(e)
            result["file_path"] = ""
        except Exception as e:
            result["fetch_status"] = "error"
            result["error"] = str(e)
            result["file_path"] = ""

        fetched_by_url[url] = result.copy()
        out_rows.append(result)

    fieldnames = [
        "action_id", "anchor_url", "anchor_hash", "fetch_status", "http_status", "content_type",
        "file_path", "file_sha256", "content_bytes", "fetched_at_utc", "error"
    ]
    with INDEX_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    ok = sum(1 for x in out_rows if x["fetch_status"] == "ok")
    missing = sum(1 for x in out_rows if x["fetch_status"] == "missing_url")
    failed = len(out_rows) - ok - missing

    manifest = {
        "generated_at_utc": now_utc(),
        "source": str(ACTIONS.relative_to(ROOT)),
        "output_index": str(INDEX_CSV.relative_to(ROOT)),
        "anchors_dir": str(ANCHOR_DIR.relative_to(ROOT)),
        "stats": {
            "actions_total": len(rows),
            "fetched_ok": ok,
            "missing_url": missing,
            "failed": failed,
        },
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(manifest["stats"]))


if __name__ == "__main__":
    main()
