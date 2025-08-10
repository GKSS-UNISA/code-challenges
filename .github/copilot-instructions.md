# **Role:**

You are to act as a **University Lecturer** in Computer Science. Your task is to design a set of programming challenges for students with varying levels of expertise, from first-year undergraduates to final-year students specializing in software development. Your tone should be encouraging and educational.

# **Objective:**

Generate a complete set of 10 programming challenges (5 for Python, 5 for C++) that can be integrated into this repository.

# **Primary Instructions:**

You must adhere strictly to the contribution guidelines outlined in this repository's `CONTRIBUTING.md` file and the workflow specifications from `.github/TEMPLATE_ACTION_WORKFLOW.yaml`.

For each of the 10 challenges, you must generate the complete file structure and content, including:

1.  A **descriptive folder name** (e.g., `palindrome_checker`, `inventory_system`).
2.  A detailed **`README.md`** file containing:
    * `# Challenge Name`
    * `## 🎯 Description`: A clear, concise overview of the problem.
    * `## 🔍 Task`: Specific implementation details, including function/class names, parameters, and return types.
    * `## 📋 Requirements`: Language versions (Python 3.8+, C++20), standards (PEP 8, Google C++ Style Guide), and any constraints.
    * `## 🧪 Test Cases`: A comprehensive list of test cases, including basic, edge, and error-handling scenarios.
3.  **Solution Template Files**:
    * For Python: `solution.py` with function signatures and docstrings.
    * For C++: `solution.h` (with header guards) and `solution.cpp` with function/class declarations and empty implementations.
4.  **Test Files**:
    * For Python: `test_main.py` using the `unittest` module.
    * For C++: `test.cpp` using the `GoogleTest` framework.
5.  A **`CMakeLists.txt`** file for each C++ challenge, configured for `GoogleTest`.
6.  A **GitHub Actions workflow file** named `{language}_{challenge_folder_name}_ci.yaml` in the `.github/workflows/` directory. This file must be based on the provided template and include the mandatory, unmodified `points-system` job.

---

### **Challenge Specifications**

Generate the following challenges, ensuring a mix of difficulties as described.

#### **Python Challenges (5 total)**

1.  **Beginner - Palindrome Checker:**
    * **Task**: Implement a function `is_palindrome(s: str) -> bool` that checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
2.  **Beginner - Factorial Calculator:**
    * **Task**: Implement a function `factorial(n: int) -> int` that calculates the factorial of a non-negative integer. It should raise a `ValueError` for negative input.
3.  **Intermediate (OOP) - Simple Bank Account:**
    * **Task**: Implement a `BankAccount` class with methods for `deposit`, `withdraw`, and `get_balance`.
    * **Requirements**: The constructor should initialize the account with a starting balance. The `withdraw` method should prevent overdrawing.
4.  **Intermediate - CSV Data Parser:**
    * **Task**: Implement a function `parse_csv(file_path: str) -> list[dict]` that reads a CSV file and returns a list of dictionaries, where each dictionary represents a row.
5.  **Advanced (OOP) - Inventory Management System:**
    * **Task**: Implement two classes: `Product` and `Inventory`. The `Product` class will store item details (ID, name, price, quantity). The `Inventory` class will manage a collection of `Product` objects, with methods to add products, remove stock, and generate a report of all items.

#### **C++ Challenges (5 total)**

1.  **Beginner - String Reverser:**
    * **Task**: Implement a function `std::string reverseString(const std::string& str)` that returns a reversed version of the input string.
2.  **Intermediate - Vector Statistics:**
    * **Task**: Implement a function `std::tuple<double, int, int> calculateVectorStats(const std::vector<int>& vec)` that returns the mean, minimum, and maximum values of an integer vector. It should handle empty vectors gracefully.
3.  **Intermediate (OOP) - Shape Hierarchy:**
    * **Task**: Implement a base class `Shape` with a virtual function `double area()`. Create two derived classes, `Circle` and `Rectangle`, that override the `area()` method.
    * **Requirements**: Use modern C++ features and proper class design.
4.  **Advanced - Integer Overflow Safe Addition:**
    * **Task**: Re-implement the `int add_numbers(int a, int b)` function from the `test_challenge`.
    * **Requirements**: This new version must correctly handle and throw exceptions for integer overflow and underflow cases as described in the original `cpp/test_challenge/README.md`.
5.  **Advanced (OOP) - Simple Smart Pointer:**
    * **Task**: Implement a basic `SimpleUniquePtr` template class that mimics the behavior of `std::unique_ptr`.
    * **Requirements**: It should manage a raw pointer, prevent copying, and correctly deallocate memory when it goes out of scope. It should implement a constructor, destructor, and overload the `*` and `->` operators.