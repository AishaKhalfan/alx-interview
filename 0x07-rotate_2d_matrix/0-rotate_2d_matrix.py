import numpy as np

def rotate_2d_matrix(matrix):
  rotated = np.array(matrix)

  # In-place swap of rows and columns
  np.rot90(rotated, k=1, axes=(0,1))
  
  # Override original matrix
  matrix[:] = rotated
