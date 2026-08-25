#!/usr/bin/env python3
"""检查模型数据质量（YAML 和 MD 文件）。

检查项：
  YAML:
    - description 长度是否过短（< 30 字符）
    - capabilities 条目数是否过少（< 3 个）
    - capabilities 单条是否过短（< 4 字符）
    - tags 是否为空
    - website URL 是否可疑（只是公司首页而非具体产品页）
    - release_date 是否只有年份（不够精确）
    - 新增 HF 字段是否已填写（language, license, pipeline_tag）

  MD:
    - 文件是否存在
    - 内容长度是否过短（< 500 字符，去掉 header）
    - 是否只有碎片内容（无实质信息）
"""

import sys
from pathlib import Path
from collections import defaultdict

import yaml


# --- 质量规则阈值 ---
MIN_DESCRIPTION_LEN = 30       # description 最小字符数
MIN_CAPABILITIES_COUNT = 3     # capabilities 最少条目数
MIN_CAPABILITY_ITEM_LEN = 4    # 单条 capability 最短字符数
MIN_MD_CONTENT_LEN = 500       # md 正文（去 header）最短字符数
GENERIC_URL_PATTERNS = [       # 可疑的"只是首页" URL 模式
    # 域名根路径
    lambda u: u.rstrip('/').count('/') <= 2 and not any(k in u for k in ['product', 'platform', 'ai', 'solution', 'blog', 'model']),
]


class Issue:
    """一个质量问题。"""
    def __init__(self, file, field, severity, message):
        self.file = file        # 文件路径
        self.field = field      # 涉及字段
        self.severity = severity  # error / warning / info
        self.message = message

    def __str__(self):
        icon = {"error": "❌", "warning": "⚠️", "info": "💡"}[self.severity]
        return f"  {icon} [{self.severity.upper()}] {self.file} → {self.field}: {self.message}"


def check_yaml(filepath, root):
    """检查单个 YAML 文件的质量。"""
    issues = []
    relative = str(filepath.relative_to(root))

    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not data:
        issues.append(Issue(relative, "file", "error", "YAML 为空"))
        return issues

    # 1. description 长度
    desc = data.get("description", "")
    if len(desc) < MIN_DESCRIPTION_LEN:
        issues.append(Issue(relative, "description", "error", f"过短（{len(desc)} 字符，最少 {MIN_DESCRIPTION_LEN}）"))
    elif len(desc) < 50:
        issues.append(Issue(relative, "description", "warning", f"较短（{len(desc)} 字符），建议补充更多细节"))

    # 2. capabilities 数量和质量
    caps = data.get("capabilities", [])
    if len(caps) < MIN_CAPABILITIES_COUNT:
        issues.append(Issue(relative, "capabilities", "warning", f"仅 {len(caps)} 项，建议至少 {MIN_CAPABILITIES_COUNT} 项"))
    short_caps = [c for c in caps if len(c) < MIN_CAPABILITY_ITEM_LEN]
    if short_caps:
        issues.append(Issue(relative, "capabilities", "warning", f"{len(short_caps)} 项过短: {short_caps}"))

    # 3. tags 检查
    tags = data.get("tags", [])
    if not tags:
        issues.append(Issue(relative, "tags", "info", "无标签"))

    # 4. release_date 精度
    rd = data.get("release_date", "")
    if rd and len(rd) == 4:
        issues.append(Issue(relative, "release_date", "info", f"只有年份 '{rd}'，建议精确到月"))

    # 5. website 是否太泛
    website = data.get("website", "")
    if website:
        clean = website.rstrip("/")
        # 检查是不是纯根域名（如 https://www.bloomberg.com）
        parts = clean.replace("https://", "").replace("http://", "").split("/")
        if len(parts) == 1:
            issues.append(Issue(relative, "website", "info", f"URL 为公司首页而非产品页: {website}"))

    # 6. HF 字段缺失检查
    hf_priority = ["pipeline_tag", "language", "license"]
    for field in hf_priority:
        if field not in data or data[field] is None:
            issues.append(Issue(relative, field, "warning", "未填写"))

    # 7. parameters 字段
    if "parameters" not in data or not data.get("parameters"):
        issues.append(Issue(relative, "parameters", "info", "未标注参数量"))

    return issues


