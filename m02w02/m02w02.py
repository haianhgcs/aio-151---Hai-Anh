import numpy as np
import cv2
import sys
import os
sys.path.append("..")

if __name__ == "__main__":
    from util import vector_util
    from util import matrix_util
    from util import cv_util

    A = [[-2, 6], [8, -4]]
    A_inverse = matrix_util.inverse_matrix_2x2(A)
    print(A_inverse)

    # Resize các ảnh đầu vào về cùng kích thươc
    # bg1_image = cv2.imread(os.path.abspath(
    #     os.getcwd()) + "/data/GreenBackground.png", 1)
    # bg1_image = cv2.resize(bg1_image, (678, 381))
    # bg1_image = cv2.cvtColor(bg1_image, cv2.COLOR_BGR2RGB)

    # ob_image = cv2.imread(os.path.abspath(os.getcwd()) + "/data/Object.png", 1)
    # ob_image = cv2.resize(ob_image, (678, 381))
    # ob_image = cv2.cvtColor(ob_image, cv2.COLOR_BGR2RGB)

    # bg2_image = cv2.imread(os.path.abspath(
    #     os.getcwd()) + "/data/NewBackground.jpg", 1)
    # bg2_image = cv2.resize(bg2_image, (678, 381))
    # bg2_image = cv2.cvtColor(bg2_image, cv2.COLOR_BGR2RGB)

    # output = cv_util.replace_background(bg1_image, bg2_image, ob_image)

    print("Câu #1: D")
    vector = np.array([-2, 4, 9, 21])
    result = vector_util.compute_vector_length(vector)
    print(round(result, 2))

    print("Câu #2: B")
    v1 = np.array([0, 1, -1, 2])
    v2 = np.array([2, 5, 1, 0])
    result = vector_util.compute_dot_product(v1, v2)
    print(round(result, 2))

    print("Câu #3: A")
    x = np.array([[1, 2], [3, 4]])
    k = np.array([1, 2])
    print(x.dot(k))

    print("Câu #4: B")
    x = np.array([[-1, 2], [3, -4]])
    k = np.array([1, 2])
    print(x@k)

    print("Câu #5: A")
    m = np.array([[-1, 1, 1], [0, -4, 9]])
    v = np.array([0, 2, 1])
    print(vector_util.matrix_multi_vector(m, v))

    print("Câu #6: C")
    m1 = np.array([[0, 1, 2], [2, -3, 1]])
    m2 = np.array([[1, -3], [6, 1], [0, -1]])
    print(vector_util.matrix_multi_matrix(m1, m2))

    print("Câu #7: A")
    m1 = np.eye(3)
    m2 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print(m1@m2)

    print("Câu #8: D")
    m1 = np.eye(2)
    m1 = np.reshape(m1, (-1, 4))[0]
    m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    print(m1@m2)

    print("Câu #9: B")
    m1 = np.array([[1, 2], [3, 4]])
    m1 = np.reshape(m1, (-1, 4), "F")[0]
    m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    print(m1@m2)

    print("Câu #10: A")
    m1 = np.array([[-2, 6], [8, -4]])
    print(matrix_util.inverse_matrix_2x2(m1))

    print("Câu #11: A")
    m1 = np.array([[0.9, 0.2], [0.1, 0.8]])
    eigenvalues, eigenvectors = matrix_util.compute_eigen(m1)
    print(eigenvectors)

    print("Câu #12: C")
    x = np.array([1, 2, 3, 4])
    y = np.array([1, 0, 3, 0])
    result = matrix_util.compute_cosine_similarity(x, y)
    print(round(result, 3))
