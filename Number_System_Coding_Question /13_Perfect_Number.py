# Python Number System – 33 Coding Questions
# Q13 - Check Perfect Square

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to check whether
# a given number is a perfect square.
#
# Example:
# 25 = 5 * 5
# Therefore, 25 is a Perfect Square.

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))

if num < 0:
    print("Not a Perfect Square")
else:
    i = 0

    while i * i <= num:
        if i * i == num:
            print("Perfect Square")
            break
        i += 1
    else:
        print("Not a Perfect Square")

# ==========================================
# Output
# ==========================================
# Input: 25
# Output: Perfect Square

# Input: 20
# Output: Not a Perfect Square

# Input: 0
# Output: Perfect Square
