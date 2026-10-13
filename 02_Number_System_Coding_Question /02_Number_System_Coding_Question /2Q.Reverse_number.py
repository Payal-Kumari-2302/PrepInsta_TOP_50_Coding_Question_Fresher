```python
# ==================================================
# Q2. Reverse a Number
# ==================================================


# 📌 Problem Statement
#
# Write a Python program to reverse the digits
# of a given integer.


# 📝 Example
#
# Input: 12345
# Output: 54321


# ==========================================
# SOLUTION
# ==========================================

n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print(rev)
```
