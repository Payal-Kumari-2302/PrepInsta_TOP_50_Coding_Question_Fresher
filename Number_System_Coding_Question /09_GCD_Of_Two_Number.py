# Python Number System – 33 Coding Questions
# Q9 - Find GCD / HCF of Two Numbers


# ==========================================
# Problem Statement
# ==========================================

# Take two positive integers as input.
# Find their Greatest Common Divisor (GCD).
#
# Example:
# Input:
# 36
# 60
#
# Output: 12


# ==========================================
# Solution
# ==========================================

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(num1, num2) + 1):

    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD:", gcd)


# ==========================================
# Output
# ==========================================

# Input:
# 36
# 60

# Output:
# GCD: 12
