# Python Number System – 33 Coding Questions
# Q19 - Find Prime Factors of a Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to find all prime
# factors of a given positive integer.
#
# Example:
# Input: 12
# Output: 2 2 3
#
# Because: 12 = 2 * 2 * 3

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))

if num < 2:
    print("No Prime Factors")
else:
    print("Prime Factors:")

    divisor = 2

    while num > 1:
        if num % divisor == 0:
            print(divisor, end=" ")
            num = num // divisor
        else:
            divisor += 1

# ==========================================
# Output
# ==========================================
# Input: 12
# Output: Prime Factors:
#         2 2 3
#
# Input: 30
# Output: Prime Factors:
#         2 3 5
