# Python Number System – 33 Coding Questions
# Q2 - Reverse a Number


# ==========================================
# Problem Statement
# ==========================================

# Take an integer as input and reverse its digits.
#
# Example:
# Input: 12345
# Output: 54321


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed Number:", reverse)


# ==========================================
# Output
# ==========================================

# Input: 12345
# Output: Reversed Number: 54321
