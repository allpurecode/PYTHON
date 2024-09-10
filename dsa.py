"""program 1--------------------------------------------------------------------------------------------
n = int(input())
m = int(input())
x = abs(n)
y = abs(m)
print((x % 10) + (y % 10))"""

"""program 2-----------------------------------------------------------------------------------------------------
num1 = int(input())
num2 = int(input())
if num1 == 0 or num2 == 0:
    print(3)
elif num1 % num2 == 0 or num2 % num1 == 0:
    print(2)
elif num1 % num2 != 0 or num2 % num1 != 0:
    print(1)"""

"""program 3----------------------------------------------------------------------------------------------------------
s1 = input()
s2 = input()
if len(s1) > len(s2):
    print(s2 + s1 + s2)
else:
    print(s1 + s2 + s1)"""
"""program 4-------------------------------------------------------------------------------------------------------------


def count_even_or_odd(num1, num2, num3, num4, num5, type):
    numbers = [num1, num2, num3, num4, num5]
    even_count = 0
    odd_count = 0
    for number in numbers:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if type == "even":
        return even_count
    elif type == "odd":
        return odd_count


print(count_even_or_odd(12, 17, 19, 14, 115, "odd"))  # Output: 3
print(count_even_or_odd(12, 17, 19, 14, 115, "even"))  # Output: 2"""

"""program 5--------------------------------------------------------------------------------------------------------------
number = int(input())
s = number // 10
print(s % 10)"""

"""program 6---------------------------------------------------------------------------------------------------------------
s1 = input()
s2 = input()
result = []
a = len(s1)
b = len(s2)
mini = min(a, b)
for i in range(mini):
    result.append(s1[i])
    result.append(s2[i])
if a > mini:
    result.append(s1[mini:])
else:
    result.append(s2[mini:])
print(*result)"""

"""program 7--------------------------------------------------------------------------------------------------------------

def padovan_sequence(num):

    if num <= 0:
        return []
    elif num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    elif num == 3:
        return [1, 1, 1]


    sequence = [1, 1, 1]


    for i in range(3, num):
        next_term = sequence[i - 2] + sequence[i - 3]
        sequence.append(next_term)

    return sequence


num = int(input())
sequence = padovan_sequence(num)
print(f"Padovan Sequence up to {num}:")
print(" ".join(map(str, sequence)))"""









