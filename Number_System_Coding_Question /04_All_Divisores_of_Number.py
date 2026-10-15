# Python Number System – 33 Coding Questions
# Q4 - Find All Divisors of a Number


# ==========================================
# Problem Statement
# ==========================================

# Take a positive integer as input.
# Print all positive divisors of the given number.
#
# Example:
# Input: 12
# Output: 1 2 3 4 6 12


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

for i in range(1, num + 1):

    if num % i == 0:
        print(i, end=" ")


# ==========================================
# Output
# ==========================================

# Input: 12
# Output: 1 2 3 4 6 12
