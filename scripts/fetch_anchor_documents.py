#!/usr/bin/env python3
import csv
import hashlib
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
GOV = ROOT / "data" / "input" / "governance"
ACTIONS = GOV / "governance_actions_all.csv"
ANCHOR_DIR = GOV / "anchors"
INDEX_CSV = GOV / "anchor_documents_index.csv"
MANIFEST = GOV / "anchor_documents_manifest.json"
CACHE_INDEX = GOV / "anchor_cache_index.json"


def now_utc() -> str:
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
        "https://cloudflare-ipfs.com/ipfs/",
        "https://gateway.pinata.cloud/ipfs/",
        "https://w3s.link/ipfs/",
        "https://nftstorage.link/ipfs/",
    ]


def _fallback_mirrors() -> list[str]:
    """Optional secondary mirror list for non-ipfs anchors.

    Set ANCHOR_MIRRORS as comma-separated base URLs (e.g. internal cache service).
    Example: https://anchors.beacn.example/fetch?url=
    """
    env = os.environ.get("ANCHOR_MIRRORS", "").strip()
    if not env:
        return []
    vals = [x.strip() for x in env.split(",") if x.strip()]
    return vals


def _extract_ipfs_target(u: str) -> str | None:
    if not u:
        return None
    if u.startswith("ipfs://"):
        return u[len("ipfs://"):].lstrip("/")
    parsed = urlparse(u)
    m = re.search(r"/ipfs/([^?#]+)", parsed.path or "")
    if m:
        return m.group(1).lstrip("/")
    if parsed.netloc.endswith(".ipfs.dweb.link") and parsed.netloc:
        # cid in subdomain
        cid = parsed.netloc.split(".ipfs.dweb.link")[0]
        tail = (parsed.path or "").lstrip("/")
        return f"{cid}/{tail}" if tail else cid
    return None


def candidate_urls(url: str) -> list[str]:
    u = (url or "").strip()
    if not u:
        return []

    out: list[str] = []
    seen = set()

    # Direct URL first
    out.append(u)

    # IPFS expansion (works for ipfs:// and /ipfs/<cid> URLs)
    ipfs_target = _extract_ipfs_target(u)
    if ipfs_target:
        for g in _ipfs_gateway_prefixes():
            out.append(g + ipfs_target)

    # Optional mirror/adapters for brittle endpoints
    for m in _fallback_mirrors():
        out.append(m + u)

    for x in out:
        if x not in seen:
            seen.add(x)
            yield x


def request_profiles() -> list[dict]:
    # Rotate Accept headers for content-negotiation edge cases.
    return [
        {
            "User-Agent": "beacn-drep-resources/anchor-fetcher",
            "Accept": "application/json, text/plain;q=0.9, */*;q=0.8",
        },
        {
            "User-Agent": "beacn-drep-resources/anchor-fetcher",
            "Accept": "application/ld+json, application/json;q=0.9, */*;q=0.5",
        },
        {
            "User-Agent": "beacn-drep-resources/anchor-fetcher",
            "Accept": "text/html, application/xhtml+xml, application/json;q=0.8, */*;q=0.5",
        },
        {
            "User-Agent": "beacn-drep-resources/anchor-fetcher",
            "Accept": "*/*",
        },
    ]


