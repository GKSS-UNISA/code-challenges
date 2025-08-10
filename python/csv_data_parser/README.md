# CSV Data Parser

## 🎯 Description
This challenge focuses on file I/O operations and data parsing in Python. You'll implement a function that reads CSV (Comma-Separated Values) files and converts them into a more usable format for data processing.

## 🔍 Task
Write a function `parse_csv(file_path: str) -> list[dict]` that:
1. Takes a file path to a CSV file as input
2. Reads the CSV file and parses its contents
3. Returns a list of dictionaries where:
   - Each dictionary represents one row of data
   - Dictionary keys are the column headers from the first row
   - Dictionary values are the corresponding cell values

### Expected CSV Format
```csv
name,age,city,salary
John Doe,30,New York,75000
Jane Smith,25,Los Angeles,65000
Bob Johnson,35,Chicago,80000
```

Should return:
```python
[
    {'name': 'John Doe', 'age': '30', 'city': 'New York', 'salary': '75000'},
    {'name': 'Jane Smith', 'age': '25', 'city': 'Los Angeles', 'salary': '65000'},
    {'name': 'Bob Johnson', 'age': '35', 'city': 'Chicago', 'salary': '80000'}
]
```

## 📋 Requirements
- Function must be implemented in Python 3.8+
- Include proper type hints
- Follow PEP 8 style guidelines
- Handle empty files gracefully
- Handle files with only headers
- Raise appropriate exceptions for file access errors
- Do not use external libraries (only built-in Python modules)
- Strip whitespace from values

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Basic CSV Parsing
- Parse a simple CSV with headers and data rows
- Verify correct dictionary structure
- Verify all rows are included

### 2. Edge Cases
- Empty CSV file should return empty list
- CSV with only headers should return empty list
- CSV with empty cells should handle gracefully
- CSV with extra commas should handle gracefully

### 3. Data Integrity
- Whitespace around values should be stripped
- All values should be preserved as strings
- Headers should be used as dictionary keys

### 4. File Handling
- Non-existent file should raise `FileNotFoundError`
- Invalid file permissions should raise appropriate exception
- File reading errors should be properly handled

### 5. Format Variations
- Handle CSV with different numbers of columns per row
- Handle CSV with quoted values containing commas
- Handle empty lines in CSV files

## 📁 Files
- `solution.py` - Implement your solution here
- `test_main.py` - Contains the test cases **DO NOT EDIT**
- Sample CSV files will be created during testing

## ✅ Submission
1. Implement your solution in `solution.py`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Use Python's built-in file handling capabilities (`open()`, `with` statement)
- Consider using `str.split(',')` for basic parsing, but be aware of edge cases
- Remember to handle the header row separately from data rows
- Use `str.strip()` to remove whitespace
- Consider what happens with empty rows or malformed data
- Think about how to handle files with inconsistent column counts
- Test your solution with various CSV formats to ensure robustness
