# Python Number System – 33 Coding Questions
# Q23 - Find the Sum of Even Digits

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to calculate the sum
# of all even digits in a given integer.
#
# Example:
# Input: 123456
# Output: 12
# Explanation: 2 + 4 + 6 = 12

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

total = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        total = total + digit

    num = num // 10

print("Sum of Even Digits:", total)

# ==========================================
# Output
# ==========================================
# Input: 123456
# Output: Sum of Even Digits: 12
#
# Input: 13579
# Output: Sum of Even Digits: 0
#
# Input: 2468
# Output: Sum of Even Digits: 20
#
# Input: 0
# Output: Sum of Even Digits: 0
