#!/usr/bin/env python3
"""Validate all platform YAML files against platforms/schema.json."""

import json
import sys
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError

ROOT = Path(__file__).resolve().parent.parent
PLATFORMS_DIR = ROOT / "platforms"
SCHEMA_FILE = PLATFORMS_DIR / "schema.json"


def main():
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
