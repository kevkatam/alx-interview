#!/usr/bin/python3
"""
function that returns a list of lists of integers representing the
Pascal’s triangle of n
"""


def pascal_triangle(n):
    """ function that returns pascal's triangle """
    if (n <= 0):
        return []
    triangle = []

    for row in range(n):
        current_row = []
        for i in range(row + 1):
            if (i == 0 or i == row):
                current_row.append(1)
            else:
                prev_row = triangle[row - 1]
                current_row.append(prev_row[i - 1] + prev_row[i])
                triangle.append(current_row)
    return triangle
