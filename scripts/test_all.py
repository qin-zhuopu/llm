#!/usr/bin/env python3
"""集成测试：验证所有脚本能正常运行且输出合理。

用法:
    python scripts/test_all.py

检查项:
    1. validate.py — 所有 YAML 通过 schema 校验
    2. check.py — 能跑通，评分在合理范围
    3. build_kg.py — 图构建成功，节点数 > 0
    4. validate_platforms.py — 平台文件通过校验
    5. 脚本与 schema 一致性 — 脚本引用的字段在 schema 中存在
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PASS = 0
FAIL = 0


def run_script(name, args=None):
    """运行脚本并返回 (returncode, stdout, stderr)。"""
    cmd = [sys.executable, str(ROOT / "scripts" / name)]
    if args:
        cmd.extend(args)
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    return result.returncode, result.stdout, result.stderr


def test(name, condition, msg=""):
    """记录测试结果。"""
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"  ✅ {name}")
    else:
        FAIL += 1
        print(f"  ❌ {name}: {msg}")


def test_validate():
    """测试 validate.py。"""
    print("\n📋 validate.py")
    code, stdout, stderr = run_script("validate.py")
    test("退出码为 0", code == 0, f"exit={code}")
    test("有通过记录", "通过" in stdout, "未找到'通过'")
    test("无失败", "0 失败" in stdout, stdout.split("\n")[-3] if stdout else "")


def test_check():
    """测试 check.py。"""
    print("\n📋 check.py")
    code, stdout, stderr = run_script("check.py")
    test("退出码为 0", code == 0, f"exit={code}, stderr={stderr[:200]}")
    test("有评分输出", "模型" in stdout and "/100" in stdout[:500], "无评分输出")

    # --top 和 --bottom 也能跑
    code2, _, _ = run_script("check.py", ["--top", "5"])
    test("--top 能跑", code2 == 0, f"exit={code2}")

    code3, _, _ = run_script("check.py", ["--bottom", "5"])
    test("--bottom 能跑", code3 == 0, f"exit={code3}")

    # --details 能跑
    # 找一个存在的 yaml 文件
    sample = next((ROOT / "domains").rglob("*.yaml"))
    if sample.name == "_meta.yaml":
        sample = next(f for f in (ROOT / "domains").rglob("*.yaml") if f.name != "_meta.yaml")
    code4, out4, _ = run_script("check.py", ["--details", str(sample.relative_to(ROOT))])
    test("--details 能跑", code4 == 0 and "业务" in out4, f"exit={code4}")


def test_build_kg():
    """测试 build_kg.py。"""
    print("\n📋 build_kg.py")
    code, stdout, stderr = run_script("build_kg.py", ["--stats"])
    test("退出码为 0", code == 0, f"exit={code}, stderr={stderr[:200]}")
    test("节点数 > 0", "节点:" in stdout, "未找到节点统计")

    # 检查节点数合理
    import re
    match = re.search(r"节点:\s*(\d+)", stdout)
    if match:
        nodes = int(match.group(1))
        test("节点数 > 100", nodes > 100, f"只有 {nodes} 节点")
    else:
        test("节点数 > 100", False, "无法解析节点数")


def test_validate_platforms():
    """测试 validate_platforms.py。"""
    print("\n📋 validate_platforms.py")
    code, stdout, stderr = run_script("validate_platforms.py")
    test("退出码为 0", code == 0, f"exit={code}, stderr={stderr[:200]}")


def test_schema_consistency():
    """测试脚本与 schema 的一致性。"""
    print("\n📋 Schema 一致性")

    # 加载 schema
    schema = json.loads((ROOT / "schema" / "model.schema.json").read_text())
    schema_fields = set(schema["properties"].keys())

    # check.py 引用的字段应该在 schema 中存在
    check_src = (ROOT / "scripts" / "check.py").read_text()
    # 找 data.get("xxx") 模式
    import re
    referenced = set(re.findall(r'data\.get\(["\'](\w+)["\']', check_src))
    # 排除非字段引用
    referenced -= {"name", "stages", "framework", "techniques", "size", "comparison", "url", "title"}

    missing = referenced - schema_fields
    test("check.py 引用的字段都在 schema 中", len(missing) == 0,
         f"引用了不存在的字段: {missing}")

    # 已删除的字段不应该出现在任何脚本中
    deleted_fields = {"region", "language", "license", "pipeline_tag", "co2_eq_emissions", "model_index"}
    for script_name in ["check.py", "build_kg.py", "validate.py"]:
        script_path = ROOT / "scripts" / script_name
        if script_path.exists():
            content = script_path.read_text()
            found_deleted = [f for f in deleted_fields if f'"{f}"' in content or f"'{f}'" in content]
            test(f"{script_name} 不引用已删除字段", len(found_deleted) == 0,
                 f"还在引用: {found_deleted}")


def test_yaml_schema_match():
    """测试 YAML 文件和 schema 字段匹配。"""
    print("\n📋 YAML 字段合法性")

    schema = json.loads((ROOT / "schema" / "model.schema.json").read_text())
    schema_fields = set(schema["properties"].keys())

    violations = []
    for f in sorted((ROOT / "domains").rglob("*.yaml")):
        if f.name == "_meta.yaml":
            continue
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if not data:
            continue
        extra_fields = set(data.keys()) - schema_fields
        if extra_fields:
            violations.append((str(f.relative_to(ROOT)), extra_fields))

    test("所有 YAML 字段都在 schema 中定义",
         len(violations) == 0,
         f"{len(violations)} 文件有非法字段: {violations[:3]}")


def test_script_governance():
    """测试脚本治理：所有脚本有 docstring / 支持 -h / 被文档引用。"""
    print("\n📋 脚本治理 (check_scripts.py)")
    code, stdout, stderr = run_script("check_scripts.py")
    test("所有脚本通过治理检查", code == 0,
         stdout.split("未通过")[-1].strip()[:200] if code != 0 else "")


def main():
    global PASS, FAIL
    argparse.ArgumentParser(
        description="集成测试：验证所有脚本能正常运行且输出合理。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    ).parse_args()
    print("=" * 60)
    print("  集成测试")
    print("=" * 60)

    test_validate()
    test_check()
    test_build_kg()
    test_validate_platforms()
    test_schema_consistency()
    test_yaml_schema_match()
    test_script_governance()

    print(f"\n{'='*60}")
    print(f"  结果: {PASS} 通过, {FAIL} 失败")
    print(f"{'='*60}")

    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
