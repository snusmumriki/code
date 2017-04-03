n, m, k = map(int, input().split())
time = 2 * n // k
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(node, node1):
    tracks = [None] * len(graph)
    tracks[node] = node
    nodes = [node]
    while nodes:
        node = nodes.pop()
        for i in graph[node]:
            if tracks[i] is None:
                nodes.append(i)
                tracks[i] = tracks[node] + [i]
    return next(filter(lambda t: t[-1] == node1, tracks))
