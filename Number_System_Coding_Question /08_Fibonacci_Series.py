# Python Number System – 33 Coding Questions
# Q8 - Print the Fibonacci Series


# ==========================================
# Problem Statement
# ==========================================

# Take the number of terms as input.
# Print the first N terms of the Fibonacci series.
#
# Each term is the sum of the previous two terms.
#
# Example:
# Input: 7
# Output: 0 1 1 2 3 5 8


# ==========================================
# Solution
# ==========================================

n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")

    a, b = b, a + b


# ==========================================
# Output
# ==========================================

# Input: 7
# Output: 0 1 1 2 3 5 8
