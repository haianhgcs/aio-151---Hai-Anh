import math


def mae_loss(y_true, y_pred):
    """
    Calculate the Mean Absolute Error (MAE) between true and predicted values.

    Parameters:
    y_true (list or array-like): True values.
    y_pred (list or array-like): Predicted values.

    Returns:
    float: The MAE between the true and predicted values.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("The length of y_true and y_pred must be the same.")

    absolute_errors = [abs(true - pred) for true, pred in zip(y_true, y_pred)]
    mae = sum(absolute_errors) / len(absolute_errors)
    return mae


def mse_loss(y_true, y_pred):
    """
    Calculate the Mean Squared Error (MSE) between true and predicted values.

    Parameters:
    y_true (list or array-like): True values.
    y_pred (list or array-like): Predicted values.

    Returns:
    float: The MSE between the true and predicted values.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("The length of y_true and y_pred must be the same.")

    squared_errors = [(true - pred) ** 2 for true, pred in zip(y_true, y_pred)]
    mse = sum(squared_errors) / len(squared_errors)
    return mse


def rmse_loss(y_true, y_pred):
    """
    Calculate the Root Mean Squared Error (RMSE) between true and predicted values.

    Parameters:
    y_true (list or array-like): True values.
    y_pred (list or array-like): Predicted values.

    Returns:
    float: The RMSE between the true and predicted values.
    """
    if len(y_true) != len(y_pred):
        raise ValueError("The length of y_true and y_pred must be the same.")

    squared_errors = [(true - pred) ** 2 for true, pred in zip(y_true, y_pred)]
    mse = sum(squared_errors) / len(squared_errors)
    rmse = math.sqrt(mse)
    return rmse
