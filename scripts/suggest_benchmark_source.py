#!/usr/bin/env python3
"""扫描所有模型 YAML 的 benchmark，建议 source 标注（只读，不修改文件）。

用途：辅助 AGENTS.md 方法论自检 #2（区分公司自报 vs 第三方验证数据）。
本脚本只输出建议，实际的 source 标注必须由当前会话 Agent 结合 raw 资料人工确认后写入。

推断规则（启发式，仅供参考）：
  - comparison/name 含 arxiv/论文/paper/Nature/Science → paper
  - 含 HackerOne/排行榜/leaderboard/榜首 → leaderboard
  - 含 护士评估/医师评估/自报/公司/内部评测/端到端对话评估 → self-reported
  - 含 第三方/独立评测/盲测 → third-party
  - 其他 → unknown（需人工判断）

用法:
    python scripts/suggest_benchmark_source.py                # 全量扫描
    python scripts/suggest_benchmark_source.py --unmarked     # 只列未标注 source 的
    python scripts/suggest_benchmark_source.py --domain finance
"""

import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOMAINS = ROOT / "domains"

PAPER_RE = re.compile(r"arxiv|论文|paper|nature|science|icml|neurips|aaai|acl|同行评审", re.I)
LEADERBOARD_RE = re.compile(r"hackerone|排行榜|leaderboard|榜首|榜单|登顶|排名第", re.I)
SELF_RE = re.compile(r"护士评估|医师评估|自报|公司口径|内部评测|端到端对话评估|人类评估|用户评估|客户案例|dogfood", re.I)
THIRD_RE = re.compile(r"第三方|独立评测|盲测|independent|third.?party", re.I)


def suggest(name, comparison, metric):
    text = f"{name} {comparison} {metric}"
    if PAPER_RE.search(text):
        return "paper"
    if LEADERBOARD_RE.search(text):
        return "leaderboard"
    if THIRD_RE.search(text):
        return "third-party"
    if SELF_RE.search(text):
        return "self-reported"
    return "unknown"


def main():
    parser = argparse.ArgumentParser(description="扫描并建议 benchmark source 标注")
    parser.add_argument("--unmarked", action="store_true", help="只列未标注 source 的 benchmark")
    parser.add_argument("--domain", type=str, help="只扫描某领域")
    args = parser.parse_args()

    files = sorted(f for f in DOMAINS.rglob("*.yaml") if f.name != "_meta.yaml")
    if args.domain:
        files = [f for f in files if f.parent.name == args.domain]

    total_bench = 0
    marked = 0
    suggestions = {}

    for f in files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if not data:
            continue
        benches = data.get("benchmarks", [])
        for b in benches:
            total_bench += 1
            has_source = "source" in b
            if has_source:
                marked += 1
            if args.unmarked and has_source:
                continue
            sug = suggest(b.get("name", ""), b.get("comparison", ""), b.get("metric", ""))
            rel = str(f.relative_to(ROOT))
            suggestions.setdefault(rel, []).append(
                (b.get("name", "?"), "已标注:" + b["source"] if has_source else "建议:" + sug)
            )

    for rel, items in suggestions.items():
        print(f"\n{rel}")
        for name, sug in items:
            print(f"  [{sug}] {name}")

    print(f"\n{'='*60}")
    print(f"  总 benchmark 数: {total_bench}, 已标注 source: {marked}, 未标注: {total_bench - marked}")


if __name__ == "__main__":
    main()
