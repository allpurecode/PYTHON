'''n = int(input())
i = 1
while i <= n:
    print(str(i), end="")
    i = i +1'''

'''from collections import namedtuple

n = int(input())
headings = input().split()
totalMarks = 0
for i in range(n):
    Student = namedtuple("Topper", headings)
    inp = input().split()
    Topper = Student(inp[0], inp[1], inp[2], inp[3])
    totalMarks += int(Topper.MARKS)
print(totalMarks/n)'''

'''number= int(input("Enter the numbers"))
arr = map(int, input().split())
uniqueScore = list(set(arr))
rearranged= sorted(uniqueScore, reverse=True)  # reverse oder descending order
print(rearranged[1])'''

'''chota = ['n', 'f', 'e', 'o', 'a', 'b']
rearranged= sorted(chota)
print(rearranged)'''
