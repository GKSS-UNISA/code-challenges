# Binary Search Tree

## 🎯 Description
This intermediate challenge focuses on implementing a binary search tree (BST) data structure in C++. You'll practice dynamic memory management, recursion, tree traversal algorithms, and proper resource management with modern C++ features.

## 🔍 Task
Implement a `BinarySearchTree` class that manages integer values in a binary search tree structure.

### Class Requirements:

#### Node Structure (Internal)
You'll need an internal node structure to represent tree nodes:
```cpp
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int value) : data(value), left(nullptr), right(nullptr) {}
};
```

#### Public Interface

#### Constructor and Destructor
- `BinarySearchTree()` - Initialize empty tree
- `~BinarySearchTree()` - Clean up all allocated memory

#### Core Methods
1. `void insert(int value)` - Insert a value into the tree
2. `bool contains(int value) const` - Check if value exists in tree
3. `bool remove(int value)` - Remove a value from tree, return success status
4. `int size() const` - Return number of nodes in tree
5. `bool empty() const` - Check if tree is empty

#### Traversal Methods
1. `std::vector<int> inorder() const` - Return inorder traversal (sorted order)
2. `std::vector<int> preorder() const` - Return preorder traversal
3. `std::vector<int> postorder() const` - Return postorder traversal

#### Utility Methods
1. `int findMin() const` - Find minimum value (leftmost node)
2. `int findMax() const` - Find maximum value (rightmost node)
3. `int height() const` - Calculate height of tree

### BST Properties:
- For each node: left subtree values < node value < right subtree values
- No duplicate values allowed
- Empty tree has height 0, single node has height 1

## 📋 Requirements
- Class must be implemented in C++20
- Include proper header guards
- Use proper memory management (no memory leaks)
- Follow RAII principles
- Handle edge cases gracefully
- Use const correctness
- Implement rule of three/five if needed

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Constructor and Basic Operations
- Empty tree should have size 0 and be empty
- Single insertion should work correctly
- Tree should maintain BST property

### 2. Insertion Tests
- Multiple insertions in various orders
- Duplicate insertions should be ignored
- Tree structure should remain valid

### 3. Search Operations
- `contains()` should find existing values
- `contains()` should return false for non-existent values
- Edge case searches (empty tree, single node)

### 4. Removal Operations
- Remove leaf nodes
- Remove nodes with one child
- Remove nodes with two children
- Remove non-existent values should return false

### 5. Traversal Tests
- Inorder traversal should return values in sorted order
- Preorder and postorder should follow correct patterns
- Empty tree traversals should return empty vectors

### 6. Utility Function Tests
- `findMin()` and `findMax()` should work correctly
- Height calculation should be accurate
- Size counting should be correct

### 7. Memory Management
- No memory leaks after destructor
- Proper cleanup of all nodes
- Safe operations on empty trees

### 8. Edge Cases
- Operations on empty tree
- Single-node tree operations
- Large tree operations

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
- Use recursion for most tree operations
- Remember to handle the case where tree is empty
- For removal, consider three cases: leaf, one child, two children
- When removing node with two children, replace with inorder successor
- Include `<vector>` for return types
- Use `nullptr` instead of `NULL`
- Consider implementing helper recursive functions that take Node* parameters
- Don't forget to update size counter in insert/remove operations
- Height of empty tree is typically defined as 0 or -1 (we'll use 0)
- Be careful with memory management - every `new` needs a corresponding `delete`
