def mean_difference_nth_root_error_single_sample(actual_value, estimated_value, n, p):
    """
    Calculate the Mean Difference of the nth Root Error between actual and estimated value.
    
    Parameters:
    actual_value (int or float): The actual value.
    estimated_values (int or float): The estimated value.
    n (int): The root order.
    
    Returns:
    float: The mean difference of the nth root error.
    """
    #if len(actual_value) != len(estimated_value):
    #    raise ValueError("The lengths of actual_values and estimated_values must be the same.")
    
    #total_error = 0
    #for actual, estimated in zip(actual_values, estimated_values):
    #    error = actual** (1 / n) - estimated** (1 / n)
    #    nth_root_error = error ** (p)
    #    total_error += nth_root_error
    #mean_error = total_error / len(actual_values)
    
    error = actual_value** (1 / n) - estimated_value** (1 / n)
    error = error ** (p)
    
    return error

def mean_difference_nth_root_error(actual_values, estimated_values, n, p):
    """
    Calculate the Mean Difference of the nth Root Error between actual and estimated value.
    
    Parameters:
    actual_value (int or float): The actual value.
    estimated_values (int or float): The estimated value.
    n (int): The root order.
    
    Returns:
    float: The mean difference of the nth root error.
    """
    if len(actual_values) != len(estimated_values):
        raise ValueError("The lengths of actual_values and estimated_values must be the same.")
    
    total_error = 0
    for actual, estimated in zip(actual_values, estimated_values):
        error = actual** (1 / n) - estimated** (1 / n)
        nth_root_error = error ** (p)
        total_error += nth_root_error
    mean_error = total_error / len(actual_values)
    
    return error