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

"""program 8--------------------------------------------------------------------------------------------------------------
def find_leaders(arr):
    leaders = []

    if not arr:
        return leaders  # Return empty list if the array is empty

    n = len(arr)
    max_from_right = arr[-1]  # The last element is always a leader
    leaders.append(max_from_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            max_from_right = arr[i]
            leaders.append(max_from_right)

    leaders.reverse()
    return leaders

# Example usage
arr = [16, 17, 4, 3, 5, 2]
print("Leaders:", find_leaders(arr))  # Output: [17, 5, 2]"""

"""program 9--------------------------------------------------------------------------------------------------------------
def modular_exponentiation(base, exp, mod):
    result = 1
    base = base % mod  # Handle base greater than mod
    while exp > 0:
        if (exp % 2) == 1:  # If exp is odd
            result = (result * base) % mod
        exp = exp >> 1  # Right shift exp by 1 (divide by 2)
        base = (base * base) % mod  # Square the base
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])

    # Compute the reverse of the number N
    originalN = N
    rev = 0
    while N > 0:
        digit = N % 10
        rev = rev * 10 + digit
        N = N // 10

    # Define the modulo value
    MOD = 1000000007
    # Calculate (originalN^rev) % MOD
    result = modular_exponentiation(originalN, rev, MOD)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
"""
"program 10--------------------------------------------------------------------------------------------------------------"

"""def findMean(arr, start, end):
    if start >= end:
        return 0
    else:
        sum = arr[start] + findMean(arr, start + 1, end)
        return sum / end - start


arr = []
print("no of elements in arr:")
n = int(input())
print("give the elemnts")
for i in range(n):
    arr.append(int(input()))
print(findMean(arr, 0, n))"""

"""def findMean(arr, start, end):
    if start == end:  # Base case: no elements to sum
        return 0
    elif start == end - 1:  # Base case: single element
        return arr[start]
         else:
        # Calculate the sum of all elements
        sum = arr[start] + findMean(arr, start + 1, end)
        # Return sum divided by the number of elements
        if start == 0:
            return sum / (end - start)  # Division should be done only once
        return sum


arr = []
print("Number of elements in arr:")
n = int(input())
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

mean = findMean(arr, 0, n)
print("Mean of the array is:", mean)"""

# WEEK 2----------------------------------------------------------------------------------------------------------------------------
# linear search

"""a = list(map(int, input().split(", ")))
target = int(input("Enter the wanted number:"))


def linear(a, target):
    for i in range(len(a)):
        if target == a[i]:
            return 1
    return -1


result = linear(a, target)
if result != -1:
    print("The number exist")
else:
    print("the numbers doesnt not exist ")"""

# -------------------------------------------------------------------------------------------------------------------------------------------
# binary search
n = int(input("enter the number of elements:"))
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
    while low <= high:
        mid_point = (low + high) // 2
        if target == l[mid_point]:
            return 1
        elif l[mid_point] > target:
            high = mid_point - 1
        else:
            low = mid_point + 1
    return -1


result = binary(l, target)
if result != -1:
    print("number found")
else:
    print("number not found")


# ---------------------------------------------------------------------------------------------------------------------------
# Uniform binary search
def uniform_binary_search(arr, target):
    n = len(arr)

    # Precompute the jump sizes
    steps = []
    step = n // 2
    while step > 0:
        steps.append(step)
        step //= 2

    low = 0
    high = n - 1

    # Iterate over the precomputed steps
    for step in steps:
        mid = low + step

        if mid > high:
            continue

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Move to the right half
        else:
            high = mid - 1  # Move to the left half

    return -1  # Target not found


# Example usage:
arr = list(map(int, input().split(",")))
target = int(input())

index = uniform_binary_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")


# -------------------------------------------------------------------------------------------------------------------------------------------------
# Interpolation search
def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        # Avoid division by zero when arr[low] == arr[high]
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            else:
                return -1

        # Estimate the position using the interpolation formula
        pos = low + ((high - low) * (target - arr[low])) // (arr[high] - arr[low])

        print(f"Checking position {pos} with value {arr[pos]}")

        # Target found
        if arr[pos] == target:
            return pos
        # Target is in the right half
        elif arr[pos] < target:
            low = pos + 1
        # Target is in the left half
        else:
            high = pos - 1

    return -1  # Target not found


# Example usage:
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 70

index = interpolation_search(arr, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
#--------------------------------------------------------------------------------------------------------------------------------------