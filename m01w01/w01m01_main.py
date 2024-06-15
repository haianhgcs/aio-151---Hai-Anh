import activation_metrics as act
import f1_score as f1
import loss_functions as lf
import utilities as ut
import random
import maclaurin_estimation as mac
import mean_difference_nth_root_error as md_nre


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


if __name__ == "__main__":
    # 1. Viết function thực hiện đánh giá classification model bằng F1-Score.
    # Example usage:
    precision, recall, f1 = f1.evaluate_f1_score(2, 3, 5)
    print(f"precision: {precision} recall: {recall} F1 Score: {f1}")

    # 2. Viết function mô phỏng theo 3 activation function
    calculate_activation()

    # 3. Viết function lựa chọn regression loss function để tính loss
    calculate_loss()

    # 4. Viết 4 functions để ước lượng các hàm số sau.
    print(f"approximated sine value: {mac.approx_sin(3.14, 10)}")
    print(f"approximated cosine value: {mac.approx_cos(3.14, 10)}")
    print(f"approximated sinh value: {mac.approx_sinh(3.14, 10)}")
    print(f"approximated cosh value: {mac.approx_cosh(3.14, 10)}")

    # 5. Viết function thực hiện Mean Difference of nth Root Error:
    print(md_nre.mean_difference_nth_root_error_single_sample(100, 99.5, 2, 1))
