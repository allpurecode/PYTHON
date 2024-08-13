'''S1 = []  # Stack data structures LIFO(Last in first out)
S1.append(1)
S1.append(2)
S1.append(3)
S1.append(4)
S1.append(5)
print(S1)
print(S1.pop())
print(S1.pop())

# Queue
S2 = []
S2.append('a')
S2.append('b')
S2.append('c')
S2.append('d')
print(S2)
print(S2[0])'''

# DFS
'''graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
Start = 0 # 1 if graph key values are from 1.
Stack = [Start]
visited = set()
while Stack:
    vertex = Stack.pop()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        Stack.extend(beside for beside in graph.get(vertex, []) if beside not in visited)'''

# BFS
'''graph2 = {1: [8, 5, 2], 8: [6, 4, 3], 2: [9],
          6: [10, 7]}  # begin=1 or 0 if it begins from 1 or 0 respectively  # {0: [1, 2], 1: [3], 2: [4, 5]}
begin = 1
que = [begin]
visited = set()
while que:
    vertex = que.pop(0)
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        que.extend(beside for beside in graph2.get(vertex, []) if beside not in visited)'''

# adjacency Matrix[undirected and directed]

# no_vertices = int(input("Enter the number of vertices"))
# no_edges = int(input("Enter the number of edges"))

'''no_vertices, no_edges = map(int, input('enter vertices and edges').split(','))
vertices = []
edges = []

# vertices
for i in range(no_vertices):
    v = int(input("Enter the vertex:"))
    vertices.append(v)
print(vertices)

# edges
for j in range(no_edges):
    e = tuple(map(int, input("Enter the edge:").split(',')))
    edges.append(e)
    edges = sorted(edges, key=lambda x: x[0])

# Adjacency Matrix
Adj_Matrix = [[0] * no_vertices for l in range(no_vertices)]

for e in edges:
    v1, v2 = e
    Adj_Matrix[v1][v2] = 1  # [v1-1][v2-1]/// [v1-no_vertices[0]][v2-no_vertices[1]]
    Adj_Matrix[v2][v1] = 1  # required for directed graphs
# v v1, v2 ,w= e
# Adj_Matrix[v1][v2] = w  # [v1-1][v2-1]/// [v1-no_vertices[0]][v2-no_vertices[1]]
# Adj_Matrix[v2][v1]=w   #  required for directed graphs
# print()

for i in Adj_Matrix:
    for j in i[:-1]:
        print(j, end=', ')
    print(i[-1])



    # for matrix in Adj_Matrix:
    # print(*matrix)

    # incidence'''
'''
nv = int(input("enter the number of vertices:"))
ne = int(input("enter the number of edges:"))
vertices = []
for i in range(nv):
v = int(input("enter the vertices:"))
vertices.append(v)
print(vertices)
edges = []
for i in range(ne):
e = tuple(map(int, input("enter the edges:").split(',')))
edges.append(e)
print(edges)
inc_mat = [[0] * nv for i in range(ne)]
for x in edges:
v1, v2, = x  # w # for weighted graphs
inc_mat[vertices.index(v1)][edges.index(x)] = 1  # w
inc_mat[vertices.index(v2)][edges.index(x)] = 1  # -1 if directed
for j in inc_mat:
print(*j)
'''

# adjacency list

'''no_vertices = int(input("Enter the number of vertices:"))
no_edges = int(input("Enter the number of edges:"))

vertices = []
edges = []

# vertices
for i in range(no_vertices):
    v = int(input("Enter the vertices:"))
    vertices.append(v)
print(vertices)

# edges
for j in range(no_edges):
    e = tuple(map(int, input("Enter the edge").split(',')))
    edges.append(e)
    edges = sorted(edges, key=lambda x: x[0])
print(edges)

adjacency_list = {}
for e in edges:
    if e[0] not in adjacency_list.keys():
        adjacency_list[e[0]] = [e[1]]
    else:
        adjacency_list[e[0]].append(e[1])

    if e[1] not in adjacency_list.keys():
        adjacency_list[e[1]] = [e[0]]

    else:
        adjacency_list[e[1]].append(e[0])

for k in adjacency_list:
    adjacency_list[k] = sorted(adjacency_list[k])

for i in vertices:
    print(str(i) + ":", end="")
    print(adjacency_list[i])'''

# multiedge

''' no_edges = int(input("Enter the number of edges:"))
edges_set = set()
for i in range(no_edges):
 e = tuple(map(int, sorted(input("enter the edge").split())))
 edges_set.add(e)
print(sorted(edges_set))

if len(edges_set) != no_edges:
 print("yes it has multiedge")
else:
 print("no multi-edges")
 '''

'''nv, ne = map(int, input().split(','))


edges = []
for i in range(ne):
    edge = list(map(int, input().split(',')))
    edges.append(edge)

# ADJACENCY MATRIX
adj_mat = [[1 if [i, j] in edges or [j, i] in edges else 0 for j in range(nv)] for i in range(nv)]
print("Adjacency Matrix")
for j in adj_mat:
    for i in j[:-1]:
        print(i,end=", ")
    print(j[-1])

# ADJACENCY LIST
adj_list = {v: [] for v in range(nv)}
for v1, v2 in edges:
    adj_list[v1].append(v2)
    adj_list[v2].append(v1) #nv, ne = map(int, input().split(','))


edges = []
for i in range(ne):
    edge = list(map(int, input().split(',')))
    edges.append(edge)

# ADJACENCY MATRIX
adj_mat = [[1 if [i, j] in edges or [j, i] in edges else 0 for j in range(nv)] for i in range(nv)]
print("Adjacency Matrix")
for j in adj_mat:
    for i in j[:-1]:
        print(i,end=", ")
    print(j[-1])

# ADJACENCY LIST
adj_list = {v: [] for v in range(nv)}
for v1, v2 in edges:
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

print("Adjacency List")
for i in range(nv):
    print( i, ":", adj_list[i])


print("Adjacency List")
for i in range(nv):
    print( i, ":", adj_list[i])'''


def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


def count_connected_components(n, e, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = {i: False for i in range(1, n + 1)}
    count = 0
    for node in range(1, n + 1):
        if not visited[node]:
            dfs(graph, visited, node)
            count += 1

    return count


n, e = map(int, input().split())
edges = []
for _ in range(e):
    u, v = map(int, input().split())
    edges.append((u, v))

print(count_connected_components(n, e, edges))
