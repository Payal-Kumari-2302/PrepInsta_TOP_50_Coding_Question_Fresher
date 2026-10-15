# Python Number System – 33 Coding Questions
# Q6 - Check Leap Year


# ==========================================
# Problem Statement
# ==========================================

# Take a year as input.
# Check whether the given year is a leap year.
#
# Example:
# Input: 2024
# Output: Leap Year


# ==========================================
# Solution
# ==========================================

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not a Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not a Leap Year")


# ==========================================
# Output
# ==========================================

# Input: 2024
# Output: Leap Year

# Input: 1900
# Output: Not a Leap Year

# Input: 2000
# Output: Leap Year

# Input: 2025
# Output: Not a Leap Year
