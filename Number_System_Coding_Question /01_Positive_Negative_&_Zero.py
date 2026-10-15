# Q1 - Check Positive, Negative, Odd, Even or Zero


# ==========================================
# Problem Statement
# ==========================================

# Take an integer as input.
# Check whether the number is positive, negative, or zero.
# If it is not zero, also check whether it is odd or even.


# ==========================================
# Solution
# ==========================================

num = int(input("Enter a number: "))

if num > 0:

    if num % 2 == 0:
        print("Positive, Even")

    else:
        print("Positive, Odd")

elif num < 0:

    if num % 2 == 0:
        print("Negative, Even")

    else:
        print("Negative, Odd")

else:
    print("Zero")



# ==========================================
# Output
# ==========================================

# Input: 10
# Output: Positive, Even

# Input: -7
# Output: Negative, Odd

# Input: 0
# Output: Zero
