#!/usr/bin/env python3
"""脚本治理检查 — 确保每个脚本可自解释、被文档追踪。

对 scripts/ 下每个 .py 脚本（排除自身和 __init__）检查三项：
  1. 支持 -h/--help 且能正常退出（退出码 0）
  2. 有模块级 docstring（文件开头的三引号）
  3. 在文档中被引用（AGENTS.md / README.md / docs/ / SCRIPTS.md）

配套 AGENTS.md 的强制要求：每个脚本必须有详细 docstring + 支持 -h。
本脚本被 test_all.py 调用，纳入提交前门禁。

用法:
    python scripts/check_scripts.py           # 全量检查，全通过退出 0
    python scripts/check_scripts.py --json     # 输出 JSON
    python scripts/check_scripts.py -h         # 显示本帮助
"""

import argparse
import ast
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / "scripts"
DOC_PATHS = [ROOT / "AGENTS.md", ROOT / "README.md", ROOT / "SCRIPTS.md", ROOT / "docs"]

# 治理检查脚本自身不要求被文档引用（它是元工具）
SELF = "check_scripts.py"


def collect_doc_text():
    """收集所有文档文本，用于检查脚本是否被引用。"""
    texts = []
    for p in DOC_PATHS:
        if p.is_file():
            texts.append(p.read_text(encoding="utf-8", errors="ignore"))
        elif p.is_dir():
            for f in p.rglob("*.md"):
                texts.append(f.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(texts)


def has_docstring(path):
    """检查文件是否有模块级 docstring。"""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
        return ast.get_docstring(tree) is not None
    except Exception:
        return False


def supports_help(path):
    """检查脚本能否 -h 正常退出（退出码 0）。"""
    try:
        r = subprocess.run(
            [sys.executable, str(path), "-h"],
            capture_output=True, text=True, timeout=30,
        )
        return r.returncode == 0 and "usage" in (r.stdout + r.stderr).lower()
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="脚本治理检查：-h 支持 / docstring / 文档引用。",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    args = parser.parse_args()

    doc_text = collect_doc_text()
    scripts = sorted(f for f in SCRIPTS_DIR.glob("*.py") if f.name != "__init__.py")

    results = []
    for s in scripts:
        name = s.name
        r = {
            "script": name,
            "has_docstring": has_docstring(s),
            "supports_help": supports_help(s),
            "documented": (name in doc_text) or (name == SELF),
        }
        r["pass"] = r["has_docstring"] and r["supports_help"] and r["documented"]
        results.append(r)

    failed = [r for r in results if not r["pass"]]

    if args.json:
        print(json.dumps({"results": results, "failed": len(failed)}, ensure_ascii=False, indent=2))
    else:
        print(f"{'脚本':<32} {'docstring':>10} {'-h':>5} {'文档':>5}")
        print("-" * 56)
        for r in results:
            d = "✅" if r["has_docstring"] else "❌"
            h = "✅" if r["supports_help"] else "❌"
            doc = "✅" if r["documented"] else "❌"
            print(f"{r['script']:<32} {d:>10} {h:>5} {doc:>5}")
        print("-" * 56)
        print(f"  {len(results) - len(failed)}/{len(results)} 通过")
        if failed:
            print("\n  未通过的脚本:")
            for r in failed:
                missing = []
                if not r["has_docstring"]: missing.append("缺docstring")
                if not r["supports_help"]: missing.append("不支持-h")
                if not r["documented"]: missing.append("未被文档引用")
                print(f"    ❌ {r['script']}: {', '.join(missing)}")

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
