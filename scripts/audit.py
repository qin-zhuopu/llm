#!/usr/bin/env python3
"""审查所有模型 YAML 文件的字段完整度。

按照 schema/model.schema.json 定义的所有字段（必填+可选），
检查每个模型条目的信息覆盖情况，输出统计报告。
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

import yaml


def load_schema(schema_path: Path) -> dict:
    with open(schema_path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_all_fields(schema: dict) -> tuple[list[str], list[str]]:
    """从 schema 中提取必填字段和可选字段。"""
    required = schema.get("required", [])
    all_props = list(schema.get("properties", {}).keys())
    optional = [f for f in all_props if f not in required]
    return required, optional


def audit_file(filepath: Path, required_fields: list[str], optional_fields: list[str]) -> dict:
    """审查单个 YAML 文件，返回字段填写情况。"""
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if data is None:
        return {"error": "文件为空或无效 YAML", "present": [], "missing_required": required_fields, "missing_optional": optional_fields}

    present = [k for k in (required_fields + optional_fields) if k in data and data[k] is not None]
    missing_required = [k for k in required_fields if k not in data or data[k] is None]
    missing_optional = [k for k in optional_fields if k not in data or data[k] is None]

    return {
        "data": data,
        "present": present,
        "missing_required": missing_required,
        "missing_optional": missing_optional,
    }


def main():
    root = Path(__file__).resolve().parent.parent
    schema_path = root / "schema" / "model.schema.json"
    domains_path = root / "domains"

    schema = load_schema(schema_path)
    required_fields, optional_fields = get_all_fields(schema)
    all_fields = required_fields + optional_fields

    yaml_files = sorted(domains_path.rglob("*.yaml"))
    model_files = [f for f in yaml_files if f.name != "_meta.yaml"]

    if not model_files:
        print("❌ 未找到任何模型 YAML 文件")
        sys.exit(1)

    # --- 统计 ---
    total = len(model_files)
    field_coverage = defaultdict(int)  # 每个字段被多少文件填写了
    domain_stats = defaultdict(lambda: {"total": 0, "completeness": []})
    issues = []  # 有必填字段缺失的文件

    print("=" * 70)
    print(f"  模型数据完整度审查报告")
    print(f"  共 {total} 个模型文件, {len(required_fields)} 个必填字段, {len(optional_fields)} 个可选字段")
    print("=" * 70)

    for filepath in model_files:
        relative = filepath.relative_to(root)
        domain = filepath.parent.name
        result = audit_file(filepath, required_fields, optional_fields)

        domain_stats[domain]["total"] += 1

        if "error" in result:
            issues.append((str(relative), result["error"]))
            domain_stats[domain]["completeness"].append(0.0)
            continue

        # 统计字段覆盖
        for field in result["present"]:
            field_coverage[field] += 1

        # 计算完整度（包含可选字段）
        completeness = len(result["present"]) / len(all_fields) * 100
        domain_stats[domain]["completeness"].append(completeness)

        if result["missing_required"]:
            issues.append((str(relative), f"缺少必填字段: {', '.join(result['missing_required'])}"))

    # --- 输出：字段覆盖率 ---
    print("\n📊 字段覆盖率统计")
    print("-" * 70)
    print(f"  {'字段':<20} {'类型':<6} {'已填写':<8} {'覆盖率':<10} {'状态'}")
    print("-" * 70)

    for field in all_fields:
        field_type = "必填" if field in required_fields else "可选"
        count = field_coverage.get(field, 0)
        pct = count / total * 100
        if pct == 100:
            status = "✅"
        elif pct >= 50:
            status = "⚠️"
        elif pct > 0:
            status = "🔸"
        else:
            status = "❌ 无数据"
        print(f"  {field:<20} {field_type:<6} {count:>3}/{total:<4} {pct:>5.1f}%     {status}")

    # --- 输出：HF 对齐字段专项 ---
    hf_fields = ["language", "license", "license_name", "license_link", "pipeline_tag", "base_model", "datasets", "model_index", "co2_eq_emissions"]
    print("\n📋 HuggingFace 对齐字段覆盖情况")
    print("-" * 70)
    hf_filled = 0
    hf_total_possible = total * len(hf_fields)
    for field in hf_fields:
        count = field_coverage.get(field, 0)
        pct = count / total * 100
        hf_filled += count
        bar_len = int(pct / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {field:<20} {bar} {count:>3}/{total} ({pct:.0f}%)")

    hf_overall = hf_filled / hf_total_possible * 100 if hf_total_possible > 0 else 0
    print(f"\n  HF 字段总体覆盖率: {hf_filled}/{hf_total_possible} ({hf_overall:.1f}%)")

    # --- 输出：按领域统计 ---
    print("\n📁 按领域统计")
    print("-" * 70)
    print(f"  {'领域':<30} {'模型数':<6} {'平均完整度'}")
    print("-" * 70)
    for domain in sorted(domain_stats.keys()):
        stats = domain_stats[domain]
        avg = sum(stats["completeness"]) / len(stats["completeness"]) if stats["completeness"] else 0
        print(f"  {domain:<30} {stats['total']:<6} {avg:.1f}%")

    # --- 输出：问题汇总 ---
    if issues:
        print(f"\n⚠️  发现 {len(issues)} 个问题")
        print("-" * 70)
        for path, msg in issues:
            print(f"  {path}: {msg}")

    # --- 输出：建议优先填写的字段 ---
    print("\n💡 建议优先补充的字段（按价值排序）")
    print("-" * 70)
    priority_fields = [
        ("pipeline_tag", "让模型可按任务类型分类筛选"),
        ("language", "明确模型支持的语言"),
        ("license", "标注许可证类型（闭源→proprietary）"),
        ("base_model", "标注基座模型便于溯源对比"),
        ("datasets", "标注训练数据来源"),
        ("model_index", "添加 benchmark 评测数据"),
    ]
    for field, reason in priority_fields:
        count = field_coverage.get(field, 0)
        pct = count / total * 100
        if pct < 100:
            print(f"  {field:<20} 当前 {pct:.0f}% → {reason}")

    print("\n" + "=" * 70)
    overall_completeness = sum(
        len([f for f in all_fields if f in (yaml.safe_load(open(fp, encoding="utf-8")) or {})]) / len(all_fields) * 100
        for fp in model_files
    ) / total
    print(f"  📈 总体字段完整度: {overall_completeness:.1f}%")
    print("=" * 70)


if __name__ == "__main__":
    main()
