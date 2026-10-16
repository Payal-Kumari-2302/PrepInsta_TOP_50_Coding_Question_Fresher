# Python Number System – 33 Coding Questions
# Q15 - Check Happy Number

# ==========================================
# Problem Statement
# ==========================================
# A number is called a Happy Number if repeatedly
# replacing it with the sum of the squares of its
# digits eventually produces 1.
#
# Example:
# 19 -> 1² + 9² = 82
# 82 -> 8² + 2² = 68
# 68 -> 6² + 8² = 100
# 100 -> 1² + 0² + 0² = 1
#
# Therefore, 19 is a Happy Number.

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))
original = num
seen = set()

if num <= 0:
    print("Not a Happy Number")
else:
    while num != 1 and num not in seen:
        seen.add(num)
        total = 0

        while num > 0:
            digit = num % 10
            total = total + digit ** 2
            num = num // 10

        num = total

    if num == 1:
        print("Happy Number")
    else:
        print("Not a Happy Number")

# ==========================================
# Output
# ==========================================
# Input: 19
# Output: Happy Number
#
# Input: 2
# Output: Not a Happy Number
