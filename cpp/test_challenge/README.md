# Test Challenge

## 🎯 Description
This is a simple challenge to help you get familiar with the C++ testing framework and submission process. You'll create a function that adds two numbers together and write tests to verify its functionality.

## 🔍 Task
Write a function `int add_numbers(int a, int b)` that:
1. Takes two integer parameters `a` and `b`
2. Returns their sum
3. Handles basic error cases

## 📋 Requirements
- Function must be implemented in C++20
- Include proper header guards
- Use appropriate C++ standard library features
- Handle potential integer overflow cases

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

### 4. Edge Cases
- `add_numbers(INT_MAX, 1)` should handle overflow appropriately
- `add_numbers(INT_MIN, -1)` should handle underflow appropriately

## 📁 Files
- `solution.hpp` - Declare your function interface here
- `solution.cpp` - Implement your solution here
- `test.cpp` - Contains the test cases **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `solution.hpp` and `solution.cpp`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Consider using `#pragma once` or include guards in your header file
- Follow modern C++ best practices
- Consider using `constexpr` if appropriate
- Make sure to handle integer overflow cases
- Follow the Google C++ Style Guide for consistency

## 🛠️ Building and Testing
To build and test your solution:

```bash
mkdir build
cd build
cmake ..
cmake --build .
ctest
```

## 📚 Resources
- [GoogleTest Documentation](https://google.github.io/googletest/)
- [C++20 Reference](https://en.cppreference.com/w/cpp/20)
- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
