# Python Number System – 33 Coding Questions
# Q18 - Check Strong Number

# ==========================================
# Problem Statement
# ==========================================
# A Strong Number is a number whose sum of
# the factorials of its digits equals the number.
#
# Example:
# 145 = 1! + 4! + 5!
#     = 1 + 24 + 120
#     = 145
#
# Therefore, 145 is a Strong Number.

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
original = num
total = 0

if num < 0:
    print("Not a Strong Number")
else:
    while num > 0:
        digit = num % 10
        fact = 1

        for i in range(1, digit + 1):
            fact = fact * i

        total = total + fact
        num = num // 10

    if total == original:
        print("Strong Number")
    else:
        print("Not a Strong Number")

# ==========================================
# Output
# ==========================================
# Input: 145
# Output: Strong Number
#
# Input: 123
# Output: Not a Strong Number
#
# Input: 0
# Output: Not a Strong Number
