# Vector Math Library

## 🎯 Description
This intermediate challenge focuses on implementing a 2D vector mathematics library in C++. You'll practice class design, operator overloading, and mathematical computations while creating a useful utility class for graphics and physics applications.

## 🔍 Task
Implement a `Vector2D` class that represents a 2D vector with x and y components, along with common vector operations.

### Class Requirements:

#### Constructor
- `Vector2D(double x = 0.0, double y = 0.0)` - Initialize with x and y components

#### Public Member Variables
- `double x` - X component of the vector
- `double y` - Y component of the vector

#### Methods
1. `double magnitude() const` - Calculate and return the magnitude (length) of the vector
2. `double distance(const Vector2D& other) const` - Calculate distance to another vector
3. `Vector2D normalize() const` - Return a normalized (unit) vector
4. `double dot(const Vector2D& other) const` - Calculate dot product with another vector

#### Operator Overloads
1. `Vector2D operator+(const Vector2D& other) const` - Vector addition
2. `Vector2D operator-(const Vector2D& other) const` - Vector subtraction
3. `Vector2D operator*(double scalar) const` - Scalar multiplication
4. `bool operator==(const Vector2D& other) const` - Equality comparison (with tolerance)

### Mathematical Formulas:
- **Magnitude**: √(x² + y²)
- **Distance**: √((x₁-x₂)² + (y₁-y₂)²)
- **Normalize**: (x/magnitude, y/magnitude)
- **Dot Product**: x₁×x₂ + y₁×y₂

## 📋 Requirements
- Class must be implemented in C++20
- Include proper header guards
- Use `const` correctness for methods that don't modify the object
- Handle edge cases (zero-length vectors, normalization)
- Use appropriate floating-point comparison for equality
- Follow Google C++ Style Guide

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Constructor and Basic Properties
- `Vector2D()` should create vector (0, 0)
- `Vector2D(3.0, 4.0)` should create vector (3, 4)
- Access to `x` and `y` components should work

### 2. Magnitude Calculation
- `Vector2D(3.0, 4.0).magnitude()` should return 5.0
- `Vector2D(0.0, 0.0).magnitude()` should return 0.0
- `Vector2D(1.0, 0.0).magnitude()` should return 1.0

### 3. Distance Calculation
- Distance between `(0,0)` and `(3,4)` should be 5.0
- Distance between `(1,1)` and `(4,5)` should be 5.0
- Distance from vector to itself should be 0.0

### 4. Vector Addition
- `(1,2) + (3,4)` should equal `(4,6)`
- `(0,0) + (5,7)` should equal `(5,7)`
- Addition should be commutative

### 5. Vector Subtraction
- `(5,7) - (1,2)` should equal `(4,5)`
- `(3,4) - (3,4)` should equal `(0,0)`

### 6. Scalar Multiplication
- `(2,3) * 2.0` should equal `(4,6)`
- `(1,1) * 0.0` should equal `(0,0)`
- `(3,4) * -1.0` should equal `(-3,-4)`

### 7. Dot Product
- `(1,2).dot((3,4))` should return 11.0 (1×3 + 2×4)
- `(1,0).dot((0,1))` should return 0.0 (perpendicular vectors)

### 8. Normalization
- `Vector2D(3,4).normalize()` should have magnitude 1.0
- Zero vector normalization should handle gracefully

### 9. Equality Comparison
- `(1.0,2.0) == (1.0,2.0)` should be true
- Floating-point tolerance should be considered

## 📁 Files
- `include/solution.h` - Declare your class here
- `solution.cpp` - Implement your solution here
- `test.cpp` - Contains the test cases **DO NOT EDIT**
- `CMakeLists.txt` - Build configuration **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `include/solution.h` and `solution.cpp`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Include `<cmath>` for sqrt() function
- Use `const double EPSILON = 1e-9;` for floating-point comparisons
- For normalization of zero vectors, return (0, 0) or handle as special case
- Member functions that don't modify the object should be `const`
- Operator overloading should follow C++ conventions
- Consider using initialization lists in constructors
- Test your implementation with various edge cases
