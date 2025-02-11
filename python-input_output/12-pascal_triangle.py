#!/usr/bin/python3
""" Module that defines the function pascal_triangle. """

def pascal_triangle(n):
    """ Returns a list of lists of integers representing Pascal’s triangle.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing the triangle.
    """
    if n <= 0:
        return [] # Empty list

    triangle = [[1]] # Initializing the first line

    for i in range (1, n):
        prev_row = triangle[-1] # Retrieving the last line
        new_row = [1] # First element of the line
        for j in range(len(prev_row) - 1):
            # Sum of adjacent elements
            new_row.append(prev_row[j] + prev_row[j + 1])

        new_row.append(1) # Last element of the line
        triangle.append(new_row) # Add the new row

    return triangle
