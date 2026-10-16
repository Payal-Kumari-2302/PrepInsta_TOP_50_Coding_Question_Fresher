# Python Number System – 33 Coding Questions
# Q31 - Check Palindrome Number

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to check whether a
# number is a Palindrome Number or not.
#
# Example:
# 121 -> Palindrome Number
# 123 -> Not a Palindrome Number

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))

if num < 0:
    print("Not a Palindrome Number")
else:
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if original == reverse:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")

# ==========================================
# Output
# ==========================================
# Input: 121
# Output: Palindrome Number
#
# Input: 123
# Output: Not a Palindrome Number
#
# Input: 0
# Output: Palindrome Number
