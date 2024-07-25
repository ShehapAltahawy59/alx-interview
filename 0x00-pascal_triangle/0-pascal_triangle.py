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
    pascal_triangle=[]

    for row in range(n):
        currunt_row = [1]*(row+1)
        print(currunt_row)
        for j in range(1,row):
            currunt_row[j] = pascal_triangle[row-1][j-1]+pascal_triangle[row-1][j]
        pascal_triangle.append(currunt_row)
    return pascal_triangle

