import unittest
from solution import Product, Inventory


class TestProduct(unittest.TestCase):
    
    def test_product_creation_valid(self):
        """Test creating product with valid inputs"""
        product = Product(1, "Laptop", 999.99, 10)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.price, 999.99)
        self.assertEqual(product.quantity, 10)

    def test_product_creation_invalid_inputs(self):
        """Test product creation with invalid inputs"""
        # Invalid product ID
        with self.assertRaises(TypeError):
            Product("1", "Laptop", 999.99, 10)
        
        # Empty name
        with self.assertRaises(ValueError):
            Product(1, "", 999.99, 10)
        with self.assertRaises(ValueError):
            Product(1, "   ", 999.99, 10)
        
        # Negative price
        with self.assertRaises(ValueError):
            Product(1, "Laptop", -100, 10)
        
        # Negative quantity
        with self.assertRaises(ValueError):
            Product(1, "Laptop", 999.99, -5)

    def test_product_properties_readonly(self):
        """Test that ID and name are read-only"""
        product = Product(1, "Laptop", 999.99, 10)
        
        # These should be read-only (no setters)
        with self.assertRaises(AttributeError):
            product.product_id = 2
        with self.assertRaises(AttributeError):
            product.name = "Desktop"

    def test_product_price_setter(self):
        """Test price property setter"""
        product = Product(1, "Laptop", 999.99, 10)
        
        # Valid price update
        product.price = 1199.99
        self.assertEqual(product.price, 1199.99)
        
        # Invalid price update
        with self.assertRaises(ValueError):
            product.price = -100

    def test_product_quantity_setter(self):
        """Test quantity property setter"""
        product = Product(1, "Laptop", 999.99, 10)
        
        # Valid quantity update
        product.quantity = 15
        self.assertEqual(product.quantity, 15)
        
        # Invalid quantity update
        with self.assertRaises(ValueError):
            product.quantity = -5

    def test_product_total_value(self):
        """Test total value calculation"""
        product = Product(1, "Laptop", 999.99, 10)
        expected_value = 999.99 * 10
        self.assertAlmostEqual(product.total_value(), expected_value, places=2)
        
        # Test after updates
        product.price = 1200
        product.quantity = 5
        self.assertEqual(product.total_value(), 6000.0)

    def test_product_string_representation(self):
        """Test string representation"""
        product = Product(1, "Laptop", 999.99, 10)
        expected = "ID: 1, Name: Laptop, Price: $999.99, Qty: 10"
        self.assertEqual(str(product), expected)


