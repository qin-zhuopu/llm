#!/usr/bin/env python3
"""从 .md 文件提取结构化 YAML 数据。

工作流程：
  1. 读取 schema/model.schema.json 得到字段定义
  2. 读取指定的 .md 文件作为信息来源
  3. 构建动态 prompt（注入 schema + md 内容）
  4. 调用 LLM API 提取结构化数据
  5. 验证输出是否符合 schema
  6. 写入/覆盖对应的 .yaml 文件

用法:
    python3 scripts/extract_yaml.py domains/finance/bloomberggpt.md
    python3 scripts/extract_yaml.py --domain finance          # 批量处理某领域
    python3 scripts/extract_yaml.py --all                     # 全部处理
    python3 scripts/extract_yaml.py --dry-run domains/xxx.md  # 只输出 prompt 不调用 API
"""

import argparse
import json
import os
import sys
from pathlib import Path
from string import Template

import yaml

try:
    from jsonschema import validate, ValidationError
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False


# ============================================================
# Prompt 模板
# ============================================================

EXTRACTION_PROMPT = Template("""你是一个数据提取专家。请从下面的 Markdown 文档中提取结构化信息，输出为 YAML 格式。

## 目标 Schema

以下是 YAML 文件需要满足的 JSON Schema 定义。请严格按照字段类型、枚举值和约束填写：

### 必填字段 (Required)
${required_fields_doc}

### 可选字段 (Optional) — 如果 Markdown 中有相关信息就填，没有就省略
${optional_fields_doc}

## 上下文信息

- 文件将存放在 `domains/${domain}/` 目录下
- 因此 `domain` 字段的值必须是: `${domain}`

## 质量要求

1. `description`: 至少 50 个字符，用中文描述模型的核心定位和差异化，包含具体数据（参数量、训练数据规模、性能指标等）
2. `capabilities`: 至少 4 项，每项 5 字符以上，具体描述模型能做什么
3. `tags`: 3-6 个标签，用于搜索分类
4. `references`: 包含官网和论文链接（如果有）
5. 严格只输出 Schema 中定义的字段，不要输出任何额外字段（如 language、license、pipeline_tag 等）
6. `confidence`: 根据 Markdown 来源内容的可靠性综合判断，必须填写，规则如下：
   - `high`: md 内容来自官方产品页/论文/API 文档，有具体数据（参数量、benchmark 分数、训练细节、定价），信息可交叉验证
   - `medium`: md 内容来自新闻报道/第三方评测/公司官网但细节模糊，缺少可验证的技术指标
   - `low`: md 内容零散/过时/来源不明/无法确认模型是否仍在运营，或内容主要是营销文案无实质技术信息
注意：confidence 不要输出到 YAML 中，它是计算字段，会由独立脚本检查。但你仍需在提取时内部评估，用于决定其他字段的填写深度——低置信的信息宁可不填，也不要编造。

## 输入 Markdown

```markdown
${md_content}
```

## 输出格式示例

以下是一个正确格式的输出片段，注意 references 必须是对象数组（每项包含 title 和 url），字符串中含冒号(:)必须用引号包裹：

```
name: 模型名
company: 公司名
domain: ${domain}
status: released
description: "详细描述，至少50字符..."
capabilities:
  - 能力1
  - 能力2
  - 能力3
  - 能力4
references:
  - title: "论文标题: 含冒号必须引号包裹"
    url: "https://example.com/link"
```

## 输出要求

只输出纯 YAML 内容，不要包含 ```yaml``` 代码块标记，不要输出任何解释文字。
确保 YAML 语法正确：
- 所有包含冒号(:)、引号、特殊字符的字符串必须用双引号包裹
- URL 必须用双引号包裹
- description 必须用双引号包裹
严格只输出 Schema 中定义的字段，不要输出 language、license、pipeline_tag 等未定义字段。
""")


