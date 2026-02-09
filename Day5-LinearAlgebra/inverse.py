import numpy as np

A = np.array([[4, 7],
              [2, 6]])

inverse = np.linalg.inv(A)

print("Matrix Inverse:\n", inverse)
