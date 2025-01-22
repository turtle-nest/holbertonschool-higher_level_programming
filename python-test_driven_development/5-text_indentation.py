#!/usr/bin/python3
"""
This module contains a function that formats and prints text
with 2 new lines after each of these characters: '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each 
    of these characters: '.', '?', and ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize an empty result and temporary buffer
    result = ""
    buffer = ""
    
    for char in text:
        buffer += char  # Add each character to the buffer
        if char in ".:?":
            # Strip spaces from buffer and append it with two new lines
            result += buffer.strip() + "\n\n"
            buffer = ""  # Reset the buffer
    
    # Add any remaining text in the buffer without adding extra new lines
    if buffer.strip():
        result += buffer.strip()
    
    # Print the formatted result
    print(result, end="")