class TestInventory(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.inventory = Inventory()
        self.product1 = Product(1, "Laptop", 999.99, 10)
        self.product2 = Product(2, "Mouse", 25.50, 50)
        self.product3 = Product(3, "Keyboard", 75.00, 3)

    def test_inventory_creation(self):
        """Test creating empty inventory"""
        inventory = Inventory()
        self.assertEqual(inventory.get_total_value(), 0.0)

    def test_add_product_success(self):
        """Test adding products to inventory"""
        self.inventory.add_product(self.product1)
        retrieved = self.inventory.get_product(1)
        self.assertEqual(retrieved, self.product1)

    def test_add_product_duplicate_id(self):
        """Test adding product with duplicate ID"""
        self.inventory.add_product(self.product1)
        duplicate = Product(1, "Desktop", 1500, 5)
        
        with self.assertRaises(ValueError):
            self.inventory.add_product(duplicate)

    def test_add_product_invalid_type(self):
        """Test adding non-Product object"""
        with self.assertRaises(TypeError):
            self.inventory.add_product("not a product")

    def test_remove_product_success(self):
        """Test removing existing product"""
        self.inventory.add_product(self.product1)
        result = self.inventory.remove_product(1)
        
        self.assertTrue(result)
        self.assertIsNone(self.inventory.get_product(1))

    def test_remove_product_not_found(self):
        """Test removing non-existent product"""
        result = self.inventory.remove_product(999)
        self.assertFalse(result)

    def test_update_stock_success(self):
        """Test updating stock successfully"""
        self.inventory.add_product(self.product1)
        result = self.inventory.update_stock(1, 5)
        
        self.assertTrue(result)
        self.assertEqual(self.inventory.get_product(1).quantity, 15)

    def test_update_stock_negative_quantity(self):
        """Test updating stock with invalid quantity"""
        self.inventory.add_product(self.product1)
        
        # This should work (reduce stock)
        result = self.inventory.update_stock(1, -5)
        self.assertTrue(result)
        self.assertEqual(self.inventory.get_product(1).quantity, 5)
        
        # This should fail (would result in negative stock)
        with self.assertRaises(ValueError):
            self.inventory.update_stock(1, -10)

    def test_update_stock_not_found(self):
        """Test updating stock for non-existent product"""
        result = self.inventory.update_stock(999, 5)
        self.assertFalse(result)

    def test_get_product_exists(self):
        """Test getting existing product"""
        self.inventory.add_product(self.product1)
        retrieved = self.inventory.get_product(1)
        self.assertEqual(retrieved, self.product1)

    def test_get_product_not_exists(self):
        """Test getting non-existent product"""
        result = self.inventory.get_product(999)
        self.assertIsNone(result)

    def test_get_total_value(self):
        """Test calculating total inventory value"""
        self.inventory.add_product(self.product1)  # 999.99 * 10 = 9999.90
        self.inventory.add_product(self.product2)  # 25.50 * 50 = 1275.00
        
        expected_total = (999.99 * 10) + (25.50 * 50)
        actual_total = self.inventory.get_total_value()
        self.assertAlmostEqual(actual_total, expected_total, places=2)

    def test_get_low_stock_products_default(self):
        """Test getting low stock products with default threshold"""
        self.inventory.add_product(self.product1)  # qty: 10 (not low)
        self.inventory.add_product(self.product2)  # qty: 50 (not low)
        self.inventory.add_product(self.product3)  # qty: 3 (low)
        
        low_stock = self.inventory.get_low_stock_products()
        self.assertEqual(len(low_stock), 1)
        self.assertEqual(low_stock[0], self.product3)

    def test_get_low_stock_products_custom_threshold(self):
        """Test getting low stock products with custom threshold"""
        self.inventory.add_product(self.product1)  # qty: 10
        self.inventory.add_product(self.product2)  # qty: 50
        self.inventory.add_product(self.product3)  # qty: 3
        
        low_stock = self.inventory.get_low_stock_products(threshold=15)
        self.assertEqual(len(low_stock), 2)  # product1 and product3

    def test_generate_report(self):
        """Test generating inventory report"""
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        
        report = self.inventory.generate_report()
        self.assertIsInstance(report, str)
        self.assertIn("Laptop", report)
        self.assertIn("Mouse", report)
        self.assertIn("$999.99", report)
        self.assertIn("$25.50", report)

    def test_empty_inventory_operations(self):
        """Test operations on empty inventory"""
        self.assertEqual(self.inventory.get_total_value(), 0.0)
        self.assertEqual(self.inventory.get_low_stock_products(), [])
        self.assertFalse(self.inventory.remove_product(1))
        self.assertFalse(self.inventory.update_stock(1, 5))

    def test_multiple_operations_sequence(self):
        """Test sequence of multiple operations"""
        # Add products
        self.inventory.add_product(self.product1)
        self.inventory.add_product(self.product2)
        
        # Update stock
        self.inventory.update_stock(1, -2)  # Laptop: 10 -> 8
        self.inventory.update_stock(2, 25)  # Mouse: 50 -> 75
        
        # Verify changes
        self.assertEqual(self.inventory.get_product(1).quantity, 8)
        self.assertEqual(self.inventory.get_product(2).quantity, 75)
        
        # Calculate new total
        expected_total = (999.99 * 8) + (25.50 * 75)
        actual_total = self.inventory.get_total_value()
        self.assertAlmostEqual(actual_total, expected_total, places=2)


if __name__ == "__main__":
    unittest.main()
