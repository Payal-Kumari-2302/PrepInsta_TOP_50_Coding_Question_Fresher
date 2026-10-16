# Python Number System – 33 Coding Questions
# Q28 - Replace All Zeros with Fives

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to replace every
# zero in a number with the digit five.
#
# Example:
# Input: 1020
# Output: 1525

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))

if num < 0:
    sign = -1
    num = abs(num)
else:
    sign = 1

if num == 0:
    result = 5
else:
    result = int(str(num).replace("0", "5"))

result = result * sign

print("Number after replacement:", result)

# ==========================================
# Output
# ==========================================
# Input: 1020
# Output: Number after replacement: 1525
#
# Input: 9003
# Output: Number after replacement: 9553
#
# Input: 0
# Output: Number after replacement: 5
