# Python Number System – 33 Coding Questions
# Q33 - Disarium Number

# ==========================================
# Problem Statement
# ==========================================
# A number is called a Disarium Number if the sum
# of its digits raised to their respective positions
# is equal to the original number.
#
# Example:
# 135 = 1¹ + 3² + 5³
#     = 1 + 9 + 125
#     = 135
#
# Therefore, 135 is a Disarium Number.

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))

if num < 0:
    print("Not a Disarium Number")
else:
    original = num
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        digit = int(digits[i])
        position = i + 1
        total = total + digit ** position

    if total == original:
        print("Disarium Number")
    else:
        print("Not a Disarium Number")

# ==========================================
# Output
# ==========================================
# Input: 135
# Output: Disarium Number
#
# Input: 123
# Output: Not a Disarium Number
