# Python Number System – 33 Coding Questions
# Q7 - Factorial of a Number


# ==========================================
# Problem Statement
# ==========================================

# Take a non-negative integer as input.
# Calculate the factorial of the given number.
#
# Factorial = 1 * 2 * 3 * ... * n
#
# Example:
# Input: 5
# Output: 120


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

fact = 1

if num < 0:
    print("Factorial is not defined for negative numbers")

else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial:", fact)


# ==========================================
# Output
# ==========================================

# Input: 5
# Output: Factorial: 120

# Input: 0
# Output: Factorial: 1

# Input: -3
# Output: Factorial is not defined for negative numbers
