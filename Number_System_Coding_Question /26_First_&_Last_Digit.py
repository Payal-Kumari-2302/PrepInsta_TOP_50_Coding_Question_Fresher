# Python Number System – 33 Coding Questions
# Q26 - Find First and Last Digit

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to find the first
# and last digits of a given integer.
#
# Example:
# Input: 5832
# Output:
# First Digit: 5
# Last Digit: 2

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

last_digit = num % 10

while num >= 10:
    num = num // 10

first_digit = num

print("First Digit:", first_digit)
print("Last Digit:", last_digit)

# ==========================================
# Output
# ==========================================
# Input: 5832
# Output:
# First Digit: 5
# Last Digit: 2
#
# Input: 7
# Output:
# First Digit: 7
# Last Digit: 7
#
# Input: 0
# Output:
# First Digit: 0
# Last Digit: 0
