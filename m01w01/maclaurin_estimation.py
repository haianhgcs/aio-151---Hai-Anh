import math

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.
    
    Parameters:
    n (int): The non-negative integer.
    
    Returns:
    int: The factorial of the input number.
    """
    if n <= 0:
        raise ValueError("n must be a non-negative integer.")
    #elif n == 0:
    #    return 0
    #else:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

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
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
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
    for i in range(1,n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
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
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
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
    for i in range(1,n):
        term = (x ** (2 * i)) / math.factorial(2 * i)
        cosh += term
    return cosh

print(f"approximated sine value: {approx_sin(3.14, 10)}")
print(f"approximated cosine value: {approx_cos(3.14, 10)}")
print(f"approximated sinh value: {approx_sinh(3.14, 10)}")
print(f"approximated cosh value: {approx_cosh(3.14, 10)}")