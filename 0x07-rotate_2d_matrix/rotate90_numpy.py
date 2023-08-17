import numpy as np

def rotate_90(matrix):
    return np.transpose(matrix)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotated = rotate_90(matrix)
print(rotated)
