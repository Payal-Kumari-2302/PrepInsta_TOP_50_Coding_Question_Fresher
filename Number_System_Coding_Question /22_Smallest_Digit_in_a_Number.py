# Python Number System – 33 Coding Questions
# Q22 - Find the Smallest Digit in a Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to find the smallest
# digit in a given integer.
#
# Example:
# Input: 5832
# Output: 2

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

smallest = 9

if num == 0:
    smallest = 0
else:
    while num > 0:
        digit = num % 10

        if digit < smallest:
            smallest = digit

        num = num // 10

print("Smallest Digit:", smallest)

# ==========================================
# Output
# ==========================================
# Input: 5832
# Output: Smallest Digit: 2
#
# Input: 7294
# Output: Smallest Digit: 2
#
# Input: 0
# Output: Smallest Digit: 0
