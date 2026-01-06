import numpy as np

# Creating an array
arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:", arr)
print("Reshaped to (2,3):", arr.reshape(2, 3))
print("Reshaped to (3,2):", arr.reshape(3, 2))
print("Flattened:", arr.flatten())