def _load_cache() -> dict:
    if not CACHE_INDEX.exists():
        return {}
    try:
        data = json.loads(CACHE_INDEX.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save_cache(cache: dict) -> None:
    CACHE_INDEX.write_text(json.dumps(cache, indent=2) + "\n", encoding="utf-8")


def fetch_bytes(url: str, timeout: int = 20, retries: int = 2) -> tuple[int, bytes, str, str, str]:
    """Returns: http_status, bytes, content_type, fetched_url, profile_index"""
    last_err = None

    for cand in candidate_urls(url):
        for pidx, headers in enumerate(request_profiles()):
            attempt = 0
            while attempt <= retries:
                try:
                    req = Request(cand, headers=headers)
                    with urlopen(req, timeout=timeout) as resp:
                        status = int(getattr(resp, "status", 200))
                        ctype = resp.headers.get("Content-Type", "")
                        return status, resp.read(), ctype, cand, str(pidx)
                except HTTPError as e:
                    last_err = e
                    # Respect 429 backoff when given.
                    if e.code == 429 and attempt < retries:
                        ra = e.headers.get("Retry-After", "") if hasattr(e, "headers") else ""
                        wait_s = float(ra) if ra.isdigit() else 1.2
                        time.sleep(wait_s)
                        attempt += 1
                        continue
                    break
                except URLError as e:
                    last_err = e
                    break
                except Exception as e:
                    last_err = e
                    break

    if last_err:
        raise last_err
    raise URLError("no candidate URLs")


def _cache_key(source_url: str, anchor_hash: str) -> str:
    return sha256_bytes(f"{source_url}|{anchor_hash}".encode("utf-8"))


def main():
    if not ACTIONS.exists():
        raise SystemExit(f"missing actions csv: {ACTIONS}")

    ANCHOR_DIR.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(ACTIONS.open(newline="", encoding="utf-8")))
    out_rows = []

    # de-duplicate by URL to reduce fetch load
    fetched_by_url = {}
    cache = _load_cache()

    for r in rows:
        aid = r.get("action_id", "")
        source_url = (r.get("anchor_url") or "").strip()
        ahash = (r.get("anchor_hash") or "").strip()

        if not source_url:
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
                "source_url": "",
                "request_profile": "",
            })
            continue

        if source_url in fetched_by_url:
            cached = fetched_by_url[source_url].copy()
            cached["action_id"] = aid
            cached["anchor_hash"] = ahash
            out_rows.append(cached)
            continue

        cache_key = _cache_key(source_url, ahash)
        cache_row = cache.get(cache_key) if isinstance(cache, dict) else None
        if cache_row and (ROOT / cache_row.get("file_path", "")).exists():
            reused = {
                "action_id": aid,
                "anchor_url": cache_row.get("anchor_url", source_url),
                "anchor_hash": ahash,
                "fetch_status": "ok_cached",
                "http_status": cache_row.get("http_status", ""),
                "content_type": cache_row.get("content_type", ""),
                "file_path": cache_row.get("file_path", ""),
                "file_sha256": cache_row.get("file_sha256", ""),
                "content_bytes": str(cache_row.get("content_bytes", "0")),
                "fetched_at_utc": now_utc(),
                "error": "",
                "source_url": source_url,
                "request_profile": cache_row.get("request_profile", "cache"),
            }
            fetched_by_url[source_url] = reused.copy()
            out_rows.append(reused)
            continue

        ts = now_utc().replace(":", "").replace("-", "")
        fname = f"{slug(aid)}-{ts}.bin"
        rel_path = f"data/input/governance/anchors/{fname}"
        abs_path = ROOT / rel_path

        result = {
            "action_id": aid,
            "anchor_url": source_url,
            "anchor_hash": ahash,
            "fetch_status": "ok",
            "http_status": "",
            "content_type": "",
            "file_path": rel_path,
            "file_sha256": "",
            "content_bytes": "0",
            "fetched_at_utc": now_utc(),
            "error": "",
            "source_url": source_url,
            "request_profile": "",
        }

        try:
            status, content, ctype, fetched_url, pidx = fetch_bytes(source_url)
            result["anchor_url"] = fetched_url
            result["http_status"] = str(status)
            result["content_type"] = ctype
            result["content_bytes"] = str(len(content))
            result["file_sha256"] = sha256_bytes(content)
            result["request_profile"] = pidx
            abs_path.write_bytes(content)

            cache[cache_key] = {
                "anchor_url": fetched_url,
                "http_status": str(status),
                "content_type": ctype,
                "file_path": rel_path,
                "file_sha256": result["file_sha256"],
                "content_bytes": result["content_bytes"],
                "request_profile": pidx,
                "cached_at_utc": now_utc(),
                "source_url": source_url,
                "anchor_hash": ahash,
            }
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

        fetched_by_url[source_url] = result.copy()
        out_rows.append(result)

    fieldnames = [
        "action_id", "anchor_url", "anchor_hash", "fetch_status", "http_status", "content_type",
        "file_path", "file_sha256", "content_bytes", "fetched_at_utc", "error", "source_url", "request_profile"
    ]
    with INDEX_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    _save_cache(cache)

    ok = sum(1 for x in out_rows if x["fetch_status"] in ("ok", "ok_cached"))
    ok_cached = sum(1 for x in out_rows if x["fetch_status"] == "ok_cached")
    missing = sum(1 for x in out_rows if x["fetch_status"] == "missing_url")
    failed = len(out_rows) - ok - missing

    manifest = {
        "generated_at_utc": now_utc(),
        "source": str(ACTIONS.relative_to(ROOT)),
        "output_index": str(INDEX_CSV.relative_to(ROOT)),
        "anchors_dir": str(ANCHOR_DIR.relative_to(ROOT)),
        "cache_index": str(CACHE_INDEX.relative_to(ROOT)),
        "config": {
            "ipfs_gateways": _ipfs_gateway_prefixes(),
            "anchor_mirrors": _fallback_mirrors(),
            "request_profiles": len(request_profiles()),
        },
        "stats": {
            "actions_total": len(rows),
            "fetched_ok": ok,
            "fetched_ok_cached": ok_cached,
            "missing_url": missing,
            "failed": failed,
        },
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(manifest["stats"]))


if __name__ == "__main__":
    main()
