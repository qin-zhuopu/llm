#!/usr/bin/env python3
"""回填原始资料脚本 — AGENTS.md 方法论阶段② 的脚本化落地。

把缺失的原始资料回填到 data/raw/{slug}/ 目录：
  1. 遍历 domains/ 下所有 {slug}.md
  2. 对缺 data/raw/{slug}/ 的模型，从 md 提取来源 URL
  3. 抓取每个 URL 原文，保存到 data/raw/{slug}/{name}.md
  4. 生成 sources.json（filename / url / fetched_at / type / fetch_status）

用法:
    python scripts/backfill_raw.py                 # 处理所有缺 raw 的模型
    python scripts/backfill_raw.py --slug bloomberggpt
    python scripts/backfill_raw.py --dry-run       # 只打印将抓取的 URL
    python scripts/backfill_raw.py --limit 10      # 最多处理 N 个模型

注意:
  - 单个 URL 失败不影响其他（记录 fetch_status: failed）
  - 不覆盖已存在的 data/raw/{slug}/ 目录
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    print("❌ 需要 requests 库: pip install requests")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
RAW = ROOT / "data" / "raw"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

URL_RE = re.compile(r"https?://[^\s\)\]\>\"']+")

# 噪音域名（隐私政策、条款、社交分享等），跳过不抓
# 完整域名匹配，避免子串误伤（如 x.com 匹配到 kebotix.com）
NOISE_HOSTS = (
    "policies.google.com",
    "twitter.com",
    "linkedin.com",
    "facebook.com",
    "youtube.com",
)
NOISE_PATHS = (
    "google.com/privacy",
    "google.com/terms",
)


def is_noise(url):
    host = urlparse(url).netloc.lower()
    if any(host == n or host == "www." + n for n in NOISE_HOSTS):
        return True
    if any(p in url.lower() for p in NOISE_PATHS):
        return True
    return False


def infer_type(url):
    """根据 URL 域名推断来源类型。"""
    host = urlparse(url).netloc.lower()
    if "arxiv.org" in host:
        return "arxiv"
    if "github.com" in host:
        return "github"
    if "huggingface.co" in host:
        return "huggingface"
    if any(n in host for n in ["techcrunch", "reuters", "36kr", "forbes", "bloomberg.com/news"]):
        return "news"
    return "official-website"


def slugify_url(url, idx):
    """从 URL 生成描述性文件名。"""
    host = urlparse(url).netloc.lower().replace("www.", "").split(":")[0]
    host_slug = re.sub(r"[^a-z0-9]+", "-", host).strip("-")
    t = infer_type(url)
    if t == "arxiv":
        m = re.search(r"(\d{4}\.\d{4,5})", url)
        return f"arxiv-{m.group(1)}.md" if m else f"arxiv-{idx}.md"
    if t == "github":
        return f"github-{host_slug}-{idx}.md"
    return f"{host_slug}-{idx}.md"


def extract_urls(md_text):
    """从 md 文本提取所有唯一 URL，保持出现顺序。"""
    urls = []
    seen = set()
    for m in URL_RE.finditer(md_text):
        url = m.group(0).rstrip(".,;")
        # 去掉 markdown 链接尾随的括号残留
        url = url.rstrip(")")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


# 单个抓取文件最大保存大小（字符）。超过则截断，避免抓到媒体/CDN 大文件撑爆仓库。
MAX_CONTENT_CHARS = 500_000  # ~500KB 文本，远超任何研究文档所需


def fetch(url, session, timeout=40, retries=3):
    """抓取 URL，返回 (text, status)。

    - 只接受 text/html、text/*、application/json 内容类型，跳过二进制/媒体。
    - 内容超过 MAX_CONTENT_CHARS 时截断，防止超大文件进入仓库。
    """
    for attempt in range(retries):
        try:
            r = session.get(url, timeout=timeout)
            ctype = r.headers.get("Content-Type", "").lower()
            if not any(t in ctype for t in ("text/", "application/json", "application/xml")):
                return None, f"failed (non-text content-type: {ctype})"
            if r.status_code == 200 and len(r.text) > 100:
                text = r.text
                if len(text) > MAX_CONTENT_CHARS:
                    text = text[:MAX_CONTENT_CHARS] + "\n\n[... 内容过长已截断，完整内容见原始 URL ...]"
                return text, "ok"
            else:
                last = f"status={r.status_code}, len={len(r.text)}"
        except Exception as e:
            last = repr(e)
    return None, f"failed ({last})"


def process_model(md_path, session, dry_run=False):
    """处理单个模型 md，回填 raw 资料。返回 (status, msg)。"""
    slug = md_path.stem
    raw_dir = RAW / slug

    if raw_dir.exists():
        return "skip", f"{slug}: data/raw/{slug}/ 已存在，跳过"

    md_text = md_path.read_text(encoding="utf-8")
    urls = extract_urls(md_text)

    # 过滤掉明显非资料性 URL（图片、schema）和噪音域名（隐私/条款/社交）
    urls = [
        u for u in urls
        if not u.endswith((".json", ".png", ".jpg", ".svg"))
        and not is_noise(u)
    ]

    if not urls:
        return "no-url", f"{slug}: md 中未找到来源 URL"

    if dry_run:
        lines = [f"{slug}: {len(urls)} 个 URL"]
        for u in urls:
            lines.append(f"    [{infer_type(u)}] {u}")
        return "dry-run", "\n".join(lines)

    raw_dir.mkdir(parents=True, exist_ok=True)
    today = date.today().isoformat()
    sources = []
    ok_count = 0

    for idx, url in enumerate(urls, 1):
        filename = slugify_url(url, idx)
        text, status = fetch(url, session)
        entry = {
            "filename": filename,
            "url": url,
            "fetched_at": today,
            "type": infer_type(url),
        }
        if status == "ok":
            (raw_dir / filename).write_text(
                f"# Source: {url}\n\n> 抓取日期: {today}\n\n---\n\n{text}",
                encoding="utf-8",
            )
            ok_count += 1
        else:
            entry["fetch_status"] = "failed"
        sources.append(entry)

    (raw_dir / "sources.json").write_text(
        json.dumps({"files": sources}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    return "ok", f"{slug}: {ok_count}/{len(urls)} URL 成功抓取"


def main():
    parser = argparse.ArgumentParser(description="回填原始资料到 data/raw/")
    parser.add_argument("--slug", type=str, help="只处理指定模型")
    parser.add_argument("--dry-run", action="store_true", help="只打印将抓取的 URL")
    parser.add_argument("--limit", type=int, help="最多处理 N 个模型")
    args = parser.parse_args()

    md_files = sorted(f for f in DOMAINS.rglob("*.md") if f.stem != "_meta")

    if args.slug:
        md_files = [f for f in md_files if f.stem == args.slug]
        if not md_files:
            print(f"❌ 未找到 slug={args.slug} 的 md 文件")
            sys.exit(1)

    # 只保留缺 raw 的
    todo = [f for f in md_files if not (RAW / f.stem).exists()]

    if args.limit:
        todo = todo[: args.limit]

    print(f"📋 回填原始资料")
    print(f"   缺 raw 的模型: {len(todo)}")
    print(f"   模式: {'dry-run' if args.dry_run else '实际抓取'}")
    print("=" * 60)

    session = requests.Session()
    session.headers.update(HEADERS)

    stats = {"ok": 0, "skip": 0, "no-url": 0, "dry-run": 0}
    for i, md in enumerate(todo, 1):
        status, msg = process_model(md, session, dry_run=args.dry_run)
        stats[status] = stats.get(status, 0) + 1
        icon = {"ok": "✅", "skip": "⏭️", "no-url": "⚠️", "dry-run": "📝"}.get(status, "•")
        print(f"  [{i}/{len(todo)}] {icon} {msg}")

    print("=" * 60)
    print(f"  结果: {dict(stats)}")


if __name__ == "__main__":
    main()
