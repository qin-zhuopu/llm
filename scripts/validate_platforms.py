#!/usr/bin/env python3
"""验证所有平台 YAML 文件是否符合 platforms/schema.json。

遍历 platforms/*.yaml，对每个文件做 JSON Schema 校验（inference_api 为必填）。
全部通过退出码 0，任一失败退出码 1。

用法:
    python scripts/validate_platforms.py     # 校验所有平台 YAML
    python scripts/validate_platforms.py -h  # 显示本帮助
"""

import argparse
import json
import sys
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parent.parent
PLATFORMS_DIR = ROOT / "platforms"
SCHEMA_FILE = PLATFORMS_DIR / "schema.json"


def main():
    argparse.ArgumentParser(
        description="验证所有平台 YAML 文件是否符合 platforms/schema.json。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    ).parse_args()

    if not SCHEMA_FILE.exists():
        print(f"ERROR: Schema file not found: {SCHEMA_FILE}")
        sys.exit(1)

    with open(SCHEMA_FILE) as f:
        schema = json.load(f)

    yaml_files = sorted(PLATFORMS_DIR.glob("*.yaml"))
    # Exclude _meta.yaml
    yaml_files = [f for f in yaml_files if f.name != "_meta.yaml"]

    if not yaml_files:
        print("No platform YAML files found.")
        sys.exit(0)

    passed = 0
    failed = 0
    errors = []

    for yaml_file in yaml_files:
        try:
            with open(yaml_file) as f:
                data = yaml.safe_load(f)
            validate(instance=data, schema=schema)
            print(f"  PASS: {yaml_file.name}")
            passed += 1
        except ValidationError as e:
            print(f"  FAIL: {yaml_file.name} - {e.message}")
            failed += 1
            errors.append((yaml_file.name, e.message))
        except Exception as e:
            print(f"  ERROR: {yaml_file.name} - {e}")
            failed += 1
            errors.append((yaml_file.name, str(e)))

    print(f"\nResults: {passed} pass, {failed} fail (total: {passed + failed})")

    if errors:
        print("\nErrors:")
        for name, msg in errors:
            print(f"  - {name}: {msg}")
        sys.exit(1)


if __name__ == "__main__":
    main()
