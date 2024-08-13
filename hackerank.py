# list comprehensions
'''x = int(input())
y = int(input())
z = int(input())
n = int(input())
coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(coordinates)'''

'''no_students = int(input())
student = []
for _ in range(no_students):
    name = input()
    grade = float(input())
    student.append([name, grade])
grades = [grade for name, grade in student]
unique_grades = sorted(set(grades))
second_lowest_grade = unique_grades[1]
second_lowest_students = [name for name, grade in student if grade == second_lowest_grade]
second_lowest_students.sort()
for student in second_lowest_students:
    print(student)'''


# dictioniers
'''def koo(*args):
    print(args)


koo('a', 'b', 'c')  # Using *args to Collect Positional Arguments


def foo(**kwargs):
    print(kwargs)


foo(a=1, b=2)  # Using **kwargs to Collect Keyword Argument


def foo(a, b, c):
    print(a, b, c)


args = (1, 2, 3)
foo(*args)


def soo(a, b, c):
    print(a, b, c)


kwargs = {'a': 1, 'b': 2, 'c': 3}
soo(**kwargs)'''

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
average_score = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{average_score:.2f}")
