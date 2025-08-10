# Prime Number Checker

## 🎯 Description
This beginner challenge focuses on implementing mathematical algorithms in C++. You'll create a function that determines whether a given positive integer is a prime number, helping you practice loops, conditionals, and algorithm optimization.

## 🔍 Task
Write a function `bool isPrime(int n)` that:
1. Takes a positive integer as input
2. Returns `true` if the number is prime, `false` otherwise
3. Handles edge cases appropriately (numbers ≤ 1 are not prime)
4. Uses an efficient algorithm for checking primality

### Mathematical Background:
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Examples:
- `isPrime(2)` should return `true` (smallest prime)
- `isPrime(17)` should return `true`
- `isPrime(4)` should return `false` (4 = 2 × 2)
- `isPrime(1)` should return `false` (by definition)

## 📋 Requirements
- Function must be implemented in C++20
- Include proper header guards in header file
- Use efficient algorithm (don't check all numbers up to n)
- Handle negative numbers and edge cases appropriately
- Follow Google C++ Style Guide
- Use appropriate data types

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Basic Prime Numbers
- `isPrime(2)` should return `true` (smallest prime)
- `isPrime(3)` should return `true`
- `isPrime(5)` should return `true`
- `isPrime(7)` should return `true`
- `isPrime(11)` should return `true`

### 2. Basic Composite Numbers
- `isPrime(4)` should return `false` (2 × 2)
- `isPrime(6)` should return `false` (2 × 3)
- `isPrime(8)` should return `false` (2 × 4)
- `isPrime(9)` should return `false` (3 × 3)
- `isPrime(10)` should return `false` (2 × 5)

### 3. Edge Cases
- `isPrime(0)` should return `false`
- `isPrime(1)` should return `false`
- `isPrime(-5)` should return `false`
- `isPrime(-1)` should return `false`

### 4. Larger Prime Numbers
- `isPrime(13)` should return `true`
- `isPrime(17)` should return `true`
- `isPrime(19)` should return `true`
- `isPrime(23)` should return `true`
- `isPrime(29)` should return `true`

### 5. Larger Composite Numbers
- `isPrime(15)` should return `false` (3 × 5)
- `isPrime(21)` should return `false` (3 × 7)
- `isPrime(25)` should return `false` (5 × 5)
- `isPrime(27)` should return `false` (3 × 9)

### 6. Performance Test Cases
- `isPrime(97)` should return `true` (larger prime)
- `isPrime(100)` should return `false` (2 × 50)
- `isPrime(101)` should return `true` (larger prime)

### 7. Return Type Validation
- Function should return `bool` type
- Should work with different integer inputs

## 📁 Files
- `include/solution.h` - Declare your function here
- `solution.cpp` - Implement your solution here
- `test.cpp` - Contains the test cases **DO NOT EDIT**
- `CMakeLists.txt` - Build configuration **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `include/solution.h` and `solution.cpp`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- You only need to check divisors up to √n (square root of n)
- You can skip even numbers after checking for divisibility by 2
- Consider using a loop starting from 3 and incrementing by 2
- Include `<cmath>` if you want to use `sqrt()` function
- Remember that 2 is the only even prime number
- For efficiency: `for (int i = 3; i * i <= n; i += 2)`
- Handle the special case of 2 separately from other numbers
