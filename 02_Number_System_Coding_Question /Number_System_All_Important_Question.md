# 🐍 Python Number System – 20 Coding Questions

## 🎯 Objective

Practice Number System coding questions for BCA placement preparation using Python.

* **Level:** Beginner to Intermediate
* **Language:** Python
* **Purpose:** Placement Preparation
* **Total Questions:** 20

## 📌 Instructions

1. Try to solve every question yourself before looking at a solution.
2. Write clean and readable Python code.
3. Test your code with different inputs.
4. Use loops, conditions and operators wherever appropriate.
5. Save each solution in a separate `.py` file.
6. Mark each question as completed after testing your code.

---

# ⭐ Priority 1 – Must Practice First

## Q1. Check Positive, Negative, Odd, Even or Zero

**Problem Statement:**
Write a Python program to determine whether an integer is positive, negative, or zero. If it is not zero, also determine whether it is odd or even.

**Example:**

```text
Input: 10
Output: Positive, Even
```

**Instructions:**

* Take an integer as input.
* Check whether the number is positive, negative, or zero.
* If it is not zero, check whether it is odd or even.

---

## Q2. Reverse a Number

**Problem Statement:**
Write a Python program to reverse the digits of a given integer.

**Example:**

```text
Input: 12345
Output: 54321
```

**Instructions:**

* Take an integer as input.
* Extract the last digit using `%`.
* Build the reversed number.
* Remove the last digit using `//`.

---

## Q3. Find the Sum of Digits of a Number

**Problem Statement:**
Write a Python program to calculate the sum of all digits of a given integer.

**Example:**

```text
Input: 1234
Output: 10
```

**Instructions:**

* Take an integer as input.
* Extract each digit.
* Add the digits to a sum variable.
* Repeat until all digits have been processed.

---

## Q4. Find All Divisors of a Number

**Problem Statement:**
Write a Python program to print all positive divisors of a given positive integer.

**Example:**

```text
Input: 12
Output: 1 2 3 4 6 12
```

**Instructions:**

* Take a positive integer as input.
* Use a loop from `1` to the given number.
* Check which numbers divide it completely.
* Print all divisors.

---

## Q5. Check Whether a Number Is Prime

**Problem Statement:**
Write a Python program to determine whether a given integer is a prime number.

**Example:**

```text
Input: 7
Output: Prime Number
```

**Instructions:**

* Take an integer as input.
* A prime number has exactly two positive divisors.
* Check whether any number other than `1` and itself divides it.
* Numbers less than `2` are not prime.

---

## Q6. Check Whether a Year Is a Leap Year

**Problem Statement:**
Write a Python program to determine whether a given year is a leap year.

**Example:**

```text
Input: 2024
Output: Leap Year
```

**Instructions:**

* Take a year as input.
* A year divisible by `400` is a leap year.
* A year divisible by `100` but not by `400` is not a leap year.
* Other years divisible by `4` are leap years.

---

## Q7. Find the Factorial of a Number

**Problem Statement:**
Write a Python program to calculate the factorial of a non-negative integer.

**Example:**

```text
Input: 5
Output: 120
```

**Instructions:**

* Take a non-negative integer as input.
* Initialize a variable to store the factorial.
* Multiply the numbers from `1` to the given number.
* Remember that `0! = 1`.

---

## Q8. Print the Fibonacci Series

**Problem Statement:**
Write a Python program to print the first `N` terms of the Fibonacci series.

**Example:**

```text
Input: 7
Output: 0 1 1 2 3 5 8
```

**Instructions:**

* Take the number of terms as input.
* Start with `0` and `1`.
* Print each term.
* Calculate the next term by adding the previous two terms.
* Continue until `N` terms have been printed.

---

## Q9. Find the Greatest Common Divisor (GCD)

**Problem Statement:**
Write a Python program to find the greatest common divisor of two positive integers.

**Example:**

```text
Input:
36
60

Output: 12
```

**Instructions:**

* Take two positive integers as input.
* Find the common divisors of both numbers.
* Identify the greatest common divisor.
* Try solving the problem using a loop.

---

## Q10. Check Whether a Number Is Perfect

**Problem Statement:**
Write a Python program to determine whether a positive integer is a perfect number.

**Example:**

```text
Input: 28
Output: Perfect Number
```

**Instructions:**

* Take a positive integer as input.
* Find its proper divisors, excluding the number itself.
* Calculate their sum.
* Compare the sum with the original number.

---

## Q11. Check Whether a Number Is Armstrong

**Problem Statement:**
Write a Python program to determine whether a non-negative integer is an Armstrong number.

**Example:**

```text
Input: 153
Output: Armstrong Number
```

**Instructions:**

* Take a non-negative integer as input.
* Count the digits.
* Raise each digit to the power of the total number of digits.
* Calculate the sum.
* Compare the sum with the original number.

---

# ⭐ Priority 2 – Important Practice

## Q12. Check Whether a Number Is a Valid Perfect Square

**Problem Statement:**
Write a Python program to determine whether a given non-negative integer is a perfect square.

**Example:**

