# Python Number System – 33 Coding Questions
# Q5 - Check Prime Number


# ==========================================
# Problem Statement
# ==========================================

# Take an integer as input.
# Check whether it is a prime number.
#
# A prime number has exactly two positive divisors:
# 1 and the number itself.
#
# Example:
# Input: 7
# Output: Prime Number


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

if num < 2:
    print("Not a Prime Number")

else:
    for i in range(2, num):

        if num % i == 0:
            print("Not a Prime Number")
            break

    else:
        print("Prime Number")


# ==========================================
# Output
# ==========================================

# Input: 7
# Output: Prime Number

# Input: 10
# Output: Not a Prime Number

# Input: 1
# Output: Not a Prime Number
