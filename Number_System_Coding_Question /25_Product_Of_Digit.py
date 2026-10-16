# Python Number System – 33 Coding Questions
# Q25 - Find the Product of Digits

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to calculate the product
# of all digits in a given integer.
#
# Example:
# Input: 234
# Output: 24
# Explanation: 2 * 3 * 4 = 24

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
num = abs(num)

product = 1

if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10
        product = product * digit
        num = num // 10

print("Product of Digits:", product)

# ==========================================
# Output
# ==========================================
# Input: 234
# Output: Product of Digits: 24
#
# Input: 1234
# Output: Product of Digits: 24
#
# Input: 105
# Output: Product of Digits: 0
#
# Input: 0
# Output: Product of Digits: 0
