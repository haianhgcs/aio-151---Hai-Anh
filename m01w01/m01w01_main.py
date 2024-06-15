import activation_metrics as act
import f1_score as f1
import loss_functions as lf
import utilities as ut
import random
import maclaurin_estimation as mac
import mean_difference_nth_root_error as md_nre
import math


def calculate_activation():
    """
    Calculate activation sigmoid, relu, or elu

    Parameters:
    n (number): value to calculate activation.
    activation method (string): activation name, enter 'sigmoid', 'relu', or 'elu'

    Returns:
    float: activation value

    """
    print("Calculate activation:")
    user_input = input("Input a number: ")
    if not ut.is_number(user_input):
        print("x must be a number")
        return
    x = float(user_input)

    activation_name = input("Input activation function (sigmoid|relu|elu): ")
    if activation_name == 'sigmoid':
        print(f"{activation_name}: f({x}) = {act.sigmoid(x)}")
    elif activation_name == 'relu':
        print(f"{activation_name}: f({x}) = {act.relu(x)}")
    elif activation_name == 'elu':
        print(f"{activation_name}: f({x}) = {act.elu(x)}")
    else:
        print(f"{activation_name} is not supported")


def calculate_loss():
    """
    Calculate loss MAE, MSE, or RMSE

    Parameters:
    num_samples (int): number of samples
    loss method (string): enter 'MSE', 'MAE', or 'RMSE'

    Returns:
    sring: loss name
    string: sample - sample order generated
    float: predict
    float: target

    """
    print("Calculate loss:")
    user_input = input(
        "Input number of samples ( integer number ) which are generated: ")
    if not ut.isnumeric(user_input):
        print("number of samples must be an integer number’")
        return
    num_samples = int(user_input)
    loss_name = input("Input loss function (MAE|MSE|RMSE): ").lower()

    for i in range(num_samples):
        predict = [random.uniform(0, 10)]  # random value in range [0,10)
        target = [random.uniform(0, 10)]  # random value in range [0,10)
        if loss_name == 'mae':
            print(
                f"loss name: {loss_name.upper()}, sample: {i}, pred: {predict}, target: {target}, loss: {lf.mae_loss(predict, target)}")
        elif loss_name == 'mse':
            print(
                f"loss name: {loss_name.upper()}, sample: {i}, pred: {predict}, target: {target}, loss: {lf.mse_loss(predict, target)}")
        elif loss_name == 'rmse':
            print(
                f"loss name: {loss_name.upper()}, sample: {i}, pred: {predict}, target: {target}, loss: {lf.rmse_loss(predict, target)}")
        else:
            print(f"{loss_name.upper()} is not supported")


def calc_activation_func(x, act_name):
    """
    Calculate activation sigmoid, relu, or elu

    Parameters:
    n (number): value to calculate activation.
    activation method (string): activation name, enter 'sigmoid', 'relu', or 'elu'

    Returns:
    float: activation value

    """

    if not ut.is_number(x):
        print("x must be a number")
        return

    if act_name == 'sigmoid':
        print(f"{act_name}: f({x}) = {act.sigmoid(x)}")
        return act.sigmoid(x)
    elif act_name == 'relu':
        print(f"{act_name}: f({x}) = {act.relu(x)}")
        return act.relu(x)
    elif act_name == 'elu':
        print(f"{act_name}: f({x}) = {act.elu(x)}")
        return act.elu(x)
    else:
        print(f"{act_name} is not supported")


def calc_ae(y, y_hat):
    absolute_errors = abs(y - y_hat)

    return absolute_errors


def calc_se(y, y_hat):
    squared_errors = (y - y_hat)**2

    return squared_errors


if __name__ == "__main__":
    # 1. Viết function thực hiện đánh giá classification model bằng F1-Score.
    # Example usage:
    # precision, recall, f1 = f1.evaluate_f1_score(2, 3, 5)
    # print(f"precision: {precision} recall: {recall} F1 Score: {f1}")

    # 2. Viết function mô phỏng theo 3 activation function
    # calculate_activation()

    # 3. Viết function lựa chọn regression loss function để tính loss
    # calculate_loss()

    # 4. Viết 4 functions để ước lượng các hàm số sau.
    # print(f"approximated sine value: {mac.approx_sin(3.14, 10)}")
    # print(f"approximated cosine value: {mac.approx_cos(3.14, 10)}")
    # print(f"approximated sinh value: {mac.approx_sinh(3.14, 10)}")
    # print(f"approximated cosh value: {mac.approx_cosh(3.14, 10)}")

    # 5. Viết function thực hiện Mean Difference of nth Root Error:
    # print(md_nre.mean_difference_nth_root_error_single_sample(100, 99.5, 2, 1))

    # Câu hỏi 1
    assert ut.float_equals(
        round(f1.evaluate_f1_score(tp=2, fp=3, fn=5), 2), 0.33) == False
    print(round(f1.evaluate_f1_score(tp=2, fp=4, fn=5), 2))

    # Câu hỏi 2
    assert ut.float_equals(ut.is_number(3), 1.0) == False
    assert ut.float_equals(ut.is_number('-2a'), 0.0) == False
    print(ut.is_number(1))
    print(ut.is_number('n'))

    # Câu hỏi 4
    calc_sig = act.sigmoid
    assert ut.float_equals(round(calc_sig(3), 2), 0.95) == False
    print(round(calc_sig(2), 2))

    # Câu hỏi 5
    calc_elu = act.elu
    assert round(calc_elu(1, 0.01)) == 1
    print(round(calc_elu(-1, 0.01), 2))

    # Câu hỏi 6
    assert round(calc_activation_func(x=1, act_name='relu'), 0) == 1
    print(round(calc_activation_func(x=3, act_name='sigmoid'), 2))

    # Câu hỏi 7
    y = 1
    y_hat = 6
    assert calc_ae(y, y_hat) == 5
    y = 2
    y_hat = 9
    print(calc_ae(y, y_hat))

    # Câu hỏi 8
    y = 4
    y_hat = 2
    assert calc_se(y, y_hat) == 4
    print(calc_se(2, 1))

    # Câu hỏi 9
    approx_cos = mac.approx_cos
    assert ut.float_equals(round(approx_cos(x=1, n=10), 2), 0.54) == False
    print(round(approx_cos(x=3.14, n=10), 2))

    # Câu hỏi 10
    approx_sin = mac.approx_sin
    assert ut.float_equals(round(approx_sin(x=1, n=10), 4), 0.8415) == False
    print(round(approx_sin(x=3.14, n=10), 4))

    # Câu hỏi 11
    approx_sinh = mac.approx_sinh
    assert ut.float_equals(round(approx_sinh(x=1, n=10), 2), 1.18) == False
    print(round(approx_sinh(x=3.14, n=10), 2))

    # Câu hỏi 12
    approx_cosh = mac.approx_cosh
    assert ut.float_equals(round(approx_cosh(x=1, n=10), 2), 1.54) == False
    print(round(approx_cosh(x=3.14, n=10), 2))
