# Python Number System – 33 Coding Questions
# Q32 - Fibonacci Using Recursion

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to print the Fibonacci
# series using recursion.
#
# Example:
# Input: 7
# Output: 0 1 1 2 3 5 8

# ==========================================
# Solution
# ==========================================
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter the number of terms: "))

if n < 0:
    print("Please enter a non-negative number")
else:
    for i in range(n):
        print(fibonacci(i), end=" ")

# ==========================================
# Output
# ==========================================
# Input: 7
# Output: 0 1 1 2 3 5 8
