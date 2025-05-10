# Test Challenge

## 🎯 Description
This is a simple challenge to help you get familiar with the testing framework and submission process. You'll create a function that adds two numbers together and write tests to verify its functionality.

## 🔍 Task
Write a function `add_numbers(a: int, b: int) -> int` that:
1. Takes two integer parameters `a` and `b`
2. Returns their sum
3. Handles basic error cases

## 📋 Requirements
- Function must be implemented in Python 3.8+
- Include proper type hints
- Handle invalid input types

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Basic Addition Tests
- `add_numbers(2, 3)` should return `5`
- `add_numbers(-1, 1)` should return `0`
- `add_numbers(0, 0)` should return `0`

### 2. Large Number Tests
- `add_numbers(999999, 1)` should return `1000000`
- `add_numbers(-500000, 500000)` should return `0`

### 3. Negative Number Tests
- `add_numbers(-5, -7)` should return `-12`
- `add_numbers(-3, 10)` should return `7`

### 4. Type Checking Tests
- `add_numbers(1, 2)` should return an integer
- `add_numbers("1", 2)` should raise a TypeError
- `add_numbers(1.5, 2)` should raise a TypeError

## 📁 Files
- `solution.py` - Implement your solution here
- `test_main.py` - Contains the test cases **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `solution.py`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Consider edge cases in your implementation
- Follow PEP 8 style guidelines
- Make sure your function validates input types
