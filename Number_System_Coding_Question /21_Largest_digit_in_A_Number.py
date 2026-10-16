# Python Number System – 33 Coding Questions
# Q21 - Find the Largest Digit in a Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to find the largest
# digit in a given integer.
#
# Example:
# Input: 5832
# Output: 8

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

largest = 0

while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

print("Largest Digit:", largest)

# ==========================================
# Output
# ==========================================
# Input: 5832
# Output: Largest Digit: 8
#
# Input: 7294
# Output: Largest Digit: 9
#
# Input: 0
# Output: Largest Digit: 0
