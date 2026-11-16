#!/usr/bin/env python3
"""抓取 Bambu Lab 中文 Wiki 全量页面并本地缓存（gzip）。"""
import gzip
import hashlib
import os
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests

BASE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(BASE, "cache")
UA = "Mozilla/5.0 (compatible; BambuWikiKB/1.0; +knowledge-base-builder)"
LOCK = threading.Lock()
DONE = 0
FAIL = []


def cache_path(url: str) -> str:
    h = hashlib.sha1(url.encode()).hexdigest()[:16]
    path = urlparse(url).path.strip("/").replace("/", "__")
    return os.path.join(CACHE, f"{path}__{h}.html.gz")


def fetch(session: requests.Session, url: str, attempt: int = 0) -> bool:
    cp = cache_path(url)
    if os.path.exists(cp) and os.path.getsize(cp) > 1000:
        return True
    try:
        r = session.get(url, timeout=30, headers={"User-Agent": UA})
        if r.status_code != 200:
            raise RuntimeError(f"HTTP {r.status_code}")
        with gzip.open(cp, "wb") as f:
            f.write(r.content)
        return True
    except Exception as e:
        if attempt < 2:
            time.sleep(1.5 * (attempt + 1))
            return fetch(session, url, attempt + 1)
        with LOCK:
            FAIL.append((url, str(e)[:120]))
        return False


def worker(urls):
    global DONE
    s = requests.Session()
    s.mount("https://", requests.adapters.HTTPAdapter(pool_maxsize=2))
    for u in urls:
        ok = fetch(s, u)
        with LOCK:
            DONE += 1
            if DONE % 200 == 0:
                print(f"[{DONE}/{TOTAL}] ok={DONE-len(FAIL)} fail={len(FAIL)}", flush=True)
        if not ok:
            time.sleep(0.5)


TOTAL = 0
if __name__ == "__main__":
    os.makedirs(CACHE, exist_ok=True)
    with open(os.path.join(BASE, "zh_urls.txt")) as f:
        urls = [ln.strip() for ln in f if ln.strip()]
    pending = [u for u in urls if not (os.path.exists(cache_path(u)) and os.path.getsize(cache_path(u)) > 1000)]
    TOTAL = len(urls)
    DONE = len(urls) - len(pending)
    print(f"total={len(urls)} cached={DONE} pending={len(pending)}", flush=True)
    chunks = [pending[i::8] for i in range(8)]
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(worker, c) for c in chunks if c]
        for f in as_completed(futs):
            f.result()
    print(f"FINISH ok={TOTAL-len(FAIL)} fail={len(FAIL)}", flush=True)
    with open(os.path.join(BASE, "crawl_fail.txt"), "w") as f:
        for u, e in FAIL:
            f.write(f"{u}\t{e}\n")
