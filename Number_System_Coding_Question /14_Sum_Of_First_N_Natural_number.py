# Python Number System – 33 Coding Questions
# Q14 - Sum of First N Natural Numbers

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to calculate the sum
# of the first N natural numbers.
#
# Example:
# N = 5
# Sum = 1 + 2 + 3 + 4 + 5 = 15

# ==========================================
# Solution
# ==========================================
n = int(input("Enter a number: "))

if n < 1:
    print("Enter a positive integer")
else:
    total = 0

    for i in range(1, n + 1):
        total = total + i

    print("Sum:", total)

# ==========================================
# Output
# ==========================================
# Input: 5
# Output: Sum: 15
#
# Input: 10
# Output: Sum: 55
