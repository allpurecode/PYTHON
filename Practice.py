'''n = int(input())
if n % 2 == 1:
    print("weird")
    elif n % 2 == 0 and n>=6 and n <= 20:
    print("weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("not weird ")

else:
    print("not weird")'''

'''n = int(input())
for i in range(0,n):
    print(i*i)'''

# dictionary
dict1 = {1: 'red', 2: 'green', 3: 'yellow', 4: 'white'}
'''print(dict1.keys())
print(dict1.items())
print(dict1[2])
for i in dict1:
    print(i)
    print(dict1[i])
    print(i,dict[i])

for a, b in dict1.items():
    print(a, b)'''
'''
# undirected
G = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['B', 'D']}
for i in G:
    print(i, G[i])
# directed
Gd = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['D'], 'D': ['E'], 'E': []}

for i in Gd:
    m=len(Gd[i])
    print("the degree of " + i + ":", len(Gd[i]))
    if m == 0:
        print(i, "is the sink node")'''

'''# complete graph
G1 = {'A': ['B', 'D', 'C'], 'B': ['A', 'C', 'D'], 'C': ['A', 'B', 'D'], 'D': ['A', 'B', 'C']}
for i in G1:
    a = (len(G1))
    b = len(G1[i])
if b == a - 1:
    print("This is a complete graph")
else:
    print("This is not a complete graph")'''

'''# loops presence
G2 = {'A': ['A', 'B', 'D'], 'B': ['B','A', 'C'], 'C': ['D', 'B'], 'D': ['A', 'C']}
count = 0
for i in G2:
    if i in G2[i]:
        count = count + 1

print("the no of loops are:", count)'''
'''thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-1:-5])'''

'''cubes = []
for i in range(7):
    cubes.append(i ** 3)
print("cubes of the number from 0-6:", cubes)

cubes2 = [i ** 3 for i in range(7)]
print("cubes of the numbers :", cubes2)

List = [(x, y) for x in [10, 20, 30] for y in [30, 10, 40]]
print("two list:", List)

#ENUMERATE
Number_list=[1,2,3,4,5]
for index, i in enumerate(Number_list):
    print(index,i)'''

'''nv = int(input("enter the number of vertices:"))
ne = int(input("enter the number of edges:"))
vertices = []  # [0, 1, 2, 3, 4]
for i in range(nv):
    vertex = int(input('Enter the vertices'))
    vertices.append(vertex)
print(vertices)
edges = []  # [(0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (2, 3), (3, 4)]
for i in range(ne):
    edge = tuple(map(int, input("Enter an edge").split()))  # int should be removed if string values
    edges.append(edge)
print(edges)

adj_matrix = [[0] * nv for x in range(nv)]
for e in edges:
    v1, v2 = e  # v1,v2,w=e
adj_matrix[(v1)][(v2)] = 1
adj_matrix[(v2)][(v1)] = 1  # for numbers #instead of 1 put w for weighted graphs

for j in adj_matrix:
    print(j)

# patters
row =int(input("Enter the no of rows"))
for i in range (0,row):
   print("*"*i)'''

# functions
'''def add(a, b):
    return a + b
a = 9
b = 9
print(add(a, b))'''

# factorial


'''def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


n = int(input("Enter the number"))
print(fact(n))'''

# prime
'''def prime(n):
    count = 0
    for i in range(1, 1 + n):
        if n % i == 0:
            count = count + 1
    if count == 2:
        print("Prime no")
    else:
        print("not a prime")


n = int(input("Enter the numbers"))
prime(n)''';

# lamda
'''s = lambda n: n * n
n=int(input("Enter the number n:"))
print(s(n))

S1= lambda a,b,c:a+b+c
print(S1(3,4,5))'''

'''my_list = [1, 3, 4, 8, 11, 12]
new_list = list(filter(lambda x:( x % 2 == 0),my_list))
print(new_list)'''

# stack
'''stack = []
size = int(input("Enter the size of stack"))


def push(stack, item):
    if len(stack) == size:
        print("stack overflow")
        print(stack)
    else:
        stack.append(item)
        print(stack)


def pop():
    if len(stack) == 0:
        print("stack underflow")
    else:
        stack.pop()
        print(stack)


def display():
    print(stack)


def peek():
    n = len(stack)
    print(stack[n - 1])


print("menu 1.push 2.pop  3.display 4.peek 5.exit")
while 1:
    ch = int(input("Enter the choice "))
    if ch == 1:
        item = int(input("Enter element"))
        push(stack, item)
    elif ch == 2:
        pop()
    elif ch == 3:
        display()
    elif ch == 4:
        peek()
    else:
        print("Enter valid input:")
        exit(0)'''

# queue

'''que = []
size = int(input("Enter the size of queue"))


def insert(que, item):
    if len(que) == size:
        print("queue overflow")

        print(que)
    else:
        que.append(item)
        print(que)


def delete():
    if len(que) == 0:
        print("que underflow")
    else:
        que.pop(0)
        print(que)


def display():
    print(que)


print("menu 1.insert 2.delete 3.display  4.exit")
while 1:
    ch = int(input("Enter the choice "))
    if ch == 1:
        item = int(input("Enter element"))
        insert(que, item)
    elif ch == 2:
        delete()
    elif ch == 3:
        display()
    elif ch == 4:
        exit()
    else:
        print("Enter valid input:")
        exit(0)'''

