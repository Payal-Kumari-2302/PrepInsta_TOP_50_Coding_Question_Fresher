# Python Number System – 33 Coding Questions
# Q17 - Print Prime Numbers in a Range

# ==========================================
# Problem Statement
# ==========================================
# Write a Python program to print all prime
# numbers between two given numbers.
#
# Example:
# Input: start = 10, end = 20
# Output: 11 13 17 19

# ==========================================
# Solution
# ==========================================
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime Numbers:")

for num in range(max(2, start), end + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")

# ==========================================
# Output
# ==========================================
# Input:
# Enter starting number: 10
# Enter ending number: 20
#
# Output:
# Prime Numbers:
# 11 13 17 19
