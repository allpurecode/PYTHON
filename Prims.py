import heapq
nv,ne=map(int,input().split(","))
edges=[]
for i in range(ne):
    edge=tuple(map(int,input().split(", ")))
    edges.append(edge)
adj_list={v:[] for v in range(nv)}
for w,v1,v2 in edges:
    adj_list[v1].append((w,v2))
    adj_list[v2].append((w,v1))

def prim(adj_list,start):
    mst=[]
    visited=set()
    heap=[(0,start)]
    while heap:
        w,v1,v2=heapq.heappop(heap)
        if v2 not in visited:
            visited.add(v2)
            mst.append(w,v1,v2)
            for w,n in adj_list[v2]:
                if n not in visited:
                    heapq.heappush(heap,(w,v2,n))
    return mst

start =0
mst=prim(adj_list, start)
tot=0
for w, v1, v2 in mst:
    tot+=w
print(tot)














