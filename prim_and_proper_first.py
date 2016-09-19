def clear_edges(E, V):
    to_remove = []
    for i, e in enumerate(E):
        if e[0] in V and e[1] in V:
            to_remove.append(i)
    # we now have to_remove which is a list of edges indexes to remove
    to_remove.sort(reverse=True)
    for i in to_remove:
        E.pop(i)


N, M = map(int, input().strip().split(' '))
nodes = [x for x in range(1, N+1)]
edges = []
for _ in range(M):
    x, y, r = map(int, input().strip().split(' '))
    if y < x:
        temp = y
        y = x
        x = temp
    edges.append([x, y, r])
vertices = [0, int(input().strip())]
weight = 0
while len(nodes) > 0:
    test = [edge for edge in edges if edge[0] in vertices or edge[1] in vertices]
    test.sort(key=lambda x: x[2])
    weight += test[0][2]
    if test[0][0] in nodes: nodes.remove(test[0][0])
    if test[0][1] in nodes: nodes.remove(test[0][1])
    if test[0][0] not in vertices: vertices.append(test[0][0])
    if test[0][1] not in vertices: vertices.append(test[0][1])
    clear_edges(edges, vertices)

print(weight)
