# String Reverser

## 🎯 Description
This beginner-level challenge focuses on basic string manipulation in C++. You'll implement a function that reverses a string, helping you understand string handling, iterators, and basic algorithms in modern C++.

## 🔍 Task
Write a function `std::string reverseString(const std::string& str)` that:
1. Takes a constant reference to a string as input
2. Returns a new string with characters in reverse order
3. Handles empty strings gracefully
4. Does not modify the original string

### Examples:
- `reverseString("hello")` should return `"olleh"`
- `reverseString("world")` should return `"dlrow"`
- `reverseString("")` should return `""`
- `reverseString("a")` should return `"a"`

## 📋 Requirements
- Function must be implemented in C++20
- Include proper header guards in header file
- Use `const` correctness
- Follow Google C++ Style Guide
- Use modern C++ features where appropriate
- Handle empty strings without errors

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Basic String Reversal
- `reverseString("hello")` should return `"olleh"`
- `reverseString("world")` should return `"dlrow"`
- `reverseString("C++")` should return `"++C"`

### 2. Edge Cases
- `reverseString("")` should return `""` (empty string)
- `reverseString("a")` should return `"a"` (single character)
- `reverseString("ab")` should return `"ba"` (two characters)

### 3. Special Characters and Numbers
- `reverseString("123")` should return `"321"`
- `reverseString("Hello, World!")` should return `"!dlroW ,olleH"`
- `reverseString("  spaces  ")` should return `"  secaps  "`

### 4. Palindromes
- `reverseString("racecar")` should return `"racecar"`
- `reverseString("level")` should return `"level"`

### 5. Longer Strings
- `reverseString("The quick brown fox")` should return `"xof nworb kciuq ehT"`

### 6. Return Type and Const Correctness
- Function should return `std::string` by value
- Input parameter should not be modified
- Function should work with string literals

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
- You can use `std::reverse()` from `<algorithm>` or implement your own reversal logic
- Consider using iterators for a modern C++ approach
- String construction from reverse iterators: `std::string(str.rbegin(), str.rend())`
- Alternative: manually swap characters from both ends
- Don't forget to include necessary headers (`<string>`, `<algorithm>` if needed)
- Remember that `const std::string&` prevents modification of the input
