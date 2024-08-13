# 1.1 two sum
'''nums = list(map(int, input().split(', ')))
target = int(input())
list1 = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            list1.append(sorted([i, j]))
for k in list1:
    print(k)'''

# PROGRAM 2
'''list_l = list(map(int, input().split()))
target = int(input())

if target in list_l:
    print(1)
else:
    print(0)'''

# 1.5 majority elements
'''list_r = list(map(int, input().split()))
n = len(list_r)
for i in list_r:
    if list_r.count(i) > n / 2:
        print(i)
        break'''

# 1.2 duplicate
'''def has_duplicates(lst):
    seen_set = {}  # it stores the elements in dic such as 1:true
    for item in lst:
        if item in seen_set:
            return True
        seen_set[item] = True
    return False


my_list = list(map(int, input().split()))
print(has_duplicates(my_list))'''

# 1.3 roman to integer
'''s = input()


def roman(number):
    ans = 0
    dic_1 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(s)):
        if i < len(s) - 1 and dic_1[s[i]] < dic_1[s[i + 1]]:
            ans -= dic_1[s[i]]
        else:
            ans += dic_1[s[i]]
    return ans


print(roman(s))'''

# 1.4 plus one
'''list_r = list(map(int, input().split()))
list_r = list(list_r)
print(list_r)
s = ''
for i in list_r:
    s = s + str(i)
#print(str(int(s)+1))
n=str(int(s)+1)

list=[]
for j in n:
    list.append(int(j))
print(list)'''

# 1.6 nested list
'''arr = [list(map(int, i.split())) for i in input().split(',')]
print(arr)
sums=[]
for i in arr:
    sums.append(sum(i))
print(sums)
print(max(sums))'''

# 1.7 fizz buzz
'''list_u = []
n = int(input("enter the number:"))
for i in range(1, n + 1):
    if i % 3 == 0:
        list_u.append("fizz")
    elif i % 5 == 0:
       list_u.append("buzz")
    elif i % 5 == 0 and i % 3 == 0:
        list_u.append("fizzBuzz")
    else:
        list_u.append((i))

print(list_u)'''

# 1.8 Number of Steps to Reduce a Number to Zero
'''count = 0
given = int(input("enter the number:"))
while given > 0:
    if given % 2 == 0:
        given = given / 2
    else:
        given = given - 1
    count = count + 1

print(count)'''

# 1.9 Running Sum of 1D Array
'''arr = list(map(int, input().split()))
print(arr)
list_E = []
sum = 0
for i in arr:
    sum= sum+i
    list_E.append(sum)

print(list_E)'''

# 1.10 Remove Element
'''arr = list(map(int, input().split()))
value = int(input("enter the value:"))
print(arr)
empty_list=[]
for i in arr:
    if i==value:
        empty_list.append('_')
    else:
        empty_list.append(i)
print(empty_list)'''

# 2.1 add two matrices
'''X= [list(map(int, i.split())) for i in input().split(',')]
Y = [list(map(int, i.split())) for i in input().split(',')]


result = [[0]*3 for i in range(len(X))]

for i in range(len(Y)):
    for j in range(len(Y[0])):
        result[i][j] = X[i][j] + Y[i][j]
for k in result:
    print(k)'''

# 2.2 multiplication of matrix
'''k1 = int(input("enter the number of rows of first matrix:")) ,'
k2 = int(input("enter the rows of row of second matrix:"))
M1 = []
M2 = []
for i in range(k1):
    M1.append(list(map(int, input().split())))
for i in range(k2):
    M2.append(list(map(int, input().split())))

result_M = [[0] * max(len(M1), len(M2)) for i in range(len(M1))]

for i in range(len(M1)):
    for j in range(len(M2[0])):
        for k in range(len(M1[0])):
            result_M[i][j] += M1[i][k] * M2[k][j]
for i in result_M:
    print(i)'''

# 2.3 transpose of matrix
'''n1 = int(input("enter the number of rows:"))
mat1 = []
for i in range(n1):
    mat1.append(list(map(int, input().split())))

transpose = [[0] * len(mat1) for i in range(len(mat1[0]))]
for i in range(len(mat1[0])):
    for j in range(len(mat1)):
        transpose[i][j] = mat1[j][i]
for i in transpose:
    print(i)'''

# 2.4 multiplication matrix
'''list1 = int(input("enter the inner list"))
list_empty = []
for i in range(list1):
    list_empty.append(list(map(int, input().split())))
result = 1
for i in list_empty:
    for j in i:
        result = result * j
print(result)'''

# 3.3
'''string_1 = input()
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for i in string_1:
    if i in vowels:
        count = count + 1
print(count)

for i in string_1:
    if i != 'e' and i != 's':
        print(i,end=' ')'''

