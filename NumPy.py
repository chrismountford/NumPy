import numpy as np

a = np.array([[2, 5, 6, 9], [1, 6, 11, 9]], dtype=int)  # List of lists transforms arrays in n-dimensions

b = np.array([(1, 3, 5, 7), (2, 4, 6, 8)])

# print(a)
# print(b)

# Elementwise operations
print("a + b =")
print(a+b)

print("a * b =")
print(a*b)

# Matrix operations

c = np.array([[1, 4, 9]])
d = np.array([[1], [3], [10]])

print("c dot product d =")
print(c.dot(d))  # Matrix multiplication

# Unary operations
e = np.random.random((3, 4))
print(e)

print("e.sum(axis=0) =")  # Specify axis as rows or columns
print(e.sum(axis=0))

print("e.sum(axis=1) =")
print(e.sum(axis=1))
