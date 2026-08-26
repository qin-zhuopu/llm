#!/usr/bin/env python3
"""从 YAML 文件构建知识图谱（NetworkX，无需 API）。

直接解析现有 YAML 数据建立实体-关系图，不依赖任何外部服务。

用法:
    python scripts/build_kg.py              # 构建并保存
    python scripts/build_kg.py --stats      # 只输出统计
    python scripts/build_kg.py --query "Microsoft"  # 查询某节点的关系

输出:
    kg_data.graphml — 可用 Gephi/yEd/Cytoscape 可视化
"""

import argparse
import sys
from pathlib import Path

import networkx as nx
import yaml


ROOT = Path(__file__).resolve().parent.parent


def build_graph():
    """从 YAML 文件构建知识图谱。"""
    G = nx.DiGraph()

    # === 从 domains/*.yaml 建图 ===
    domains_dir = ROOT / "domains"
    for f in sorted(domains_dir.rglob("*.yaml")):
        if f.name == "_meta.yaml":
            continue
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        if not data:
            continue

        model_name = data.get("name", f.stem)
        company = data.get("company", "")
        domain = f.parent.name

        # 模型节点
        G.add_node(model_name, type="model", domain=domain,
                   parameters=data.get("parameters", ""),
                   status=data.get("status", ""),
                   website=data.get("website", ""),
                   file=str(f.relative_to(ROOT)))

        # 公司 → 模型
        if company:
            G.add_node(company, type="company")
            G.add_edge(company, model_name, relation="developed")

        # 模型 → 领域
        G.add_node(domain, type="domain")
        G.add_edge(model_name, domain, relation="in_domain")

        # 模型 → 基座模型
        base = data.get("base_model")
        if base:
            bases = base if isinstance(base, list) else [base]
            for b in bases:
                G.add_node(b, type="base_model")
                G.add_edge(model_name, b, relation="based_on")

        # 模型 → 标签
        for tag in data.get("tags", []):
            G.add_node(tag, type="tag")
            G.add_edge(model_name, tag, relation="tagged")

        # 模型 → 访问方式
        for acc in data.get("access", []):
            G.add_node(acc, type="access_type")
            G.add_edge(model_name, acc, relation="accessible_via")

    # === 从 platforms/*.yaml 建图 ===
    platforms_dir = ROOT / "platforms"
    if platforms_dir.exists():
        for f in sorted(platforms_dir.glob("*.yaml")):
            if f.name in ("_meta.yaml", "schema.json"):
                continue
            data = yaml.safe_load(f.read_text(encoding="utf-8"))
            if not data:
                continue
            name = data.get("name", f.stem)
            company = data.get("company", "")
            G.add_node(name, type="platform",
                       website=data.get("website", ""),
                       file=str(f.relative_to(ROOT)))
            if company:
                G.add_node(company, type="company")
                G.add_edge(company, name, relation="operates")

    return G


def print_stats(G):
    """输出图统计信息。"""
    print(f"节点: {G.number_of_nodes()}")
    print(f"边:   {G.number_of_edges()}")
    print()
    types = {}
    for _, d in G.nodes(data=True):
        t = d.get("type", "unknown")
        types[t] = types.get(t, 0) + 1
    print("按类型:")
    for t, c in sorted(types.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


def query_node(G, name):
    """查询某节点的所有关系。"""
    # 模糊匹配
    matches = [n for n in G.nodes if name.lower() in n.lower()]
    if not matches:
        print(f"未找到包含 '{name}' 的节点")
        return

    for node in matches:
        node_data = G.nodes[node]
        print(f"\n{'='*60}")
        print(f"节点: {node}")
        print(f"类型: {node_data.get('type', '?')}")
        for k, v in node_data.items():
            if k != "type" and v:
                print(f"  {k}: {v}")

        # 出边
        out_edges = list(G.out_edges(node, data=True))
        if out_edges:
            print(f"\n  出边 ({len(out_edges)}):")
            for _, target, d in out_edges:
                print(f"    → [{d.get('relation', '?')}] → {target}")

        # 入边
        in_edges = list(G.in_edges(node, data=True))
        if in_edges:
            print(f"\n  入边 ({len(in_edges)}):")
            for source, _, d in in_edges:
                print(f"    ← [{d.get('relation', '?')}] ← {source}")


def main():
    parser = argparse.ArgumentParser(description="从 YAML 构建知识图谱")
    parser.add_argument("--stats", action="store_true", help="只输出统计")
    parser.add_argument("--query", type=str, help="查询某节点的关系（模糊匹配）")
    parser.add_argument("--output", type=str, default="kg_data.graphml", help="输出文件路径")
    args = parser.parse_args()

    G = build_graph()

    if args.query:
        query_node(G, args.query)
    elif args.stats:
        print_stats(G)
    else:
        # 默认：保存并输出统计
        output_path = ROOT / args.output
        nx.write_graphml(G, str(output_path))
        print(f"知识图谱已保存: {output_path}")
        print()
        print_stats(G)


if __name__ == "__main__":
    main()
