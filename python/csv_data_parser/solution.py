def parse_csv(file_path: str) -> list[dict]:
    """
    Parse a CSV file and return its contents as a list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file to parse
        
    Returns:
        list[dict]: List of dictionaries representing CSV rows,
                   where keys are column headers and values are cell contents
                   
    Raises:
        FileNotFoundError: If the specified file doesn't exist
        PermissionError: If file cannot be read due to permissions
        IOError: If there's an error reading the file
    """
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    
    # TODO: Implement CSV parsing logic
    # Steps:
    # 1. Open and read the file
    # 2. Split content into lines
    # 3. Parse header row to get column names
    # 4. Parse data rows and create dictionaries
    # 5. Handle edge cases (empty files, malformed rows, etc.)
    pass
