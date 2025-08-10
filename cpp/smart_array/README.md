# Smart Pointer Array

## 🎯 Description
This advanced challenge focuses on implementing a dynamic array class using modern C++ memory management techniques. You'll create a template class that manages memory automatically and provides safe, efficient array operations.

## 🔍 Task
Implement a `SmartArray<T>` template class that manages a dynamic array of elements.

### Class Requirements:

#### Template Declaration
```cpp
template<typename T>
class SmartArray
```

#### Constructor and Destructor
- `SmartArray(size_t initial_capacity = 10)` - Initialize with capacity
- `SmartArray(const SmartArray& other)` - Copy constructor
- `SmartArray& operator=(const SmartArray& other)` - Copy assignment
- `~SmartArray()` - Destructor

#### Core Methods
1. `void push_back(const T& element)` - Add element to end
2. `void pop_back()` - Remove last element
3. `T& at(size_t index)` - Access element with bounds checking
4. `const T& at(size_t index) const` - Const version of at()
5. `size_t size() const` - Return number of elements
6. `size_t capacity() const` - Return current capacity
7. `bool empty() const` - Check if array is empty
8. `void clear()` - Remove all elements

#### Operators
1. `T& operator[](size_t index)` - Array subscript operator
2. `const T& operator[](size_t index) const` - Const version

## 📋 Requirements
- Must be a template class working with any type T
- Automatic memory management (no memory leaks)
- Dynamic resizing when capacity is exceeded
- Exception safety for bounds checking
- Rule of Three implementation
- Modern C++ features (C++20)

## 📁 Files
- `include/solution.h` - Declare your template class here
- `solution.cpp` - Template implementations (if needed)
- `test.cpp` - Contains the test cases **DO NOT EDIT**
- `CMakeLists.txt` - Build configuration **DO NOT EDIT**
