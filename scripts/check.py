#!/usr/bin/env python3
"""统一数据质量检查：对每个模型按三个维度打分。

维度：
  - 业务 (B): 商业信息——公司、产品定位、客户、使用方式、官网
  - 技术 (T): 技术细节——参数量、架构、训练过程、数据集、benchmark
  - 来源 (S): 信息来源——md 文件质量、具体数据、论文/官方链接

每个维度满分 100，总分为三维度平均。

用法:
    python scripts/check.py                 # 全部检查
    python scripts/check.py --domain finance
    python scripts/check.py --top 10
    python scripts/check.py --bottom 10
    python scripts/check.py --details domains/finance/bloomberggpt.yaml
"""

import argparse
import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent


def score_business(data):
    """业务维度评分 (满分 100)。
    
    评估：公司信息、产品定位、客户/市场、使用方式、官网/参考链接
    """
    score = 0
    details = {}

    # description 质量——是否清晰传达产品定位 (0-25)
    desc = data.get("description", "")
    desc_len = len(desc)
    if desc_len >= 100:
        score += 25
    elif desc_len >= 60:
        score += 18
    elif desc_len >= 30:
        score += 10
    else:
        score += 3
    details["description"] = f"{desc_len} chars"

    # capabilities 是否具体说明能做什么 (0-25)
    caps = data.get("capabilities", [])
    cap_count = len(caps)
    avg_cap_len = sum(len(c) for c in caps) / max(cap_count, 1)
    if cap_count >= 5 and avg_cap_len >= 8:
        score += 25
    elif cap_count >= 4 and avg_cap_len >= 6:
        score += 18
    elif cap_count >= 3:
        score += 10
    else:
        score += 3
    details["capabilities"] = f"{cap_count} items"

    # access 方式是否明确 (0-15)
    access = data.get("access", [])
    if access and len(access) >= 1:
        score += 15
    details["access"] = str(access) if access else "missing"

    # website 是否有 (0-15)
    website = data.get("website", "")
    if website and "/" in website:
        score += 15
    details["website"] = "Y" if website else "N"

    # references 是否有多个来源 (0-20)
    refs = data.get("references", [])
    if len(refs) >= 3:
        score += 20
    elif len(refs) >= 2:
        score += 14
    elif len(refs) >= 1:
        score += 7
    details["references"] = f"{len(refs)} links"

    return score, details


def score_technical(data):
    """技术维度评分 (满分 100)。
    
    评估：参数量、架构、基座模型、训练过程、技术栈、数据集、评测
    """
    score = 0
    details = {}

    # parameters (0-15)
    if data.get("parameters"):
        score += 15
    details["parameters"] = data.get("parameters", "-")

    # architecture (0-10)
    if data.get("architecture"):
        score += 10
    details["architecture"] = data.get("architecture", "-")

    # base_model (0-10)
    if data.get("base_model"):
        score += 10
    details["base_model"] = "Y" if data.get("base_model") else "-"

    # training (0-25)
    training = data.get("training")
    if training:
        stages = training.get("stages", [])
        t_score = 5  # 有 training 对象就 5 分
        if stages:
            t_score += min(len(stages) * 5, 10)  # 每阶段 5 分，最多加 10
        if training.get("total_tokens"):
            t_score += 5
        if training.get("context_length"):
            t_score += 5
        score += min(t_score, 25)
    details["training"] = f"{len(training.get('stages', []))} stages" if training else "-"

    # tech_stack (0-10)
    ts = data.get("tech_stack")
    if ts:
        t_score = 0
        if ts.get("framework"):
            t_score += 4
        if ts.get("techniques"):
            t_score += min(len(ts["techniques"]) * 2, 6)
        score += min(t_score, 10)
    details["tech_stack"] = "Y" if ts else "-"

    # datasets (0-15)
    datasets = data.get("datasets", [])
    if datasets:
        d_score = min(len(datasets) * 5, 10)
        # 有 size 信息加分
        if any(d.get("size") for d in datasets):
            d_score += 5
        score += min(d_score, 15)
    details["datasets"] = f"{len(datasets)} sets" if datasets else "-"

    # benchmarks (0-15)
    benchmarks = data.get("benchmarks", [])
    if benchmarks:
        b_score = min(len(benchmarks) * 3, 10)
        # 有 comparison 加分
        if any(b.get("comparison") for b in benchmarks):
            b_score += 5
        score += min(b_score, 15)
    details["benchmarks"] = f"{len(benchmarks)} scores" if benchmarks else "-"

    return score, details


