#!/usr/bin/python3
"""
0-pascal_triangle
"""
def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    if n <= 0 :
        return[]
    triangle = []
    for row in range(n):
        # Initialize each row with 1s
        current_row = [1] * (row + 1)
        # Calculate values between the edges of the triangle
        for j in range(1, row):
            current_row[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]
        triangle.append(current_row)
    return triangle
