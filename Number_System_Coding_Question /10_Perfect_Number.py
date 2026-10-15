# Python Number System – 33 Coding Questions
# Q10 - Check Perfect Number


# ==========================================
# Problem Statement
# ==========================================

# Take a positive integer as input.
# Check whether it is a perfect number.
#
# A perfect number equals the sum of its proper divisors.
#
# Example:
# Input: 28
# Output: Perfect Number


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

total = 0

for i in range(1, num):
    if num % i == 0:
        total = total + i

if num > 0 and total == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# ==========================================
# Output
# ==========================================

# Input: 28
# Output: Perfect Number

# Input: 12
# Output: Not a Perfect Number