def score_source(data, yaml_path):
    """来源维度评分 (满分 100)。
    
    评估：md 文件是否存在/内容长度/具体数据/论文引用/官方来源
    """
    score = 0
    details = {}

    md_path = yaml_path.with_suffix(".md")
    if not md_path.exists():
        details["md"] = "MISSING"
        return 0, details

    md_content = md_path.read_text(encoding="utf-8")
    # 去 header
    if "---\n" in md_content:
        body = md_content[md_content.find("---\n") + 4:].strip()
    else:
        body = md_content.strip()

    body_bytes = len(body.encode("utf-8"))

    # 内容长度 (0-30)
    if body_bytes >= 5000:
        score += 30
    elif body_bytes >= 3000:
        score += 22
    elif body_bytes >= 1500:
        score += 15
    elif body_bytes >= 500:
        score += 8
    else:
        score += 2
    details["content"] = f"{body_bytes}B"

    # 具体数据——数字、百分比、金额 (0-25)
    numbers = re.findall(
        r'\d+[BMT]\b|\d+%|\d+\+|\$[\d,.]+[MBK]?|\d+万|\d+亿|\d+倍|\d+x|\d{1,3}(?:,\d{3})+',
        body
    )
    if len(numbers) >= 8:
        score += 25
    elif len(numbers) >= 4:
        score += 18
    elif len(numbers) >= 2:
        score += 10
    elif len(numbers) >= 1:
        score += 5
    details["data_points"] = f"{len(numbers)}"

    # 论文/学术来源 (0-25)
    has_arxiv = bool(re.search(r'arxiv|arXiv|论文|paper|Nature|Science|ICML|NeurIPS|AAAI', body))
    if has_arxiv:
        score += 25
    details["paper"] = "Y" if has_arxiv else "N"

    # 官方/一手来源 vs 二手 (0-20)
    source_match = re.search(r'来源:\s*\[([^\]]+)\]', md_content)
    if source_match:
        source_url = source_match.group(1)
        # 新闻/聚合网站 = 二手
        news_sites = ["techcrunch", "reuters", "36kr", "bloomberg.com/news", "wired", "theverge"]
        is_news = any(s in source_url.lower() for s in news_sites)
        if not is_news:
            score += 20
            details["source"] = "official"
        else:
            score += 10
            details["source"] = "news"
    else:
        details["source"] = "unknown"

    return score, details


def check_model(yaml_path):
    """对单个模型做三维度评分。"""
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if not data:
        return None

    b_score, b_details = score_business(data)
    t_score, t_details = score_technical(data)
    s_score, s_details = score_source(data, yaml_path)

    total = round((b_score + t_score + s_score) / 3)

    return {
        "name": data.get("name", "?"),
        "domain": yaml_path.parent.name,
        "business": b_score,
        "technical": t_score,
        "source": s_score,
        "total": total,
        "b_details": b_details,
        "t_details": t_details,
        "s_details": s_details,
    }


def main():
    parser = argparse.ArgumentParser(description="三维度数据质量检查")
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
        result = check_model(target)
        if not result:
            print("YAML 为空")
            sys.exit(1)
        print(f"\n{'='*60}")
        print(f"  {result['name']} — B:{result['business']} T:{result['technical']} S:{result['source']} (avg {result['total']})")
        print(f"{'='*60}")
        print(f"\n  业务 ({result['business']}/100):")
        for k, v in result["b_details"].items():
            print(f"    {k}: {v}")
        print(f"\n  技术 ({result['technical']}/100):")
        for k, v in result["t_details"].items():
            print(f"    {k}: {v}")
        print(f"\n  来源 ({result['source']}/100):")
        for k, v in result["s_details"].items():
            print(f"    {k}: {v}")
        sys.exit(0)

    # 全量评分
    results = []
    for f in model_files:
        result = check_model(f)
        if result:
            results.append(result)

    results.sort(key=lambda x: -x["total"])

    # 统计
    totals = [r["total"] for r in results]
    avg = sum(totals) / len(totals) if totals else 0
    b_avg = sum(r["business"] for r in results) / len(results)
    t_avg = sum(r["technical"] for r in results) / len(results)
    s_avg = sum(r["source"] for r in results) / len(results)

    print("=" * 75)
    print(f"  数据质量三维度评分 — {len(results)} 个模型")
    print(f"  综合平均: {avg:.0f} | 业务均: {b_avg:.0f}/100 | 技术均: {t_avg:.0f}/100 | 来源均: {s_avg:.0f}/100")
    print("=" * 75)

    # 显示列表
    if args.top:
        display = results[:args.top]
        label = f"TOP {args.top}"
    elif args.bottom:
        display = results[-args.bottom:]
        label = f"BOTTOM {args.bottom}"
    else:
        display = results
        label = "ALL"

    print(f"\n  {'模型':<28} {'B':>3} {'T':>3} {'S':>3} {'avg':>4}  {'领域'}")
    print(f"  {'-'*28} {'---':>3} {'---':>3} {'---':>3} {'----':>4}  {'-'*15}")
    for r in display:
        print(f"  {r['name']:<28} {r['business']:>3} {r['technical']:>3} {r['source']:>3} {r['total']:>4}  {r['domain']}")


if __name__ == "__main__":
    main()
