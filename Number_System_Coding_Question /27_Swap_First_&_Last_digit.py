# Python Number System – 33 Coding Questions
# Q27 - Swap First and Last Digit

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to swap the first
# and last digits of a given positive integer.
#
# Example:
# Input: 12345
# Output: 52341

# ==========================================
# Solution
# ==========================================
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative integer")
else:
    digits = str(num)

    if len(digits) == 1:
        result = num
    else:
        result = digits[-1] + digits[1:-1] + digits[0]
        result = int(result)

    print("Number after swapping:", result)

# ==========================================
# Output
# ==========================================
# Input: 12345
# Output: Number after swapping: 52341
#
# Input: 9876
# Output: Number after swapping: 6879
#
# Input: 7
# Output: Number after swapping: 7
