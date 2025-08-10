def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # TODO: Implement palindrome checking logic
    # Hint: Consider using string methods to clean the input
    # and then compare characters from both ends
    pass
