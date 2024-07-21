import numpy as np
import sys
sys.path.append("..")

if __name__ == "__main__":
    from util import matrix_util as mat

    # Tạo hai ma trận 3x3
    matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    matrix2 = np.array([[7, 8, 9], [1, 1, 1]])
    squared_matrix = np.array([[1, 2], [3, 4]])
    print(matrix1)
    print(matrix2)

    # nhân hai ma trận
    matrix_product = matrix1 * matrix2
    print("Tích của hai ma trận: \n", matrix_product)

    # Tìm ma trận chuyển vị:
    matrix_transpose = np.transpose(matrix1)
    print("Ma trận chuyển vị:\n", matrix_transpose)

    # Tìm ma trận nghịch đảo
    try:
        inverse_matrix = np.linalg.inv(squared_matrix)
        print("Ma trận nghịch đảo: \n", inverse_matrix)
    except np.linalg.LinAlgError:
        # Trường hợp ma trận không khả nghịch
        print("Không tồn tại ma trận nghịch đảo")

    # Tính định thức ma trận
    determinant = np.linalg.det(squared_matrix)
    print("Định thức của ma trận: \n", determinant)
