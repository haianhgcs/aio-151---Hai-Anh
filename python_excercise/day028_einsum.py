import numpy as np
import sys
sys.path.append("..")


def gram_matrix(tensor):
    # tensor có shape (channels, height, width)
    channels, height, width = tensor.shape
    features = tensor.reshape(channels, height * width)
    gram = np.einsum('ik,jk->ij', features, features)
    return gram


if __name__ == "__main__":
    from util import matrix_util

    # Tính tổng của các phần tử trong một mảng
    a = np.array([1, 2, 3, 4])
    sum_a = np.einsum('i->', a)
    print(sum_a)  # Output : 10

    # element wise multiplication
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    np.einsum('ij,ij->ij', A, B)

    # Transpose A
    np.einsum('ij->ji', A)

    # sums the values of A
    np.einsum('ij->', A)

    # Bài tập 1: Tính tổng của các cột trong ma trận
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    column_sums = np.einsum('ij->j', A)
    print("sum matrix by column: \n", column_sums)  # Output : [12 15 18]

    # Bài tập 2: Tính tích vô hướng của hai ma trận
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    dot_product = np.einsum('ij,ij->', A, B)
    print("dot product: ", dot_product)  # Output : 70???

    # a = np.array([[1, 2], [3, 4]])
    # b = np.array([[5, 6], [7, 8]])
    # result = np.dot(a, b)
    # print(result)

    # returns diagonal matrix
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    diagonal = np.einsum('ii->i', A)
    print("diagonal vector:\n", diagonal)  # Output : 15

    # Bài tập 3: Tính tổng các phần tử trên đường chéo chính của ma trận
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    diagonal_sum = np.einsum('ii->', A)
    print("diagonal sum:", diagonal_sum)  # Output : 15

    # Bài tập 4: Nhân hai ma trận 2D
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    C = np.einsum('ij,jl->il', A, B)
    print("multi 2 matrix 2D:\n", C)  # Output : [[19 22] [43 50]]

    # Bài tập 5: Tính tích ngoài của hai vector
    # Nhân chéo (Outer product)
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    outter_product = np.einsum('i,j->ij', a, b)
    # Output : [[ 4 5 6] [ 8 10 12] [12 15 18]]
    print("outter product: \n", outter_product)

    # Bài tập 6: Tính ma trận Gram của một tensor 3D
    tensor = np.random.rand(3, 4, 4)
    gram = gram_matrix(tensor)
    print("gram matrix:\n", gram)
