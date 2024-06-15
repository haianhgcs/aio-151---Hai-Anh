def is_number(x):
    """
    Check if input is numeric type or not

    Parameters:
    x (string): number to validate.
    
    Returns:
    bool: True if n is numeric, else return False

    """
    try:
        float(x)          # Type-casting the string to 'float'
                          # If string is not a valid 'float',
                          # it'll raise "ValueError" exception
    except ValueError:
        return False
    return True

def isnumeric(x):
    """
    Check if input is numeric type or not

    Parameters:
    x (string): number to validate.
    
    Returns:
    bool: True if n is numeric, else return False

    """
    try:
        int(x)          # Type-casting the string to 'int'
                        # If string is not a valid 'int',
                        # it'll raise "ValueError" exception
    except ValueError:
        print("number of samples must be an integer number")
        return False
    return True

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