'''class student:
    def __init__(self, name, roll, age):
        self.name = name
        self.age = age
        self.roll = roll

    def display(self):
        print("name:{}".format(self.name))
        print("roll:{}".format(self.roll))
        print("age:{}".format(self.age))


s1 = student("ajay", 12, 23)
s2 = student("choota bheem", 10, 10)
s1.display()
s2.display()'''

# Abstraction
'''from abc import ABC  # abstract base class


class polygon(ABC):
    def sides(self):
        pass


class triangle(polygon):
    def sides(self):
        b = int(input("Enter the base:"))
        h = int(input("Enter the height:"))
        print("It has three sides")
        area = 1 / 2 * b * h
        print(area)


class square(polygon):
    def sides(self):
        s = int(input("Enter the side:"))
        print(" it has four sides")
        area = s * s
        print(area)


t = triangle()
t.sides()
# s = square()
# s.sides()'''

# inheritance
'''class A:
    def display(self):
        print("A")


class B(A):
    def display1(self):
        print("B")


a = A()
b = B()
a.display()
b.display()
b.display1()'''

# linear search
'''a = [10, 20, 45, 1, 89, 69]
print(a)
target = int(input("Enter the wanted number:"))


def linear(a, target):
    for i in range(len(a)):
        if target == a[i]:
            return 1
    return -1


result = linear(a, target)
if result!=-1:
    print("The number exist")
else:
    print("the numbers doesnt not exist ")'''

# binary search
'''n = int(input("enter the number of elements:"))
l = []
for i in range(n):
    k = int(input("enter the element:"))
    l.append(k)
    l = sorted(l)
print(l)

target = int(input("Enter the wanted number :"))


def binary(l, target):
    low = 0
    high = len(l) - 1
    while low < high:
        mid_point = (low + high) // 2
        if target == l[mid_point]:
            return 1
        elif l[mid_point] < target:
            low = mid_point + 1
        else:
            high = high - 1
            return -1


result = binary(l, target)
if result != -1:
    print("number found")
else:
    print("number not found")

# linear search with input
n = int(input("Enter the number of elements:"))
list_p = []
for i in range(n):
    e = int(input("enter the element:"))
    list_p.append(e)
print(list_p)

target = int(input("Enter the wanted number:"))


def linear(list_p, target):
    for i in range(len(list_p)):
        if target == list_p[i]:
            return 1
    return -1


result = linear(list_p, target)
if result != -1:
    print("The number exist")
else:
    print("the numbers doesnt not exist ") '''

# degree sequence
'''import sys

deq_seq = [7, 6, 6, 4, 4, 3, 2, 2]
seq = sorted(deq_seq, reverse=True)
print(seq)
if sum(seq) % 2 != 0:
    print(deq_seq, "is an invalid degree sequence")
    sys.exit()
while True:
    first_element = seq.pop(0)
    for i in range(first_element):
        seq[i] -= 1
        seq = sorted(seq, reverse=True)
        print("seq", seq)
        if -1 in seq:
            print("invalid sequence")
            sys.exit()
        if not (any(seq)):
            print(deq_seq, "is valid degree sequence")
            sys.exit()'''
# WEEK 12-(DIJKISTRA)----------------------------------------------------------------------
'''import sys

nv = int(input())
start = int(input())
graph = []
for i in range(nv):
    arr = list(map(int, input().split()))
    graph.append(arr)

dist = [sys.maxsize] * nv
dist[start] = 0
visited = [False] * nv
for vertex in range(nv):
    min_dist = sys.maxsize
    for u in range(nv):
        if dist[u] < min_dist and visited[u] == False:
            min_dist = dist[u]
            min_index = u

    visited[min_index] = True

    for i in range(nv):
        if graph[min_index][i] > 0 and visited[i] == False and dist[i] > dist[min_index] + graph[min_index][i]:
            dist[i] = dist[min_index] + graph[min_index][i]
for i in dist[:-1]:
    print(i, end=' ')
print(dist[-1])'''


# week 10--------------------------------------------------------------------------------------------------------------
'''def euler_method(x0, y0, h, x):
    y = y0
    while x0 < x:
        y = y + h * (x0 + y + x0 * y)
        x0 = x0 + h
    return round(y, 4)


x0 = int(input())
y0 = int(input())
h = float(input())
x = float(input())

print(euler_method(x0, y0, h, x))


def f_x(x,y):
    fx = -2*x*y**2
    return (round(fx,4))

x0 = int(input())
y0 = int(input())
x = float(input())

h = x - x0

k1 = h*f_x(x0,y0)
k2 = h*f_x(x0+h,y0+k1)

y = y0 + 0.5*(k1 + k2)

print(round(y,4))'''


