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

def calculate_activation():
    """
    Calculate activation sigmoid, relu, or elu

    Parameters:
    n (number): value to calculate activation.
    activation method (string): activation name, enter 'sigmoid', 'relu', or 'elu'
    
    Returns:
    float: activation value

    """

    user_input = input("Input a number: ")
    if not is_number(user_input):
        print("x must be a number")
        return
    x = float(user_input)
    
    activation_name = input("Input activation function (sigmoid|relu|elu): ")
    if activation_name == 'sigmoid':
        print(f"{activation_name}: f({x}) = {sigmoid(x)}") 
    elif activation_name == 'relu':
        print(f"{activation_name}: f({x}) = {relu(x)}")
    elif activation_name == 'elu':
        print(f"{activation_name}: f({x}) = {elu(x)}")
    else:
        print(f"{activation_name} is not supported")
        
        
calculate_activation()