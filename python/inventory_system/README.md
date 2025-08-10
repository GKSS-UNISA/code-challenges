# Inventory Management System

## 🎯 Description
This advanced challenge combines object-oriented programming with data management to create a comprehensive inventory system. You'll implement multiple classes that work together to manage products and inventory operations.

## 🔍 Task
Implement two classes: `Product` and `Inventory` that work together to manage a collection of products.

### Product Class
Create a `Product` class with the following specifications:

#### Constructor
- `__init__(self, product_id: int, name: str, price: float, quantity: int)`
- Initialize a product with ID, name, price, and quantity
- Should raise `ValueError` for invalid inputs (negative price/quantity, empty name)

#### Properties/Methods
- `product_id: int` - Unique product identifier (read-only)
- `name: str` - Product name (read-only) 
- `price: float` - Product price (can be updated via setter)
- `quantity: int` - Available quantity (can be updated via setter)
- `total_value() -> float` - Returns price × quantity
- `__str__() -> str` - String representation: "ID: {id}, Name: {name}, Price: ${price:.2f}, Qty: {quantity}"

### Inventory Class
Create an `Inventory` class with the following specifications:

#### Constructor
- `__init__(self)` - Initialize empty inventory

#### Methods
1. `add_product(self, product: Product) -> None`
   - Add a product to inventory
   - If product ID already exists, raise `ValueError`

2. `remove_product(self, product_id: int) -> bool`
   - Remove product from inventory
   - Return `True` if removed, `False` if product not found

3. `update_stock(self, product_id: int, quantity: int) -> bool`
   - Update product quantity (add to existing quantity)
   - Return `True` if updated, `False` if product not found
   - Raise `ValueError` if resulting quantity would be negative

4. `get_product(self, product_id: int) -> Product | None`
   - Return product object by ID, or None if not found

5. `get_total_value(self) -> float`
   - Return total value of all products in inventory

6. `get_low_stock_products(self, threshold: int = 5) -> list[Product]`
   - Return list of products with quantity <= threshold

7. `generate_report(self) -> str`
   - Return formatted inventory report with all products

## 📋 Requirements
- Classes must be implemented in Python 3.8+
- Include proper type hints
- Follow PEP 8 style guidelines  
- Use appropriate encapsulation (private/protected attributes where needed)
- Implement proper validation for all inputs
- Handle edge cases gracefully

## 🧪 Test Cases
Your solution must pass the following test cases:

### 1. Product Class Tests
- Constructor with valid inputs should create product correctly
- Invalid inputs should raise appropriate exceptions
- Properties should be accessible and updateable where appropriate
- `total_value()` should calculate correctly
- String representation should be formatted correctly

### 2. Inventory Class Tests
- Empty inventory should be initialized correctly
- Adding products should work for unique IDs
- Adding duplicate product IDs should raise exception
- Removing existing products should return `True`
- Removing non-existent products should return `False`

### 3. Stock Management Tests
- Updating stock should modify quantity correctly
- Stock updates that would result in negative quantity should raise exception
- Getting products by ID should work correctly
- Getting non-existent products should return `None`

### 4. Reporting Tests
- Total value calculation should be accurate
- Low stock detection should work with default and custom thresholds
- Inventory report should be properly formatted

### 5. Edge Cases
- Empty inventory operations should handle gracefully
- Large quantities and prices should be handled correctly
- Multiple operations in sequence should maintain data integrity

## 📁 Files
- `solution.py` - Implement your solution here
- `test_main.py` - Contains the test cases **DO NOT EDIT**

## ✅ Submission
1. Implement your solution in `solution.py`
2. Push your changes to your repository
3. The automated tests will run and verify your solution

## 💡 Tips
- Use properties and setters to control access to attributes
- Consider using a dictionary to store products in the inventory (with product_id as key)
- Validate inputs in constructors and methods
- Think about when to raise exceptions vs. return error indicators
- Use list comprehensions for filtering operations like low stock detection
- Format monetary values appropriately in string representations