```text
Input: 49
Output: Perfect Square
```

**Instructions:**

* Take a non-negative integer as input.
* Find its integer square root or check possible square values.
* Determine whether an integer multiplied by itself equals the given number.
* Handle `0` correctly.

---

## Q13. Replace All Zeros with Fives in an Integer

**Problem Statement:**
Write a Python program to replace every occurrence of the digit `0` with `5` in a given integer.

**Example:**

```text
Input: 1020
Output: 1525
```

**Instructions:**

* Take an integer as input.
* Identify every digit that is `0`.
* Replace each zero with `5`.
* Preserve the order of the other digits.

---

## Q14. Find the Sum of the First N Natural Numbers

**Problem Statement:**
Write a Python program to calculate the sum of the first `N` natural numbers.

**Example:**

```text
Input: 5
Output: 15
```

**Instructions:**

* Take a non-negative integer `N` as input.
* Use a loop to add the natural numbers from `1` to `N`.
* Display the final sum.
* For `N = 0`, the sum should be `0`.

---

## Q15. Convert a Number to Hexadecimal

**Problem Statement:**
Write a Python program to convert a non-negative decimal integer into its hexadecimal representation.

**Example:**

```text
Input: 26
Output: 1A
```

**Instructions:**

* Take a non-negative decimal integer as input.
* Understand how hexadecimal uses digits `0–9` and letters `A–F`.
* Convert the number to base 16.
* Display the hexadecimal representation.

---

## Q16. Check Whether a Number Is a Happy Number

**Problem Statement:**
Write a Python program to determine whether a positive integer is a happy number.

**Example:**

```text
Input: 19
Output: Happy Number
```

**Instructions:**

* Take a positive integer as input.
* Calculate the square of each digit.
* Add the squares together.
* Repeat the process with the resulting number.
* If the process reaches `1`, it is a happy number.
* If a number repeats without reaching `1`, it is not a happy number.

---

## Q17. Add Two Fractions

**Problem Statement:**
Write a Python program to add two fractions and express the result in its simplest form.

**Example:**

```text
Input:
1 2
1 3

Output: 5/6
```

Here, the inputs represent `1/2` and `1/3`.

**Instructions:**

* Take the numerators and denominators of both fractions as input.
* Calculate the sum of the fractions.
* Find the greatest common divisor of the resulting numerator and denominator.
* Simplify the final fraction.
* Assume the denominators are non-zero.

---

## Q18. Find the Roots of a Quadratic Equation

**Problem Statement:**
Write a Python program to calculate the roots of a quadratic equation of the form:

`ax² + bx + c = 0`

**Example:**

```text
Input:
1
-5
6

Output:
2
3
```

**Instructions:**

* Take the coefficients `a`, `b` and `c` as input.
* Calculate the discriminant using `b² - 4ac`.
* Determine whether the roots are real and distinct, real and equal, or complex.
* Assume `a` is not zero.

---

# ⭐ Priority 3 – Additional Practice

## Q19. Find the Number of Ways to Arrange N Persons Around a Circular Table

**Problem Statement:**
Write a Python program to calculate the number of distinct arrangements of `N` different people around a circular table.

**Example:**

```text
Input: 4
Output: 6
```

**Instructions:**

* Take a positive integer `N` as input.
* Understand circular permutations.
* Use the formula `(N - 1)!` for `N` distinct people.
* Calculate and display the result.

---

## Q20. Generate the Fibonacci Series Using Recursion

**Problem Statement:**
Write a Python program to generate Fibonacci numbers using a recursive function.

**Example:**

```text
Input: 7
Output: 0 1 1 2 3 5 8
```

**Instructions:**

* Create a recursive function to calculate Fibonacci numbers.
* Define the base cases.
* Calculate each subsequent term using the previous two terms.
* Print the first `N` terms.
* Be aware that the basic recursive method becomes slow for large values of `N`.

---

# ✅ Progress Tracker

* [ ] Q1 – Positive, Negative, Odd, Even or Zero
* [ ] Q2 – Reverse a Number
* [ ] Q3 – Sum of Digits
* [ ] Q4 – All Divisors
* [ ] Q5 – Prime Number
* [ ] Q6 – Leap Year
* [ ] Q7 – Factorial
* [ ] Q8 – Fibonacci Series
* [ ] Q9 – GCD
* [ ] Q10 – Perfect Number
* [ ] Q11 – Armstrong Number
* [ ] Q12 – Valid Perfect Square
* [ ] Q13 – Replace Zeros with Fives
* [ ] Q14 – Sum of First N Natural Numbers
* [ ] Q15 – Decimal to Hexadecimal
* [ ] Q16 – Happy Number
* [ ] Q17 – Add Two Fractions
* [ ] Q18 – Roots of a Quadratic Equation
* [ ] Q19 – Circular Permutations
* [ ] Q20 – Fibonacci Using Recursion

---

## 🚀 My Practice Rule

**Understand → Try Yourself → Test Your Code → Review Mistakes → Upload to GitHub**

*Consistency is the key to improving coding skills and preparing for placements.*
