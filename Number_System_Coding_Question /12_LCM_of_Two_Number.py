# Python Number System – 33 Coding Questions
# Q12 - Find LCM of Two Numbers

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to find the LCM
# (Least Common Multiple) of two numbers.
#
# Example:
# 12 and 18
# LCM = 36

# ==========================================
# Solution
# ==========================================
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == 0 or num2 == 0:
    print("LCM: 0")
else:
    a = abs(num1)
    b = abs(num2)
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            print("LCM:", greater)
            break
        greater += 1

# ==========================================
# Output
# ==========================================
# Input:
# Enter first number: 12
# Enter second number: 18
# Output:
# LCM: 36
