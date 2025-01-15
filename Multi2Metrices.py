import numpy as np

# Creating two matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8],
                    [9, 10],
                    [11, 12]])

# Matrix multiplication using np.dot()
result = np.dot(matrix1, matrix2)

# Alternatively, you can use the @ operator
# result = matrix1 @ matrix2

# Print the result
print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nProduct of Matrix 1 and Matrix 2:")
print(result)
