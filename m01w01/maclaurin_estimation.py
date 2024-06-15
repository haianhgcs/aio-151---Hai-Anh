import math
import utilities as ut


def approx_sin(x, n):
    """
    Estimate the sine function for a given radian x using Maclaurin series up to n terms.

    Parameters:
    x (float): The radian value.
    n (int): The number of terms to use in the series expansion.

    Returns:
    float: The estimated value of sine(x).
    """
    sine = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / ut.factorial(2 * i + 1)
        sine += term
    return sine


def approx_cos(x, n):
    """
    Estimate the cosine function for a given radian x using Maclaurin series up to n terms.

    Parameters:
    x (float): The radian value.
    n (int): The number of terms to use in the series expansion.

    Returns:
    float: The estimated value of cosine(x).
    """
    cosine = 1
    for i in range(1, n):
        term = ((-1) ** i) * (x ** (2 * i)) / ut.factorial(2 * i)
        cosine += term
    return cosine


def approx_sinh(x, n):
    """
    Estimate the hyperbolic sine function for a given radian x using Maclaurin series up to n terms.

    Parameters:
    x (float): The radian value.
    n (int): The number of terms to use in the series expansion.

    Returns:
    float: The estimated value of sinh(x).
    """
    sinh = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / ut.factorial(2 * i + 1)
        sinh += term
    return sinh


def approx_cosh(x, n):
    """
    Estimate the hyperbolic cosine function for a given radian x using Maclaurin series up to n terms.

    Parameters:
    x (float): The radian value.
    n (int): The number of terms to use in the series expansion.

    Returns:
    float: The estimated value of cosh(x).
    """
    cosh = 1
    for i in range(1, n):
        term = (x ** (2 * i)) / math.factorial(2 * i)
        cosh += term
    return cosh
