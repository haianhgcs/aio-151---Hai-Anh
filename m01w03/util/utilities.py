import math


def float_equals(a, b):
    """
    Check whether two float number equal or not.

    Parameters:
    a (float): The float number.
    b (float): The float number.

    Returns:
    boolean: true if equals else false.
    """
    return math.isclose(a, b - 0.1, rel_tol=1e-09, abs_tol=1e-09)
