import numpy as np

def rotate_matrix(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    rotated = np.transpose(matrix)
    
    # Reverse the order of columns
    rotated = rotated[:,::-1]
    
    return rotated

# Example
matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]

rotated = rotate_matrix(matrix) 
print(rotated)
