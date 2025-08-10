# Simple Bank Account

## 🎯 Description
This challenge introduces object-oriented programming concepts by implementing a simple bank account system. You'll learn about encapsulation, instance methods, and proper validation in class design.

## 🔍 Task
Implement a `BankAccount` class with the following specifications:

### Constructor
- `__init__(self, initial_balance: float = 0.0)` 
- Initialize account with given balance (defaults to 0.0)
- Should raise `ValueError` if initial_balance is negative

### Methods
1. `deposit(self, amount: float) -> None`
   - Add money to the account
   - Should raise `ValueError` if amount is negative or zero
   
2. `withdraw(self, amount: float) -> bool`
   - Remove money from account if sufficient funds available
   - Return `True` if withdrawal successful, `False` if insufficient funds
   - Should raise `ValueError` if amount is negative or zero
   
3. `get_balance(self) -> float`
   - Return current account balance
   
4. `__str__(self) -> str`
   - Return string representation: "Account balance: $X.XX"

## 📋 Requirements
- Class must be implemented in Python 3.8+
- Include proper type hints
- Follow PEP 8 style guidelines
- Handle negative amounts appropriately
- Prevent overdrafts (balance cannot go below zero)
- Use appropriate data types for monetary values

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Constructor Tests
- `BankAccount()` should create account with balance 0.0
- `BankAccount(100.0)` should create account with balance 100.0
- `BankAccount(-50.0)` should raise `ValueError`

### 2. Deposit Tests
- `deposit(50.0)` on empty account should result in balance 50.0
- `deposit(25.50)` should handle decimal amounts
- `deposit(-10.0)` should raise `ValueError`
- `deposit(0)` should raise `ValueError`

### 3. Withdrawal Tests
- `withdraw(30.0)` from account with 100.0 should return `True` and balance 70.0
- `withdraw(150.0)` from account with 100.0 should return `False` and balance unchanged
- `withdraw(-20.0)` should raise `ValueError`
- `withdraw(0)` should raise `ValueError`

### 4. Balance Tests
- `get_balance()` should return current balance as float
- Balance should update correctly after deposits and withdrawals

### 5. String Representation Tests
- `str(account)` should return formatted string with balance

### 6. Edge Cases
- Multiple deposits and withdrawals should work correctly
- Attempting to withdraw exact balance should succeed
- Floating point precision should be handled appropriately

## 📁 Files
- `solution.py` - Implement your solution here
- `test_main.py` - Contains the test cases **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `solution.py`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Use instance variables to store account state
- Consider using `round()` for floating point precision issues
- Remember that `withdraw()` should return a boolean indicating success
- Validate inputs before processing transactions
- Consider what should happen when trying to withdraw more than the balance
