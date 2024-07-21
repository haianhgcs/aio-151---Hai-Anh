import numpy as np
import math


def compute_attention_score(Q, K):
    return np.dot(Q, K.T)


def create_position_matrix(seq_length, embed_size):
    position_matrix = np.zeros((seq_length, embed_size))

    for pos in range(seq_length):
        for i in range(0, embed_size, 2):
            if i % 2 == 0:
                position_matrix[pos, i] = math.sin(
                    pos / 10000 ** (2 * i / embed_size))
            else:
                position_matrix[pos, i] = math.cos(
                    pos / 10000 ** (2 * i / embed_size))

    return position_matrix
