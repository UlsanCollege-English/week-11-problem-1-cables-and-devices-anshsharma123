"""
HW01 — Cables and Devices
"""

def build_graph(edges, directed=False):
    g = {}

    for u, v in edges:
        if u not in g:
            g[u] = []
        if v not in g:
            g[v] = []

        g[u].append(v)

        if not directed:
            g[v].append(u)

    return g


def degree_dict(graph):
    d = {}
    for node in graph:
        d[node] = len(graph[node])
    return d


if __name__ == "__main__":
    sample = [('PC1','SW1'), ('SW1','PR1'), ('PR1','PC2')]
    print(build_graph(sample, directed=False))
    print(degree_dict(build_graph(sample, directed=False)))
