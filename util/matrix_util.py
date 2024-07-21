import numpy as np


def gram_matrix(tensor):
    # tensor có shape (channels, height, width)
    channels, height, width = tensor.shape
    features = tensor.reshape(channels, height * width)
    gram = np.einsum('ij,ik->jk', features, features)
    return gram
