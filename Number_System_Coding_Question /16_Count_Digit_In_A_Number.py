# Python Number System – 33 Coding Questions
# Q16 - Count Digits in a Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to count the number
# of digits in a given integer.
#
# Example:
# Input: 12345
# Output: 5

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        digit = num % 10
        count += 1
        num = num // 10

print("Number of Digits:", count)

# ==========================================
# Output
# ==========================================
# Input: 12345
# Output: Number of Digits: 5
#
# Input: 708
# Output: Number of Digits: 3
#
# Input: 0
# Output: Number of Digits: 1
#
# Input: -123
# Output: Number of Digits: 3
