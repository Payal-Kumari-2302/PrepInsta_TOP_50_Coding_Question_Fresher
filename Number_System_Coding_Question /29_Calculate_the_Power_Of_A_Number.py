# Python Number System – 33 Coding Questions
# Q29 - Calculate the Power of a Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to calculate the power
# of a number without using the ** operator.
#
# Example:
# Base = 2, Exponent = 5
# Result = 2 * 2 * 2 * 2 * 2 = 32

# ==========================================
# Solution
# ==========================================
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = 1

if exponent < 0:
    if base == 0:
        print("Undefined result")
    else:
        for i in range(abs(exponent)):
            result = result * base

        result = 1 / result
        print("Result:", result)
else:
    for i in range(exponent):
        result = result * base

    print("Result:", result)

# ==========================================
# Output
# ==========================================
# Input:
# Enter the base: 2
# Enter the exponent: 5
#
# Output:
# Result: 32
#
# Input:
# Enter the base: 3
# Enter the exponent: 4
#
# Output:
# Result: 81