def check_md(yaml_path, root):
    """检查对应的 md 文件质量。"""
    issues = []
    md_path = yaml_path.with_suffix(".md")
    relative_yaml = str(yaml_path.relative_to(root))
    relative_md = str(md_path.relative_to(root))

    if not md_path.exists():
        issues.append(Issue(relative_yaml, "md_file", "error", "缺少 .md 描述文件"))
        return issues

    content = md_path.read_text(encoding="utf-8")

    # 去掉 header（--- 分隔符之后的内容）
    if "---\n" in content:
        body = content.split("---\n", 1)[-1].strip()
    else:
        body = content.strip()

    # 长度检查
    if len(body) < 100:
        issues.append(Issue(relative_md, "content", "error", f"内容几乎为空（{len(body)} 字符）"))
    elif len(body) < MIN_MD_CONTENT_LEN:
        issues.append(Issue(relative_md, "content", "warning", f"内容过短（{len(body)} 字符，建议 > {MIN_MD_CONTENT_LEN}）"))

    # 碎片检测：如果内容里大部分是链接/按钮文本
    lines = [l.strip() for l in body.split("\n") if l.strip()]
    if lines:
        link_lines = sum(1 for l in lines if l.startswith("[") or l.startswith("<") or "http" in l)
        if len(lines) > 0 and link_lines / len(lines) > 0.6:
            issues.append(Issue(relative_md, "content", "warning", "内容多为链接/碎片，缺少实质描述"))

    return issues


def main():
    root = Path(__file__).resolve().parent.parent
    domains_path = root / "domains"

    yaml_files = sorted(domains_path.rglob("*.yaml"))
    model_files = [f for f in yaml_files if f.name != "_meta.yaml"]

    if not model_files:
        print("❌ 未找到任何模型 YAML 文件")
        sys.exit(1)

    all_issues = []
    file_scores = {}  # 每个文件的质量分

    for filepath in model_files:
        yaml_issues = check_yaml(filepath, root)
        md_issues = check_md(filepath, root)
        file_issues = yaml_issues + md_issues
        all_issues.extend(file_issues)

        # 计算分数：满分 100，每个 error -20，warning -10，info -2
        score = 100
        for issue in file_issues:
            if issue.severity == "error":
                score -= 20
            elif issue.severity == "warning":
                score -= 10
            elif issue.severity == "info":
                score -= 2
        file_scores[str(filepath.relative_to(root))] = max(0, score)

    # --- 统计 ---
    errors = [i for i in all_issues if i.severity == "error"]
    warnings = [i for i in all_issues if i.severity == "warning"]
    infos = [i for i in all_issues if i.severity == "info"]

    print("=" * 70)
    print("  模型数据质量检查报告")
    print(f"  共 {len(model_files)} 个模型文件")
    print("=" * 70)

    # 按严重程度输出
    if errors:
        print(f"\n❌ 严重问题 ({len(errors)} 个) — 必须修复")
        print("-" * 70)
        for issue in errors:
            print(str(issue))

    if warnings:
        print(f"\n⚠️  警告 ({len(warnings)} 个) — 建议修复")
        print("-" * 70)
        for issue in warnings:
            print(str(issue))

    if infos:
        print(f"\n💡 建议 ({len(infos)} 个) — 可选优化")
        print("-" * 70)
        for issue in infos:
            print(str(issue))

    # 最差文件 TOP 10
    print(f"\n📉 质量最差的文件 (TOP 10)")
    print("-" * 70)
    sorted_scores = sorted(file_scores.items(), key=lambda x: x[1])
    for path, score in sorted_scores[:10]:
        bar_len = int(score / 5)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  {bar} {score:>3}/100  {path}")

    # 总体评分
    avg_score = sum(file_scores.values()) / len(file_scores) if file_scores else 0
    print(f"\n{'=' * 70}")
    print(f"  📊 总计: {len(errors)} 错误, {len(warnings)} 警告, {len(infos)} 建议")
    print(f"  📈 平均质量分: {avg_score:.1f}/100")
    print(f"{'=' * 70}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
