"""import heapq

nv, ne = map(int, input().split(","))
edges = []
for i in range(ne):
    edge = tuple(map(int, input().split(", ")))
    edges.append(edge)
adj_list = {v: [] for v in range(nv)}
for w, v1, v2 in edges:
    adj_list[v1].append((w, v2))
    adj_list[v2].append((w, v1))


def prim(adj_list, start):
    mst = []
    visited = set()
    heap = [(0, start)]
    while heap:
        w, v1, v2 = heapq.heappop(heap)
        if v2 not in visited:
            visited.add(v2)
            mst.append(w, v1, v2)
            for w, n in adj_list[v2]:
                if n not in visited:
                    heapq.heappush(heap, (w, v2, n))
    return mst


start = 0
mst = prim(adj_list, start)
tot = 0
for w, v1, v2 in mst:
    tot += w
print(tot)
"""


# quicksort
"""def QuickSort(A, l, r):
    if r - l <= 1:
        return ()
    yellow = l + 1
    for green in range(l + 1, r):
        if A[green] <= A[l]:
            (A[yellow], A[green]) = (A[green], A[yellow])
            yellow = yellow + 1
    (A[l], A[yellow - 1]) = (A[yellow - 1], A[l])
    QuickSort(A, l, yellow - 1)
    QuickSort(A, yellow, r)


A = list(map(int, input().split(" ")))
print(QuickSort(A, 0, len(A)))
print(A)"""


# merge sort ------------------------------------------------------------------------------------------------------


def merge(A, B):
    (c, m, n) = ([], len(A), len(B))  # Initialize the merged list and lengths
    (i, j) = (0, 0)  # Two pointers to track position in A and B

    while i + j < m + n:
        if i == m:  # If all elements of A are used, add the rest of B
            c.append(B[j])
            j = j + 1
        elif j == n:  # If all elements of B are used, add the rest of A
            c.append(A[i])
            i = i + 1
        elif A[i] <= B[j]:  # If A's current element is smaller or equal, add it to merged list
            c.append(A[i])
            i = i + 1
        else:  # Otherwise, add B's current element to the merged list
            c.append(B[j])
            j = j + 1


    return c

def merge_sort(A, left, right):
    if right - left <= 1:
        return A[left:right]  # Base case: single element or empty array

    mid = (left + right) // 2  # Correct division to find the middle point
    L = merge_sort(A, left, mid)  # Recursively sort left half
    R = merge_sort(A, mid, right)  # Recursively sort right half

    return merge(L, R)  # Merge the two sorted halves

# Dynamic input for the array
A = list(map(int, input("Enter elements of the array separated by spaces: ").split()))

# Call merge_sort on the full array (left is 0, right is len(A))
sorted_array = merge_sort(A, 0, len(A))

# Print the sorted array
print("Sorted array:", sorted_array)




