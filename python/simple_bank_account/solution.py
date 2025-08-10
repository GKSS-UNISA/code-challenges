class BankAccount:
    """
    A simple bank account class that supports deposits, withdrawals, and balance inquiries.
    """
    
    def __init__(self, initial_balance: float = 0.0) -> None:
        """
        Initialize a new bank account.
        
        Args:
            initial_balance (float): Starting balance for the account (default: 0.0)
            
        Raises:
            ValueError: If initial_balance is negative
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        # TODO: Initialize the account balance
        pass
    
    def deposit(self, amount: float) -> None:
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Raises:
            ValueError: If amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        # TODO: Add amount to account balance
        pass
    
    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if withdrawal successful, False if insufficient funds
            
        Raises:
            ValueError: If amount is negative or zero
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        # TODO: Check if sufficient funds and withdraw if possible
        # Return True if successful, False if insufficient funds
        pass
    
    def get_balance(self) -> float:
        """
        Get the current account balance.
        
        Returns:
            float: Current account balance
        """
        # TODO: Return current balance
        pass
    
    def __str__(self) -> str:
        """
        Return string representation of the account.
        
        Returns:
            str: Formatted account balance
        """
        # TODO: Return formatted balance string: "Account balance: $X.XX"
        pass
