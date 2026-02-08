import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array Addition:", a + b)
print("Array Multiplication:", a * b)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix Addition:\n", A + B)
print("Elementwise Multiplication:\n", A * B)
print("Matrix Multiplication:\n", A @ B)
print("Transpose of A:\n", A.T)
