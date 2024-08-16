#!/usr/bin/python3
"""
Generates Pascal's Triangle up to the specified number of rows.
"""


def pascal_triangle(n):
    """
    generates Pascal's Triangle up to the nth row.
    Args:
        n (int): Number of rows of Pascal's Triangle to generate.
    Returns:
        list: A list of lists, where each inner list represents a row of
                Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle
