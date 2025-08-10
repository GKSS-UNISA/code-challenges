import unittest
from solution import is_palindrome


class TestPalindromeChecker(unittest.TestCase):
    
    def test_basic_palindromes(self):
        """Test basic palindrome functionality"""
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome(""))

    def test_case_insensitive(self):
        """Test case insensitive palindrome checking"""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("MadAm"))
        self.assertFalse(is_palindrome("NoLemon"))

    def test_alphanumeric_only(self):
        """Test palindrome checking with spaces and punctuation"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_special_cases(self):
        """Test numeric and mixed palindromes"""
        self.assertTrue(is_palindrome("12321"))
        self.assertFalse(is_palindrome("12345"))
        self.assertTrue(is_palindrome("Madam123321madaM"))
        self.assertTrue(is_palindrome("!@#$%^&*()"))  # No alphanumeric characters

    def test_type_validation(self):
        """Test type validation"""
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)
        with self.assertRaises(TypeError):
            is_palindrome(['a', 'b', 'c'])

    def test_edge_cases(self):
        """Test additional edge cases"""
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("aba"))
        self.assertFalse(is_palindrome("ab"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))


if __name__ == "__main__":
    unittest.main()
