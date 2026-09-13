#!/usr/bin/env python3
"""kg_query.sh 的表格渲染辅助脚本。

从 stdin 读取 `jc neo4j query` 的 JSON 输出，渲染成 CJK 宽度对齐的表格。
仅供 scripts/kg_query.sh 内部调用；单独运行可用于调试（管道喂入 jc 输出）。

用法:
    jc neo4j query --cypher '...' | python3 scripts/_kg_render.py
"""
import json
import sys


def w(s: str) -> int:
    """CJK 宽字符计 2，其余计 1。"""
    return sum(2 if ord(c) > 0x2E80 else 1 for c in s)


def pad(s: str, width: int) -> str:
    return s + " " * (width - w(s))


def cell(v) -> str:
    if v is None:
        return "-"
    if isinstance(v, (list, dict)):
        return json.dumps(v, ensure_ascii=False)
    return str(v)


def main() -> int:
    import argparse
    argparse.ArgumentParser(
        description="从 stdin 读取 jc neo4j query 的 JSON，渲染为对齐表格。"
    ).parse_args()
    raw = sys.stdin.read()
    try:
        resp = json.loads(raw)
    except Exception:
        print(raw)
        return 0
    if not resp.get("success"):
        print("查询失败:", resp.get("message") or resp)
        return 1
    data = resp.get("data", {})
    fields = data.get("fields", [])
    records = data.get("records", [])
    if not records:
        print("(无结果)")
        return 0
    rows = [[cell(r.get(f)) for f in fields] for r in records]
    widths = [max(w(fields[i]), *(w(row[i]) for row in rows)) for i in range(len(fields))]
    print(" | ".join(pad(fields[i], widths[i]) for i in range(len(fields))))
    print("-+-".join("-" * widths[i] for i in range(len(fields))))
    for row in rows:
        print(" | ".join(pad(row[i], widths[i]) for i in range(len(fields))))
    print(f"\n({len(records)} 行)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
