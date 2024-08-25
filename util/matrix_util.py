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