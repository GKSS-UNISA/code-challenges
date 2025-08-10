def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        TypeError: If input is not an integer
        ValueError: If input is negative
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # TODO: Implement factorial calculation
    # Remember: 0! = 1, and n! = n × (n-1) × (n-2) × ... × 1
    pass
