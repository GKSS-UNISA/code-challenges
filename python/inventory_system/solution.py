from typing import Optional


class Product:
    """
    Represents a product in the inventory system.
    """
    
    def __init__(self, product_id: int, name: str, price: float, quantity: int) -> None:
        """
        Initialize a new product.
        
        Args:
            product_id (int): Unique product identifier
            name (str): Product name
            price (float): Product price (must be non-negative)
            quantity (int): Available quantity (must be non-negative)
            
        Raises:
            ValueError: If price or quantity is negative, or name is empty
            TypeError: If inputs have wrong types
        """
        if not isinstance(product_id, int):
            raise TypeError("Product ID must be an integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer")
        
        # TODO: Initialize instance variables
        pass
    
    @property
    def product_id(self) -> int:
        """Get the product ID (read-only)."""
        # TODO: Return product ID
        pass
    
    @property
    def name(self) -> str:
        """Get the product name (read-only)."""
        # TODO: Return product name
        pass
    
    @property
    def price(self) -> float:
        """Get the product price."""
        # TODO: Return product price
        pass
    
    @price.setter
    def price(self, value: float) -> None:
        """Set the product price."""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        # TODO: Set product price
        pass
    
    @property
    def quantity(self) -> int:
        """Get the product quantity."""
        # TODO: Return product quantity
        pass
    
    @quantity.setter
    def quantity(self, value: int) -> None:
        """Set the product quantity."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Quantity must be a non-negative integer")
        # TODO: Set product quantity
        pass
    
    def total_value(self) -> float:
        """
        Calculate the total value of this product (price × quantity).
        
        Returns:
            float: Total value of the product
        """
        # TODO: Calculate and return total value
        pass
    
    def __str__(self) -> str:
        """
        Return string representation of the product.
        
        Returns:
            str: Formatted product information
        """
        # TODO: Return formatted string: "ID: {id}, Name: {name}, Price: ${price:.2f}, Qty: {quantity}"
        pass


class Inventory:
    """
    Manages a collection of products.
    """
    
    def __init__(self) -> None:
        """Initialize an empty inventory."""
        # TODO: Initialize inventory data structure
        pass
    
    def add_product(self, product: Product) -> None:
        """
        Add a product to the inventory.
        
        Args:
            product (Product): Product to add
            
        Raises:
            ValueError: If product ID already exists
            TypeError: If product is not a Product instance
        """
        if not isinstance(product, Product):
            raise TypeError("Must provide a Product instance")
        
        # TODO: Check for duplicate ID and add product
        pass
    
    def remove_product(self, product_id: int) -> bool:
        """
        Remove a product from inventory.
        
        Args:
            product_id (int): ID of product to remove
            
        Returns:
            bool: True if removed, False if not found
        """
        # TODO: Remove product if exists, return success status
        pass
    
    def update_stock(self, product_id: int, quantity: int) -> bool:
        """
        Update product stock (add to existing quantity).
        
        Args:
            product_id (int): ID of product to update
            quantity (int): Quantity to add (can be negative)
            
        Returns:
            bool: True if updated, False if product not found
            
        Raises:
            ValueError: If resulting quantity would be negative
        """
        # TODO: Find product, validate new quantity, and update
        pass
    
    def get_product(self, product_id: int) -> Optional[Product]:
        """
        Get a product by its ID.
        
        Args:
            product_id (int): Product ID to search for
            
        Returns:
            Product or None: The product if found, None otherwise
        """
        # TODO: Return product if found, None otherwise
        pass
    
    def get_total_value(self) -> float:
        """
        Calculate total value of all products in inventory.
        
        Returns:
            float: Total inventory value
        """
        # TODO: Sum total values of all products
        pass
    
    def get_low_stock_products(self, threshold: int = 5) -> list[Product]:
        """
        Get products with stock below or equal to threshold.
        
        Args:
            threshold (int): Stock threshold (default: 5)
            
        Returns:
            list[Product]: List of low-stock products
        """
        # TODO: Filter products by quantity <= threshold
        pass
    
    def generate_report(self) -> str:
        """
        Generate a formatted inventory report.
        
        Returns:
            str: Formatted report with all products
        """
        # TODO: Create formatted report of all products
        pass
