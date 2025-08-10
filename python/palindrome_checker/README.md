# Palindrome Checker

## 🎯 Description
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. This challenge will help you practice string manipulation and algorithmic thinking by implementing a function that checks if a string is a palindrome.

## 🔍 Task
Write a function `is_palindrome(s: str) -> bool` that:
1. Takes a string parameter `s`
2. Returns `True` if the string is a palindrome, `False` otherwise
3. Ignores case differences (e.g., "Aa" should be considered a palindrome)
4. Ignores non-alphanumeric characters (spaces, punctuation, etc.)

## 📋 Requirements
- Function must be implemented in Python 3.8+
- Include proper type hints
- Follow PEP 8 style guidelines
- Handle empty strings gracefully
- Only consider alphanumeric characters for palindrome checking

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Basic Palindrome Tests
- `is_palindrome("racecar")` should return `True`
- `is_palindrome("hello")` should return `False`
- `is_palindrome("A")` should return `True`
- `is_palindrome("")` should return `True`

### 2. Case Insensitive Tests
- `is_palindrome("Racecar")` should return `True`
- `is_palindrome("MadAm")` should return `True`
- `is_palindrome("NoLemon")` should return `False`

### 3. Alphanumeric Tests
- `is_palindrome("A man a plan a canal Panama")` should return `True`
- `is_palindrome("race a car")` should return `False`
- `is_palindrome("Was it a car or a cat I saw?")` should return `True`

### 4. Special Cases
- `is_palindrome("12321")` should return `True`
- `is_palindrome("12345")` should return `False`
- `is_palindrome("Madam123321madaM")` should return `True`
- `is_palindrome("!@#$%^&*()")` should return `True` (no alphanumeric characters)

### 5. Type Validation Tests
- Function should raise `TypeError` for non-string inputs

## 📁 Files
- `solution.py` - Implement your solution here
- `test_main.py` - Contains the test cases **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `solution.py`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Consider using Python's built-in string methods like `isalnum()` and `lower()`
- Think about how to efficiently compare characters from both ends of the string
- Remember that empty strings are considered palindromes by convention
