import numpy as np

# Nhân ma trận 2D (Matrix multiplication)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.einsum('ij,jk->ik', A, B)
print(C)  # Output : [[19 22] [43 50]]

# Tính tổng của các phần tử trong một mảng
a = np.array([1, 2, 3, 4])
sum_a = np.einsum('i->', a)
print(sum_a)  # Output : 10

# Nhân chéo (Outer product)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
outter_product = np.einsum('i,j->ij', a, b)
print(outter_product)  # Output : [[ 4 5 6] [ 8 10 12] [12 15 18]]

# Tính tổng của các cột trong ma trận
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
column_sums = np.einsum('ij->j', A)
print(column_sums)  # Output : [12 15 18]

# Tính tích vô hướng của hai ma trận
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
dot_product = np.einsum('ij,jk->ik', A, B)
print(dot_product) # Output : 70???

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)
print(result)

# Tính tổng các phần tử trên đường chéo chính của ma trận
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
diagonal_sum = np.einsum('ii->', A)
print(diagonal_sum) # Output : 15

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)
print(result)
