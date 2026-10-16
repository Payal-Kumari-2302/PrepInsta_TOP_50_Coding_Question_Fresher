# Python Number System – 33 Coding Questions
# Q30 - Add Two Fractions

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to add two fractions
# and simplify the resulting fraction.
#
# Example:
# 1/2 + 1/3 = 5/6

# ==========================================
# Solution
# ==========================================
from math import gcd

num1 = int(input("Enter first numerator: "))
den1 = int(input("Enter first denominator: "))

num2 = int(input("Enter second numerator: "))
den2 = int(input("Enter second denominator: "))

if den1 == 0 or den2 == 0:
    print("Denominator cannot be zero")
else:
    numerator = num1 * den2 + num2 * den1
    denominator = den1 * den2

    common = gcd(abs(numerator), abs(denominator))

    numerator = numerator // common
    denominator = denominator // common

    if denominator < 0:
        numerator = -numerator
        denominator = -denominator

    print("Sum:", numerator, "/", denominator)

# ==========================================
# Output
# ==========================================
# Input:
# First numerator: 1
# First denominator: 2
# Second numerator: 1
# Second denominator: 3
#
# Output:
# Sum: 5 / 6
