import numpy as np


def softmax_matrix(matrix):
    exp_matrix = np.exp(matrix - np.max(matrix, axis=1, keepdims=True))
    sum_exp = np.sum(exp_matrix, axis=1, keepdims=True)
    softmax_matrix = exp_matrix / sum_exp
    return softmax_matrix


def softmax_vector(x):
    print("x: ", x)
    x = np.exp(x)
    print("exp(x): ", exp_matrix)
    sum_exp = np.sum(x)
    x = x / sum_exp
    print("softmax(x): ", x)
    return x
