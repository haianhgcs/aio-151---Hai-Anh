import numpy as np


def compute_vector_length(vector):
    len_of_vector = np.sqrt(np.sum(vector ** 2))
    return len_of_vector


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result