def build_field_doc(schema, field_names):
    """从 schema 中构建字段文档说明。"""
    props = schema.get("properties", {})
    lines = []
    for name in field_names:
        if name not in props:
            continue
        prop = props[name]
        desc = prop.get("description", "")
        field_type = prop.get("type", "")

        # 枚举值
        enum_vals = prop.get("enum", [])
        if not enum_vals and "items" in prop:
            enum_vals = prop["items"].get("enum", [])

        line = f"- `{name}` ({field_type}): {desc}"
        if enum_vals:
            if len(enum_vals) <= 10:
                line += f"\n  可选值: {enum_vals}"
            else:
                line += f"\n  可选值（部分）: {enum_vals[:10]}... 共 {len(enum_vals)} 个"

        # 特殊约束
        if "minLength" in prop:
            line += f"\n  最小长度: {prop['minLength']}"
        if "minItems" in prop:
            line += f"\n  最少条目: {prop['minItems']}"
        if "pattern" in prop:
            line += f"\n  格式: {prop['pattern']}"

        # 描述数组项结构（对象类型的items）
        if field_type == "array" and "items" in prop:
            items = prop["items"]
            if items.get("type") == "object" and "properties" in items:
                item_props = items["properties"]
                required_item_fields = items.get("required", [])
                line += f"\n  数组项结构 (对象，必填字段: {required_item_fields}):"
                for pname, pdef in item_props.items():
                    pdesc = pdef.get("description", "")
                    ptype = pdef.get("type", "")
                    line += f"\n    - `{pname}` ({ptype}): {pdesc}"

        lines.append(line)
    return "\n".join(lines)


def build_prompt(schema, md_content, domain):
    """构建完整的提取 prompt。

    注意：禁止任何形式的截断。当前最大 md 文件约 24K chars (~8K tokens)，
    模型上下文窗口 128K-500K tokens，完全不需要截断。
    """
    required = schema.get("required", [])
    all_props = list(schema.get("properties", {}).keys())
    optional = [f for f in all_props if f not in required]

    required_doc = build_field_doc(schema, required)
    optional_doc = build_field_doc(schema, optional)

    return EXTRACTION_PROMPT.substitute(
        required_fields_doc=required_doc,
        optional_fields_doc=optional_doc,
        domain=domain,
        md_content=md_content,  # 完整内容，禁止截断
    )


