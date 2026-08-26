#!/usr/bin/env python3
"""数据新鲜度检查 — AGENTS.md 方法论自检 #6。

基于 data/raw/{slug}/sources.json 的 fetched_at 字段，识别过期的原始资料。
垂类 AI 公司的融资、估值、benchmark、客户数变化快，原始资料需定期刷新。

新鲜度分级（相对当前日期）：
  - fresh   : <= 90 天
  - aging   : 91-180 天
  - stale   : 181-365 天
  - expired : > 365 天

用法:
    python scripts/check_freshness.py                # 全量报告
    python scripts/check_freshness.py --stale        # 只列 stale + expired（需刷新）
    python scripts/check_freshness.py --days 180     # 自定义过期阈值
    python scripts/check_freshness.py --missing      # 只列缺 sources.json/fetched_at 的

刷新建议：对 stale/expired 的模型运行
    python scripts/backfill_raw.py --slug {slug}
（注：backfill_raw.py 默认跳过已存在的 raw 目录，刷新前需先删除旧目录或改造脚本支持 --force）
"""

import argparse
import json
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"


def parse_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def grade(age_days):
    if age_days is None:
        return "unknown"
    if age_days <= 90:
        return "fresh"
    if age_days <= 180:
        return "aging"
    if age_days <= 365:
        return "stale"
    return "expired"


def main():
    parser = argparse.ArgumentParser(description="数据新鲜度检查")
    parser.add_argument("--stale", action="store_true", help="只列 stale + expired")
    parser.add_argument("--missing", action="store_true", help="只列缺 sources.json/fetched_at")
    parser.add_argument("--days", type=int, help="自定义过期阈值（天），超过则标记需刷新")
    args = parser.parse_args()

    today = date.today()
    rows = []
    missing = []

    for slug_dir in sorted(RAW.iterdir()):
        if not slug_dir.is_dir():
            continue
        slug = slug_dir.name
        sj = slug_dir / "sources.json"
        if not sj.exists():
            missing.append((slug, "no sources.json"))
            continue
        try:
            data = json.loads(sj.read_text(encoding="utf-8"))
        except Exception:
            missing.append((slug, "invalid json"))
            continue

        dates = [parse_date(f.get("fetched_at")) for f in data.get("files", [])]
        dates = [d for d in dates if d]
        if not dates:
            missing.append((slug, "no fetched_at"))
            continue

        newest = max(dates)
        age = (today - newest).days
        rows.append((slug, newest.isoformat(), age, grade(age)))

    # 输出
    if args.missing:
        print("=== 缺 sources.json / fetched_at 的模型 ===")
        for slug, reason in missing:
            print(f"  ⚠️  {slug}: {reason}")
        print(f"\n  共 {len(missing)} 个")
        return

    rows.sort(key=lambda r: -r[2])  # 按 age 降序

    threshold = args.days
    print(f"{'模型':<32} {'最新抓取':<12} {'天龄':>5}  新鲜度")
    print("-" * 62)
    stat = {}
    for slug, d, age, g in rows:
        stat[g] = stat.get(g, 0) + 1
        if args.stale and g not in ("stale", "expired"):
            continue
        if threshold and age <= threshold:
            continue
        icon = {"fresh": "🟢", "aging": "🟡", "stale": "🟠", "expired": "🔴"}.get(g, "⚪")
        print(f"{slug:<32} {d:<12} {age:>5}  {icon} {g}")

    print("-" * 62)
    print(f"  分布: {stat}")
    if missing:
        print(f"  另有 {len(missing)} 个缺 sources.json/fetched_at（用 --missing 查看）")


if __name__ == "__main__":
    main()
