# 🤝 Contributing to Code Challenges

Thank you for your interest in contributing new challenges to this repository! This guide will help you create well-structured, testable programming challenges that provide value to the community.

## 📋 Overview

To contribute a new challenge, you'll need to create:
1. A challenge folder with a descriptive name
2. A detailed README explaining the challenge
3. Test files/suites to validate solutions
4. A GitHub Actions workflow for automated testing and scoring

## 🏗️ Challenge Structure Requirements

### 1. Folder Naming Convention
- Create a folder with a **short, descriptive name** using lowercase letters and underscores
- Examples: `fibonacci_sequence`, `binary_search`, `merge_sort`, `palindrome_checker`
- Place your folder in the appropriate language directory (`python/`, `cpp/`, etc.)

### 2. Required Files in Each Challenge Folder

#### 📝 README.md (Required)
Your README must include the following sections:

```markdown
# Challenge Name

## 🎯 Description
Clear, concise description of what the challenge is about.

## 🔍 Task
Detailed explanation of what needs to be implemented, including:
- Function/class names (be specific!)
- Input parameters and their types
- Expected return values and types
- Any special requirements or constraints

## 📋 Requirements
- Language version requirements
- Coding standards to follow
- Any specific libraries or frameworks to use/avoid

## 🧪 Test Cases
List all test cases that solutions must pass:
- Basic functionality tests
- Edge cases
- Error handling scenarios
- Performance requirements (if applicable)
```

#### 🔧 Solution Template/Starter Code
- Provide a basic template or starter file
- Include function signatures, class definitions, or structure
- Add helpful comments for guidance

#### 🧪 Test Files (Required)
Create comprehensive test suites that:
- Test all specified functionality
- Cover edge cases and error conditions
- Provide clear, descriptive test names
- Use appropriate testing frameworks for the language 
  > _we use GoogleTest for C++ & Unittest for python to avoid having to pip install_

#### ⚙️ Build Configuration (if needed)
- For C++: Include `CMakeLists.txt`
- For Python: Include `requirements.txt` if external packages are needed
- For other languages: Include appropriate build/dependency files but all must be contained within the named folder of the challenge.

## 📐 Naming Conventions

### Function/Class Naming
Be specific and consistent with naming requirements:

**Python:**
```python
def function_name(param1: type, param2: type) -> return_type:
    """Clear docstring explaining the function"""
    pass
```

**C++:**
```cpp
// In header file
int functionName(int param1, const std::string& param2);

// In implementation
int functionName(int param1, const std::string& param2) {
    // Implementation
}
```

### File Naming
- **Python:** `solution.py`, `test_main.py`
- **C++:** `solution.cpp`, `solution.h`, `test.cpp`
- **README:** Always `README.md`

## 🚀 GitHub Actions Workflow

### Required Workflow File
Create a workflow file in `.github/workflows/` with the naming pattern:
`{language}_{challenge_folder_name}_ci.yaml`

Examples:
- `python_fibonacci_sequence_ci.yaml`
- `cpp_binary_search_ci.yaml`

### Workflow Requirements
Your workflow must:

1. **Trigger on appropriate paths:**
   ```yaml
   on:
     push:
       paths:
         - 'language/challenge_folder/**'
   ```

2. **Include a test job** that builds and runs your tests

3. **Include a points-system job** that runs after successful tests

4. **Use the exact same secrets pattern** as existing workflows:
   ```yaml
   - name: Check secrets and increment points
     shell: bash
     run: |
       if [[ -n "${{ secrets.GKSS_LEADERBOARD_API_URL }}" && -n "${{ secrets.GKSS_LEADERBOARD_API_KEY }}" ]]; then
         echo "Incrementing points..."
         curl -X POST ${{ secrets.GKSS_LEADERBOARD_API_URL }} \
           -H "x-gkssunisa-api-key: ${{ secrets.GKSS_LEADERBOARD_API_KEY }}" \
           -H "Content-Type: application/json" \
           -d '{"message": "i did it! ${{ github.actor }}"}'
       else
         echo "Skipping points increment - required secrets not found"
         exit 1
       fi
   ```

> ⚠️ **Important:** The secrets access pattern must match exactly as shown above. This is required for the leaderboard system to function properly.

## 📚 Template Files

Use the [`TEMPLATE_ACTION_WORKFLOW.yaml`](./.github/TEMPLATE_ACTION_WORKFLOW.yaml) file in the `.github/` folder as a starting point for your workflow. This template includes:
- Detailed comments explaining each section
- Examples for Python, C++, JavaScript, and Java
- The exact secrets pattern required for the points system
- A comprehensive customization checklist

Replace placeholder text like `LANGUAGE` and `CHALLENGE_FOLDER` with your actual values.

## ✅ Quality Checklist

Before submitting your challenge, ensure:

- [ ] Folder has a clear, descriptive name
- [ ] README includes all required sections
- [ ] Function/class names are clearly specified
- [ ] Test suite covers all requirements and edge cases
- [ ] **Tests pass locally**
- [ ] GitHub Actions workflow is properly configured
- [ ] Workflow file name follows the naming convention
- [ ] Secrets are accessed using the exact required pattern
- [ ] **Challenge difficulty is appropriate for the target audience**

## 🎯 Challenge Difficulty Guidelines

> Be as informtive and keep the quality of challenges fair 

- **Beginner:** Basic programming concepts, simple algorithms
- **Intermediate:** Data structures, algorithm optimization, error handling
- **Advanced:** Complex algorithms, performance optimization, system design

## 📝 Submission Process

1. Clone this repo directly!
> This is because we want to avoid pushing solutions into the base repo. You work on challenges in your fork and submit new challenge directly to the base repo.
2. Create a new branch with for your new challenge.
2. Create your challenge following the structure above
3. Test your workflow locally (if possible)
4. Submit a Pull Request with:
   - Clear description of the challenge
   - Difficulty level
   - Any special requirements or dependencies

## 🤔 Need Help?

- Check existing challenges for examples
- Review the template workflow file
- Examine the current challenge structures
- Reach out in the discussions if your have questions.

## 🙏 Thank You!

Your contributions help make this repository a valuable learning resource for developers of all skill levels. We appreciate your effort in creating well-structured, educational challenges!

---

<div align="center">

*Happy coding! 🚀*

</div>