#!/usr/bin/python3
import numpy as np

def rotate_2d_matrix(matrix):
    """
    an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    rotated = np.array(matrix)

    # In-place swap of rows and columns
    np.rot90(rotated, k=1, axes=(0,1))

    # Override original matrix
    matrix[:] = rotated
