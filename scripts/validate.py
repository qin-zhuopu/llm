#!/usr/bin/env python3
"""验证所有模型 YAML 文件是否符合 JSON Schema 定义。"""

import json
import sys
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError

def main():
    root = Path(__file__).resolve().parent.parent
    schema_path = root / "schema" / "model.schema.json"
    domains_path = root / "domains"

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    yaml_files = sorted(domains_path.rglob("*.yaml"))
    model_files = [f for f in yaml_files if f.name != "_meta.yaml"]

    if not model_files:
        print("❌ 未找到任何模型 YAML 文件")
        sys.exit(1)

    passed = 0
    failed = 0
    errors = []

    for filepath in model_files:
        relative = filepath.relative_to(root)
        domain_folder = filepath.parent.name

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)

            if data is None:
                raise ValueError("文件为空或无效 YAML")

            # JSON Schema 校验
            validate(instance=data, schema=schema)

            # 检查 domain 字段是否匹配所在文件夹名
            if data.get("domain") != domain_folder:
                raise ValueError(
                    f"domain 字段值 '{data.get('domain')}' 与文件夹名 '{domain_folder}' 不匹配"
                )

            passed += 1
            print(f"  ✅ {relative}")

        except (ValidationError, ValueError, yaml.YAMLError) as e:
            failed += 1
            error_msg = str(e.message) if isinstance(e, ValidationError) else str(e)
            errors.append((str(relative), error_msg))
            print(f"  ❌ {relative}")
            print(f"     错误: {error_msg}")

    print(f"\n结果: {passed} 通过, {failed} 失败, 共 {passed + failed} 个文件")

    if failed > 0:
        sys.exit(1)
    else:
        print("\n🎉 所有模型文件验证通过！")
        sys.exit(0)


if __name__ == "__main__":
    main()
