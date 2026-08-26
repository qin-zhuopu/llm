#!/usr/bin/env python3
"""统一数据质量检查：对每个模型计算综合质量分。

评分维度（满分 100）：
  - 基础完整性 (30分): 必填字段质量
  - 技术深度 (40分): 可选字段填写情况
  - 来源可靠性 (30分): md 文件质量

用法:
    python scripts/check.py                 # 全部检查
    python scripts/check.py --domain finance
    python scripts/check.py --top 10        # 最好的10个
    python scripts/check.py --bottom 10     # 最差的10个
    python scripts/check.py --details domains/finance/bloomberggpt.yaml
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent


def score_yaml(data, yaml_path):
    """对单个 YAML 文件打分，返回 (total_score, breakdown)。"""
    breakdown = {}

    # === 基础完整性 (30分) ===
    base_score = 0

    # description 质量 (0-10)
    desc = data.get("description", "")
    desc_len = len(desc)
    if desc_len >= 80:
        base_score += 10
    elif desc_len >= 50:
        base_score += 7
    elif desc_len >= 30:
        base_score += 4
    else:
        base_score += 1
    breakdown["description"] = f"{desc_len} chars"

    # capabilities 数量和质量 (0-10)
    caps = data.get("capabilities", [])
    cap_count = len(caps)
    avg_cap_len = sum(len(c) for c in caps) / max(cap_count, 1)
    if cap_count >= 5 and avg_cap_len >= 8:
        base_score += 10
    elif cap_count >= 4:
        base_score += 7
    elif cap_count >= 3:
        base_score += 4
    else:
        base_score += 1
    breakdown["capabilities"] = f"{cap_count} items, avg {avg_cap_len:.0f} chars"

    # references 质量 (0-10)
    refs = data.get("references", [])
    ref_count = len(refs)
    has_paper = any("arxiv" in r.get("url", "").lower() or "paper" in r.get("title", "").lower() for r in refs)
    has_official = any(data.get("website", "") and data["website"] in r.get("url", "") for r in refs)
    if ref_count >= 2 and has_paper:
        base_score += 10
    elif ref_count >= 2:
        base_score += 7
    elif ref_count >= 1:
        base_score += 4
    else:
        base_score += 0
    breakdown["references"] = f"{ref_count} links, paper={'Y' if has_paper else 'N'}"

    # === 技术深度 (40分) ===
    tech_score = 0

    # parameters (0-5)
    if data.get("parameters"):
        tech_score += 5
    # architecture (0-5)
    if data.get("architecture"):
        tech_score += 5
    # base_model (0-5)
    if data.get("base_model"):
        tech_score += 5
    # training (0-8)
    training = data.get("training")
    if training:
        stages = training.get("stages", [])
        if stages and len(stages) >= 2:
            tech_score += 8
        elif stages:
            tech_score += 5
        else:
            tech_score += 2
    # tech_stack (0-5)
    if data.get("tech_stack"):
        ts = data["tech_stack"]
        if ts.get("framework") and ts.get("techniques"):
            tech_score += 5
        else:
            tech_score += 2
    # datasets (0-7)
    datasets = data.get("datasets", [])
    if datasets and len(datasets) >= 2:
        tech_score += 7
    elif datasets:
        tech_score += 4
    # benchmarks (0-5)
    benchmarks = data.get("benchmarks", [])
    if benchmarks and len(benchmarks) >= 2:
        tech_score += 5
    elif benchmarks:
        tech_score += 3

    filled_optional = sum(1 for k in ["parameters", "architecture", "base_model", "training", "tech_stack", "datasets", "benchmarks", "api"]
                         if data.get(k))
    breakdown["tech_fields"] = f"{filled_optional}/8 filled"

    # === 来源可靠性 (30分) ===
    source_score = 0
    md_path = yaml_path.with_suffix(".md")

    if md_path.exists():
        md_content = md_path.read_text(encoding="utf-8")
        # 去 header
        if "---\n" in md_content:
            body = md_content[md_content.find("---\n") + 4:].strip()
        else:
            body = md_content.strip()

        body_bytes = len(body.encode("utf-8"))

        # 内容长度 (0-10)
        if body_bytes >= 3000:
            source_score += 10
        elif body_bytes >= 1500:
            source_score += 7
        elif body_bytes >= 500:
            source_score += 4
        else:
            source_score += 1

        # 具体数据 (0-10)
        numbers = re.findall(r'\d+[BMT]\b|\d+%|\d+\+|\$[\d,.]+|\d+万|\d+亿|\d+倍|\d+x', body)
        if len(numbers) >= 5:
            source_score += 10
        elif len(numbers) >= 2:
            source_score += 6
        elif len(numbers) >= 1:
            source_score += 3

        # 来源可信度 (0-10)
        source_match = re.search(r'来源:\s*\[([^\]]+)\]', md_content)
        has_arxiv = bool(re.search(r'arxiv|论文|paper', body, re.IGNORECASE))
        has_product_url = bool(re.search(r'docs|api|product|platform|blog', body, re.IGNORECASE))

        if has_arxiv:
            source_score += 10
        elif has_product_url:
            source_score += 7
        elif source_match:
            source_score += 4

        breakdown["md"] = f"{body_bytes}B, {len(numbers)} numbers"
    else:
        breakdown["md"] = "MISSING"

    total = base_score + tech_score + source_score
    breakdown["_scores"] = f"base={base_score}/30 tech={tech_score}/40 source={source_score}/30"

    return total, breakdown


def main():
    parser = argparse.ArgumentParser(description="统一数据质量检查")
    parser.add_argument("--domain", type=str, help="只检查某个领域")
    parser.add_argument("--top", type=int, help="显示最好的 N 个")
    parser.add_argument("--bottom", type=int, help="显示最差的 N 个")
    parser.add_argument("--details", type=str, help="显示某个文件的详细得分")
    args = parser.parse_args()

    domains_dir = ROOT / "domains"
    yaml_files = sorted(domains_dir.rglob("*.yaml"))
    model_files = [f for f in yaml_files if f.name != "_meta.yaml"]

    if args.domain:
        model_files = [f for f in model_files if f.parent.name == args.domain]

    if args.details:
        target = ROOT / args.details
        if not target.exists():
            print(f"文件不存在: {args.details}")
            sys.exit(1)
        data = yaml.safe_load(target.read_text(encoding="utf-8"))
        score, breakdown = score_yaml(data, target)
        print(f"\n{'='*60}")
        print(f"  {data.get('name', '?')} — {score}/100")
        print(f"{'='*60}")
        for k, v in breakdown.items():
            print(f"  {k}: {v}")
        sys.exit(0)

    # 全量评分
    results = []
    for f in model_files:
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if not data:
            continue
        score, breakdown = score_yaml(data, f)
        results.append((str(f.relative_to(ROOT)), data.get("name", "?"), score, breakdown))

    results.sort(key=lambda x: -x[2])

    # 统计
    scores = [r[2] for r in results]
    avg = sum(scores) / len(scores) if scores else 0
    high = sum(1 for s in scores if s >= 60)
    medium = sum(1 for s in scores if 30 <= s < 60)
    low = sum(1 for s in scores if s < 30)

    print("=" * 70)
    print(f"  数据质量综合评分 — {len(results)} 个模型")
    print(f"  平均分: {avg:.1f}/100 | 高(≥60): {high} | 中(30-59): {medium} | 低(<30): {low}")
    print("=" * 70)

    # 显示列表
    if args.top:
        display = results[:args.top]
        print(f"\n🟢 TOP {args.top}:")
    elif args.bottom:
        display = results[-args.bottom:]
        print(f"\n🔴 BOTTOM {args.bottom}:")
    else:
        display = results
        print()

    for path, name, score, breakdown in display:
        bar_len = score // 5
        bar = "█" * bar_len + "░" * (20 - bar_len)
        scores_detail = breakdown.get("_scores", "")
        print(f"  {bar} {score:>3}/100  {name:<30} [{scores_detail}]")


if __name__ == "__main__":
    main()
