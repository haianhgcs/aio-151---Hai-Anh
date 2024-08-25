import math


def sigmoid(x):
    """
    Calculate the Sigmoid of a given value.

    Parameters:
    x (float): The input value.

    Returns:
    float: The Sigmoid of the input value.
    """
    return 1 / (1 + math.exp(-x))


def relu(x):
    """
    Calculate the ReLU of a given value.

    Parameters:
    x (float): The input value.

    Returns:
    float: The ReLU of the input value.
    """
    return max(0, x)


def elu(x, alpha=1.0):
    """
    Calculate the ELU of a given value.

    Parameters:
    x (float): The input value.
    alpha (float): The alpha value, default is 1.0.

    Returns:
    float: The ELU of the input value.
    """
    return x if x > 0 else alpha * (math.exp(x) - 1)
