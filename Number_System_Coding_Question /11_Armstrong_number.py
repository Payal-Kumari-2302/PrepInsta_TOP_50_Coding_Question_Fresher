# Python Number System – 33 Coding Questions
# Q11 - Check Armstrong Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to check whether a
# given number is an Armstrong number.
#
# Example:
# 153 = 1**3 + 5**3 + 3**3 = 153

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
original = num
digits = len(str(num))
total = 0

if num < 0:
    print("Not an Armstrong Number")
else:
    while num > 0:
        digit = num % 10
        total = total + digit ** digits
        num = num // 10

    if total == original:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

# ==========================================
# Output
# ==========================================
# Input: 153
# Output: Armstrong Number

# Input: 123
# Output: Not an Armstrong Number

# Input: 0
# Output: Armstrong Number
