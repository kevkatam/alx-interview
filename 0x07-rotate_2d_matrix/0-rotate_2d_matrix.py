#!/usr/bin/python3
"""
module containing function to rotate a 2d matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ rotates a 2d matrix 90 degrees clockwise"""
    length = len(matrix)
    for i in range(length):
        matrix[i].reverse()

    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in range(length):
        matrix[row].reverse()

    matrix.reverse()
