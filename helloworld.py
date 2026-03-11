#!/usr/bin/env python3
"""
A comprehensive Hello World program demonstrating Python best practices.
"""

def greet(name="World"):
    """
    Greet someone by name.
    
    Args:
        name (str): The name of the person to greet (default: "World")
    
    Returns:
        str: A personalized greeting message
    """
    return f"Hello, {name}!"

def main():
    """Main function to demonstrate the greeting functionality."""
    # Simple greeting
    print(greet())
    
    # Personalized greeting
    print(greet("Python Programmer"))
    
    # Demonstrate with multiple names
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(greet(name))

if __name__ == "__main__":
    main()
