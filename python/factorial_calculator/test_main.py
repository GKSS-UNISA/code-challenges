import unittest
from solution import factorial


class TestFactorialCalculator(unittest.TestCase):
    
    def test_basic_factorials(self):
        """Test basic factorial calculations"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_edge_cases(self):
        """Test small number factorials"""
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def test_large_numbers(self):
        """Test larger factorial calculations"""
        self.assertEqual(factorial(20), 2432902008176640000)
        self.assertEqual(factorial(15), 1307674368000)

    def test_error_handling_negative(self):
        """Test error handling for negative numbers"""
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)
        with self.assertRaises(ValueError):
            factorial(-100)

    def test_error_handling_type(self):
        """Test error handling for wrong input types"""
        with self.assertRaises(TypeError):
            factorial(3.5)
        with self.assertRaises(TypeError):
            factorial("5")
        with self.assertRaises(TypeError):
            factorial(None)
        with self.assertRaises(TypeError):
            factorial([5])

    def test_return_type(self):
        """Test that function returns integers"""
        result = factorial(5)
        self.assertIsInstance(result, int)
        result = factorial(0)
        self.assertIsInstance(result, int)

    def test_additional_cases(self):
        """Test additional factorial cases"""
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)


if __name__ == "__main__":
    unittest.main()
