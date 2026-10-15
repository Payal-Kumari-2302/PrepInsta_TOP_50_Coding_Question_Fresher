# Python Number System – 33 Coding Questions
# Q3 - Sum of Digits


# ==========================================
# Problem Statement
# ==========================================

# Take an integer as input.
# Calculate the sum of all its digits.
#
# Example:
# Input: 1234
# Output: 10


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of Digits:", total)


# ==========================================
# Output
# ==========================================

# Input: 1234
# Output: Sum of Digits: 10
