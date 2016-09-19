import heapq
from collections import defaultdict

graph = defaultdict(list)
weight = 0
subtree_vertices = set([])
priority_queue = []

vertices, edges = map(int, input().strip().split(' '))
for _ in range(edges):
    x, y, w = map(int, input().strip().split(' '))
    graph[x].append((w, y))
    graph[y].append((w, x))
starting_vertex = int(input().strip())
subtree_vertices.add(starting_vertex)
for vertex in graph[starting_vertex]:
    heapq.heappush(priority_queue, vertex)
while priority_queue:
    wt, y = heapq.heappop(priority_queue)
    if y not in subtree_vertices:
        weight += wt
        subtree_vertices.add(y)
        for vertex in graph[y]:
            heapq.heappush(priority_queue, vertex)

print(weight)
