import math
import numpy as np


def gram_matrix(tensor):
    # tensor có shape (channels, height, width)
    channels, height, width = tensor.shape
    features = tensor.reshape(channels, height * width)
    gram = np.einsum('ij,ik->jk', features, features)
    return gram

def inverse_matrix_2x2(matrix):
    return np.linalg.inv(matrix)


def compute_eigen(matrix):
    """
    Tính eigenvalues và eigenvectors của ma trận.

    Args:
        matrix (numpy.ndarray): Ma trận đầu vào (phải là ma trận vuông).

    Returns:
        tuple: Eigenvalues và eigenvectors của ma trận đầu vào.
    """
    # Kiểm tra nếu ma trận là ma trận vuông
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError(
            "Ma trận phải là ma trận vuông để tính eigenvalues và eigenvectors.")

    # Tính eigenvalues và eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    return eigenvalues, eigenvectors


def compute_cosine_similarity(vector1, vector2):
    """
    Tính Cosine Similarity giữa hai vector.

    Args:
        vector1 (numpy.ndarray): Vector đầu vào thứ nhất.
        vector2 (numpy.ndarray): Vector đầu vào thứ hai.

    Returns:
        float: Cosine Similarity giữa hai vector.
    """
    # Tính dot product của hai vector
    dot_product = np.dot(vector1, vector2)

    # Tính độ lớn (norm) của từng vector
    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    # Tính Cosine Similarity
    cosine_similarity_value = dot_product / (norm1 * norm2)


    return cosine_similarity_value


class Solution:
    def calculate_eigenvalues_eigenvectors(self, A):
        def get_eigenvalues(matrix):
            a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
            trace = a + d
            determinant = a * d - b * c
            delta = trace**2 - 4 * determinant

            if delta < 0:
                raise ValueError("Eigenvalues are complex.")

            sqrt_delta = math.sqrt(delta)
            eigenvalue1 = (trace + sqrt_delta) / 2
            eigenvalue2 = (trace - sqrt_delta) / 2

            return eigenvalue1, eigenvalue2

        def get_eigenvectors(matrix, eigenvalue):
            a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
            if eigenvalue == a:
                x = -b
                y = a - eigenvalue
            else:
                x = -c
                y = d - eigenvalue

            norm = math.sqrt(x**2 + y**2)
            return [x / norm, y / norm]

        eigenvalues = get_eigenvalues(A)
        eigenvectors = [get_eigenvectors(A, eigenvalue)
                        for eigenvalue in eigenvalues]

        return {eigenvalues[0]: eigenvectors[0], eigenvalues[1]: eigenvectors[1]}
