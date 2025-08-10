import unittest
from solution import BankAccount


class TestSimpleBankAccount(unittest.TestCase):
    
    def test_constructor_default(self):
        """Test default constructor"""
        account = BankAccount()
        self.assertEqual(account.get_balance(), 0.0)

    def test_constructor_with_balance(self):
        """Test constructor with initial balance"""
        account = BankAccount(100.0)
        self.assertEqual(account.get_balance(), 100.0)
        
        account = BankAccount(50.75)
        self.assertEqual(account.get_balance(), 50.75)

    def test_constructor_negative_balance(self):
        """Test constructor with negative balance"""
        with self.assertRaises(ValueError):
            BankAccount(-50.0)
        with self.assertRaises(ValueError):
            BankAccount(-0.01)

    def test_deposit_basic(self):
        """Test basic deposit functionality"""
        account = BankAccount()
        account.deposit(50.0)
        self.assertEqual(account.get_balance(), 50.0)
        
        account.deposit(25.50)
        self.assertEqual(account.get_balance(), 75.50)

    def test_deposit_invalid_amounts(self):
        """Test deposit with invalid amounts"""
        account = BankAccount()
        
        with self.assertRaises(ValueError):
            account.deposit(-10.0)
        with self.assertRaises(ValueError):
            account.deposit(0)
        with self.assertRaises(ValueError):
            account.deposit(-0.01)

    def test_withdraw_sufficient_funds(self):
        """Test withdrawal with sufficient funds"""
        account = BankAccount(100.0)
        
        result = account.withdraw(30.0)
        self.assertTrue(result)
        self.assertEqual(account.get_balance(), 70.0)
        
        result = account.withdraw(70.0)  # Withdraw exact balance
        self.assertTrue(result)
        self.assertEqual(account.get_balance(), 0.0)

    def test_withdraw_insufficient_funds(self):
        """Test withdrawal with insufficient funds"""
        account = BankAccount(100.0)
        
        result = account.withdraw(150.0)
        self.assertFalse(result)
        self.assertEqual(account.get_balance(), 100.0)  # Balance unchanged

    def test_withdraw_invalid_amounts(self):
        """Test withdrawal with invalid amounts"""
        account = BankAccount(100.0)
        
        with self.assertRaises(ValueError):
            account.withdraw(-20.0)
        with self.assertRaises(ValueError):
            account.withdraw(0)
        with self.assertRaises(ValueError):
            account.withdraw(-0.01)

    def test_get_balance(self):
        """Test get_balance method"""
        account = BankAccount(42.50)
        self.assertIsInstance(account.get_balance(), float)
        self.assertEqual(account.get_balance(), 42.50)

    def test_string_representation(self):
        """Test string representation"""
        account = BankAccount(123.45)
        expected = "Account balance: $123.45"
        self.assertEqual(str(account), expected)
        
        account = BankAccount(0.0)
        expected = "Account balance: $0.00"
        self.assertEqual(str(account), expected)

    def test_multiple_transactions(self):
        """Test multiple deposits and withdrawals"""
        account = BankAccount(50.0)
        
        account.deposit(25.0)
        self.assertEqual(account.get_balance(), 75.0)
        
        account.withdraw(20.0)
        self.assertEqual(account.get_balance(), 55.0)
        
        account.deposit(10.50)
        self.assertEqual(account.get_balance(), 65.50)
        
        result = account.withdraw(100.0)  # Insufficient funds
        self.assertFalse(result)
        self.assertEqual(account.get_balance(), 65.50)

    def test_floating_point_precision(self):
        """Test floating point operations"""
        account = BankAccount(10.10)
        account.deposit(20.20)
        account.withdraw(5.05)
        # Due to floating point precision, we use assertAlmostEqual
        self.assertAlmostEqual(account.get_balance(), 25.25, places=2)


if __name__ == "__main__":
    unittest.main()
