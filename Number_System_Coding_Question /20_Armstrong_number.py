# Python Number System – 33 Coding Questions
# Q20 - Print Armstrong Numbers in a Range

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to print all Armstrong
# numbers between a given starting and ending number.
#
# Example:
# Input: 1 to 500
# Output: 1 2 3 4 5 6 7 8 9 153 370 371 407

# ==========================================
# Solution
# ==========================================
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Armstrong Numbers:")

for num in range(max(0, start), end + 1):
    original = num
    digits = len(str(num))
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == original:
        print(original, end=" ")

# ==========================================
# Output
# ==========================================
# Input:
# Enter starting number: 1
# Enter ending number: 500
#
# Output:
# Armstrong Numbers:
# 1 2 3 4 5 6 7 8 9 153 370 371 407
