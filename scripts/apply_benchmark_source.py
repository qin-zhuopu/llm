#!/usr/bin/env python3
"""为所有未标注的 benchmark 应用 source 标注（基于规则 + sources.json）。

决策规则（保守：默认 self-reported，因为报告核心结论是垂类AI指标绝大多数为公司自报口径）：
  1. benchmark 文本(name+comparison+metric) 含论文关键词 → paper
  2. 含排行榜关键词 → leaderboard
  3. 含独立/第三方/实验验证关键词 → third-party
  4. 否则:
     - 若该模型有 arxiv 来源(真论文) 且 benchmark 描述定量 → paper
     - 其余 → self-reported (有 github README 不作为 paper 依据)

只处理未标注 source 的 benchmark，不覆盖已人工标注的。
处理后打印每个文件的标注结果供审核。

用法:
    python scripts/apply_benchmark_source.py --dry-run   # 预览
    python scripts/apply_benchmark_source.py             # 实际写入
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"
RAW = ROOT / "data" / "raw"

PAPER_RE = re.compile(r"arxiv|论文|paper|nature|science|icml|neurips|aaai|\bacl\b|同行评审|技术报告", re.I)
LEADERBOARD_RE = re.compile(r"hackerone|排行榜|leaderboard|榜首|榜单|登顶|排名第|matbench|榜单第", re.I)
THIRD_RE = re.compile(r"第三方|独立评测|独立实验|盲测|独立实验室|合成验证|independent|third.?party|外部验证", re.I)


def load_source_types(slug):
    """读取某模型 sources.json 的来源类型分布。"""
    sj = RAW / slug / "sources.json"
    if not sj.exists():
        return Counter()
    try:
        data = json.loads(sj.read_text(encoding="utf-8"))
    except Exception:
        return Counter()
    return Counter(f.get("type", "unknown") for f in data.get("files", []))


def decide(name, comparison, metric, source_types):
    text = f"{name} {comparison} {metric}"
    if PAPER_RE.search(text):
        return "paper"
    if LEADERBOARD_RE.search(text):
        return "leaderboard"
    if THIRD_RE.search(text):
        return "third-party"
    # 仅当该模型有 arxiv 来源（真正的论文，非 github README）时，
    # 定量学术指标才归 paper；否则保守归 self-reported。
    # 注：有 GitHub repo 不等于该 benchmark 经过同行评审，不作为 paper 依据。
    if source_types.get("arxiv", 0) > 0 and re.search(r"\d", str(comparison) + str(name)):
        return "paper"
    return "self-reported"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    files = sorted(f for f in DOMAINS.rglob("*.yaml") if f.name != "_meta.yaml")

    changed = 0
    stat = Counter()
    for f in files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if not data or not data.get("benchmarks"):
            continue
        slug = f.stem
        source_types = load_source_types(slug)
        file_changed = False
        results = []
        for b in data["benchmarks"]:
            if "source" in b:
                stat["already"] += 1
                continue
            src = decide(b.get("name", ""), b.get("comparison", ""), b.get("metric", ""), source_types)
            b["source"] = src
            stat[src] += 1
            file_changed = True
            changed += 1
            results.append((b.get("name", "?"), src))
        if file_changed:
            if args.dry_run:
                print(f"\n{f.relative_to(ROOT)}")
                for n, s in results:
                    print(f"  [{s}] {n}")
            else:
                f.write_text(
                    yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
                    encoding="utf-8",
                )

    print(f"\n{'='*60}")
    print(f"  {'预览' if args.dry_run else '已写入'}: {changed} 条新标注")
    print(f"  分布: {dict(stat)}")


if __name__ == "__main__":
    main()
