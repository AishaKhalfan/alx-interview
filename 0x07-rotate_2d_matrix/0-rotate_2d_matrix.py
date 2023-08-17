#!/usr/bin/python3
"""
0x07 - Rotate 2D Matrix
"""
import numpy as np

def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix, rotate it
    90 degrees clockwise.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse rows
    for i in range(n):
        matrix[i].reverse()
    
