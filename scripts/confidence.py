#!/usr/bin/env python3
"""计算每个模型的数据置信度（基于 md 文件内容分析）。

置信度规则：
  high:   md 内容来自官方产品页/论文/API 文档，有具体数据，可交叉验证
  medium: md 来自新闻报道/第三方评测，细节模糊
  low:    信息零散/过时/来源不明/营销文案

计算方法（基于 md 内容的客观指标）：
  - 内容长度
  - 是否有具体数字（参数量、日期、金额、百分比）
  - 是否有论文/arxiv 链接
  - 是否有官方产品页 URL（非公司首页）
  - 是否有 benchmark 数据
  - 来源标注是否为一手来源

用法:
    python3 scripts/confidence.py                # 全部检查
    python3 scripts/confidence.py --domain finance
    python3 scripts/confidence.py --only high    # 只显示高置信
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


# --- 评分规则 ---

def compute_confidence(md_path, yaml_path):
    """计算单个模型的置信度，返回 (score, level, reasons)。"""
    score = 0
    reasons = []

    # 读取 md
    if not md_path.exists():
        return 0, "low", ["md 文件不存在"]

    md_content = md_path.read_text(encoding="utf-8")

    # 去掉 header（只以第一个 ---\n 为分隔）
    first_sep = md_content.find("---\n")
    if first_sep >= 0:
        body = md_content[first_sep + 4:].strip()
    else:
        body = md_content.strip()

    # 1. 内容长度 (max 20 分)
    # 使用字节长度，因为中文字符信息密度高于 ASCII
    length = len(body.encode("utf-8"))
    if length >= 2500:
        score += 20
        reasons.append(f"内容丰富 ({length} 字节)")
    elif length >= 800:
        score += 12
        reasons.append(f"内容适中 ({length} 字节)")
    elif length >= 300:
        score += 6
        reasons.append(f"内容偏短 ({length} 字节)")
    else:
        reasons.append(f"内容过短 ({length} 字节)")

    # 2. 具体数字（参数量、token数、百分比等）(max 20 分)
    number_patterns = [
        r'\d+[BMT]\+?',              # 7B, 20M+, 130T
        r'\d+\.?\d*%',               # 27%, 3.14%, 55%
        r'\$[\d,.]+[MBK]?\+?',       # $1.5M, $300K+
        r'\d{1,3}(?:,\d{3})+\+?',   # 9,400, 85,000+
        r'\d+[万亿千百]+\+?',         # 2000万, 300亿
        r'\d+[KMB]?\+',             # 300+, 85K+, 20M+
        r'\d+(?:\.\d+)?倍',          # 1.5倍, 30倍
    ]
    numbers = re.findall('|'.join(number_patterns), body)
    if len(numbers) >= 5:
        score += 20
        reasons.append(f"含大量具体数据 ({len(numbers)} 处)")
    elif len(numbers) >= 2:
        score += 10
        reasons.append(f"含部分数据 ({len(numbers)} 处)")
    else:
        reasons.append("缺少具体数字")

    # 3. 论文/arxiv 链接 (max 15 分)
    arxiv_count = len(re.findall(r'arxiv\.org|arXiv|论文|paper', body, re.IGNORECASE))
    if arxiv_count >= 1:
        score += 15
        reasons.append("有论文引用")

    # 4. 官方产品页 URL（非纯首页）(max 15 分)
    urls = re.findall(r'https?://[^\s\)]+', body)
    product_urls = [u for u in urls if any(k in u.lower() for k in ['product', 'platform', 'docs', 'api', 'blog', 'press', 'solution'])]
    if product_urls:
        score += 15
        reasons.append(f"有产品/文档链接 ({len(product_urls)} 处)")
    elif urls:
        score += 5
        reasons.append("有链接但非产品页")

    # 5. Benchmark / 评测数据 (max 15 分)
    benchmark_patterns = r'accuracy|F1|BLEU|benchmark|评测|得分|score|%.*vs|leaderboard'
    benchmarks = re.findall(benchmark_patterns, body, re.IGNORECASE)
    if benchmarks:
        score += 15
        reasons.append(f"有评测数据 ({len(benchmarks)} 处)")

    # 6. 来源可信度 (max 15 分)
    # 检查 md header 里的来源 URL
    source_match = re.search(r'来源:\s*\[([^\]]+)\]', md_content)
    if source_match:
        source_url = source_match.group(1)
        # 新闻/聚合网站列表（非官方来源）
        news_sites = [
            'techcrunch', 'reuters', '36kr', 'venturebeat', 'theverge',
            'wired', 'zdnet', 'cnet', 'engadget', 'thenextweb',
            'technode', 'pandaily', 'jiqizhixin', 'leiphone',
            'bloomberg.com/news', 'cnbc', 'fortune', 'forbes',
        ]
        if any(k in source_url.lower() for k in news_sites):
            score += 8
            reasons.append("来源为第三方")
        else:
            # 非新闻网站视为官方来源（公司官网、.ai、.io、.health 等）
            score += 15
            reasons.append("来源为官方/学术")
    else:
        reasons.append("未标注来源")

    # 读取 yaml 补充判断
    if yaml_path.exists():
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        if data:
            # 有 training 或 benchmarks 字段说明信息充实
            if data.get("training") or data.get("benchmarks"):
                score += 5
                reasons.append("YAML 含训练/评测结构化数据")

    # 总分 → 等级
    if score >= 60:
        level = "high"
    elif score >= 30:
        level = "medium"
    else:
        level = "low"

    return score, level, reasons


def main():
    parser = argparse.ArgumentParser(description="计算模型数据置信度")
    parser.add_argument("--domain", type=str, help="只检查指定领域")
    parser.add_argument("--only", type=str, choices=["high", "medium", "low"], help="只显示指定等级")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    domains_path = root / "domains"

    yaml_files = sorted(domains_path.rglob("*.yaml"))
    model_files = [f for f in yaml_files if f.name != "_meta.yaml"]

    if args.domain:
        model_files = [f for f in model_files if f.parent.name == args.domain]

    results = {"high": [], "medium": [], "low": []}

    for yaml_path in model_files:
        md_path = yaml_path.with_suffix(".md")
        relative = yaml_path.relative_to(root)
        score, level, reasons = compute_confidence(md_path, yaml_path)
        results[level].append((str(relative), score, reasons))

    # 输出
    if args.only:
        levels = [args.only]
    else:
        levels = ["high", "medium", "low"]

    print("=" * 70)
    print("  模型数据置信度报告")
    total = sum(len(v) for v in results.values())
    print(f"  共 {total} 个模型: {len(results['high'])} high, {len(results['medium'])} medium, {len(results['low'])} low")
    print("=" * 70)

    for level in levels:
        items = sorted(results[level], key=lambda x: -x[1])
        icon = {"high": "🟢", "medium": "🟡", "low": "🔴"}[level]
        print(f"\n{icon} {level.upper()} ({len(items)} 个)")
        print("-" * 70)
        for path, score, reasons in items:
            print(f"  [{score:>3}] {path}")
            if level != "high" or "--verbose" in sys.argv:
                for r in reasons:
                    print(f"        · {r}")

    print()


if __name__ == "__main__":
    main()
