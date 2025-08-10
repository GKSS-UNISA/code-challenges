# Factorial Calculator

## 🎯 Description
The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. This challenge will help you understand recursive thinking, mathematical computation, and proper error handling in Python.

## 🔍 Task
Write a function `factorial(n: int) -> int` that:
1. Takes a non-negative integer parameter `n`
2. Returns the factorial of `n` (n!)
3. Handles the special case where 0! = 1
4. Raises appropriate exceptions for invalid inputs

Mathematical definition:
- 0! = 1
- n! = n × (n-1) × (n-2) × ... × 2 × 1 for n > 0

## 📋 Requirements
- Function must be implemented in Python 3.8+
- Include proper type hints
- Follow PEP 8 style guidelines
- Raise `ValueError` for negative integers
- Raise `TypeError` for non-integer inputs
- Must handle large factorials efficiently

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Basic Factorial Tests
- `factorial(0)` should return `1`
- `factorial(1)` should return `1`
- `factorial(5)` should return `120`
- `factorial(10)` should return `3628800`

### 2. Edge Cases
- `factorial(2)` should return `2`
- `factorial(3)` should return `6`
- `factorial(4)` should return `24`

### 3. Large Numbers
- `factorial(20)` should return `2432902008176640000`
- `factorial(15)` should return `1307674368000`

### 4. Error Handling
- `factorial(-1)` should raise `ValueError`
- `factorial(-5)` should raise `ValueError`
- `factorial(3.5)` should raise `TypeError`
- `factorial("5")` should raise `TypeError`
- `factorial(None)` should raise `TypeError`

### 5. Return Type Tests
- The function should always return an integer for valid inputs

## 📁 Files
- `solution.py` - Implement your solution here
- `test_main.py` - Contains the test cases **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `solution.py`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- You can implement this iteratively or recursively
- Remember that 0! = 1 by mathematical convention
- Python's `int` type can handle arbitrarily large numbers
- Consider input validation before computation
- For large numbers, iterative solutions may be more efficient than recursive ones
