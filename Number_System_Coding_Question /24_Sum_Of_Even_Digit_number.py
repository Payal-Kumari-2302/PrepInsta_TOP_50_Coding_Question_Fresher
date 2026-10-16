# Python Number System – 33 Coding Questions
# Q24 - Find the Sum of Odd Digits

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to calculate the sum
# of all odd digits in a given integer.
#
# Example:
# Input: 123456
# Output: 9
# Explanation: 1 + 3 + 5 = 9

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

total = 0

while num > 0:
    digit = num % 10

    if digit % 2 != 0:
        total = total + digit

    num = num // 10

print("Sum of Odd Digits:", total)

# ==========================================
# Output
# ==========================================
# Input: 123456
# Output: Sum of Odd Digits: 9
#
# Input: 2468
# Output: Sum of Odd Digits: 0
#
# Input: 13579
# Output: Sum of Odd Digits: 25