def call_llm(prompt, api_base=None, api_key=None, model=None, md_file_size=0):
    """调用 LLM API 获取结构化输出。

    支持 Anthropic 兼容 API (通过环境变量配置):
      ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, ANTHROPIC_MODEL

    日志输出：模型名、输入 token 数（chars/3 估算）、md 文件大小、输出 token 数
    """
    import requests

    base_url = api_base or os.environ.get("ANTHROPIC_BASE_URL", "https://open.bigmodel.cn/api/anthropic")
    api_key = api_key or os.environ.get("ANTHROPIC_AUTH_TOKEN", "")
    model = model or os.environ.get("ANTHROPIC_MODEL", "glm-4.5-air")

    if not api_key:
        print("❌ 未配置 API Key。请设置环境变量 ANTHROPIC_AUTH_TOKEN")
        sys.exit(1)

    # 日志：输入信息
    input_tokens_est = len(prompt) // 3
    print(f"    📊 模型: {model}")
    print(f"    📊 MD 文件大小: {md_file_size} chars")
    print(f"    📊 Prompt 大小: {len(prompt)} chars (~{input_tokens_est} tokens 估算)")

    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }

    payload = {
        "model": model,
        "max_tokens": 8192,
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    resp = requests.post(
        f"{base_url}/v1/messages",
        headers=headers,
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()

    # 日志：输出信息
    usage = data.get("usage", {})
    output_tokens = usage.get("output_tokens", 0)
    input_tokens_actual = usage.get("input_tokens", 0)
    print(f"    📊 实际输入 tokens: {input_tokens_actual}, 输出 tokens: {output_tokens}")

    # 提取文本
    content = data.get("content", [])
    if content and isinstance(content, list):
        return content[0].get("text", "")
    return ""


def parse_yaml_output(text):
    """解析 LLM 输出的 YAML 文本。"""
    # 去掉可能的代码块标记
    text = text.strip()
    if text.startswith("```yaml"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    try:
        return yaml.safe_load(text)
    except yaml.YAMLError:
        # 尝试修复常见问题：未引号包裹含冒号的字符串
        import re
        fixed_lines = []
        for line in text.split('\n'):
            # 修复 "- title: Some Title: With Colon" 类型的问题
            match = re.match(r'^(\s*-?\s*\w+:\s+)(.+)$', line)
            if match:
                prefix, value = match.groups()
                # 如果值包含冒号且未被引号包裹
                if ':' in value and not (value.startswith('"') or value.startswith("'")):
                    value = f'"{value}"'
                    line = prefix + value
            fixed_lines.append(line)
        fixed_text = '\n'.join(fixed_lines)
        return yaml.safe_load(fixed_text)


def validate_output(data, schema):
    """验证输出是否符合 schema。"""
    if not HAS_JSONSCHEMA:
        return True, "jsonschema 未安装，跳过验证"

    # 预处理：修复常见类型问题
    if isinstance(data, dict):
        # release_date 应为字符串
        if "release_date" in data and not isinstance(data["release_date"], str):
            data["release_date"] = str(data["release_date"])
        # parameters 应为字符串
        if "parameters" in data and not isinstance(data["parameters"], str):
            data["parameters"] = str(data["parameters"])

    try:
        validate(instance=data, schema=schema)
        return True, "通过"
    except ValidationError as e:
        return False, str(e.message)


def process_md(md_path, schema, root, dry_run=False):
    """处理单个 md 文件。"""
    md_path = Path(md_path)
    relative = md_path.relative_to(root)
    domain = md_path.parent.name
    yaml_path = md_path.with_suffix(".yaml")

    # 读取 md
    md_content = md_path.read_text(encoding="utf-8")

    if len(md_content.strip()) < 100:
        return "skip", f"{relative}: md 内容太短 ({len(md_content)} 字符)，无法提取"

    # 构建 prompt
    prompt = build_prompt(schema, md_content, domain)

    if dry_run:
        print(f"\n{'='*60}")
        print(f"文件: {relative}")
        print(f"Domain: {domain}")
        print(f"Prompt 长度: {len(prompt)} 字符")
        print(f"{'='*60}")
        print(prompt[:2000])
        print(f"\n... (截断，总 {len(prompt)} 字符)")
        return "dry-run", f"{relative}: prompt 已生成"

    # 调用 LLM
    try:
        raw_output = call_llm(prompt, md_file_size=len(md_content))
    except Exception as e:
        return "error", f"{relative}: API 调用失败: {e}"

    # 解析 YAML
    try:
        data = parse_yaml_output(raw_output)
    except yaml.YAMLError as e:
        return "error", f"{relative}: YAML 解析失败: {e}"

    if not data:
        return "error", f"{relative}: LLM 返回空内容"

    # 验证
    valid, msg = validate_output(data, schema)
    if not valid:
        return "error", f"{relative}: Schema 验证失败: {msg}"

    # 写入
    with open(yaml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    return "ok", f"{relative} → {yaml_path.name} ✅"


def main():
    parser = argparse.ArgumentParser(description="从 MD 文件提取结构化 YAML")
    parser.add_argument("files", nargs="*", help="要处理的 .md 文件路径")
    parser.add_argument("--domain", type=str, help="批量处理指定领域")
    parser.add_argument("--all", action="store_true", help="处理所有 .md 文件")
    parser.add_argument("--dry-run", action="store_true", help="只生成 prompt，不调用 API")
    parser.add_argument("--show-prompt", action="store_true", help="显示完整 prompt 模板")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    schema_path = root / "schema" / "model.schema.json"
    domains_path = root / "domains"

    # 加载 schema
    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    # 显示 prompt 模板
    if args.show_prompt:
        sample_prompt = build_prompt(schema, "（示例 MD 内容）", "finance")
        print(sample_prompt)
        sys.exit(0)

    # 收集要处理的文件
    md_files = []
    if args.all:
        md_files = sorted(domains_path.rglob("*.md"))
    elif args.domain:
        domain_dir = domains_path / args.domain
        if domain_dir.exists():
            md_files = sorted(domain_dir.glob("*.md"))
    elif args.files:
        md_files = [Path(f) if Path(f).is_absolute() else root / f for f in args.files]
    else:
        parser.print_help()
        sys.exit(0)

    if not md_files:
        print("❌ 未找到匹配的 .md 文件")
        sys.exit(1)

    print(f"📋 MD → YAML 结构化提取")
    print(f"   文件数: {len(md_files)}")
    print(f"   模式: {'dry-run (只生成prompt)' if args.dry_run else '调用 LLM 提取'}")
    print(f"{'='*60}")

    stats = {"ok": 0, "skip": 0, "error": 0, "dry-run": 0}
    for i, md_file in enumerate(md_files, 1):
        status, msg = process_md(md_file, schema, root, dry_run=args.dry_run)
        stats[status] += 1
        icon = {"ok": "✅", "skip": "⏭️", "error": "❌", "dry-run": "📝"}[status]
        print(f"  [{i}/{len(md_files)}] {icon} {msg}")

    print(f"\n{'='*60}")
    print(f"  结果: {stats['ok']} 成功, {stats['skip']} 跳过, {stats['error']} 失败")


if __name__ == "__main__":
    main()
