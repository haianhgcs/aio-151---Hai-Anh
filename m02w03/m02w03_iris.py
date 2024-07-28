import numpy as np
import pandas as pd
import math
import sys
sys.path.append("..")


def calculate_gaussian_distribution(mean, variance, x):
    sigma = np.sqrt(variance)
    coefficient = 1 / (np.sqrt(2 * np.pi) * sigma)
    exponent = np.exp(- (x - mean) ** 2 / (2 * variance))
    return coefficient * exponent


if __name__ == "__main__":
    df_iris = pd.read_csv("./data/iris.csv")

    iris_0 = df_iris[df_iris["Class"] == 0]
    iris_1 = df_iris[df_iris["Class"] == 1]

    p_iris_0 = len(iris_0) / len(df_iris)
    p_iris_1 = len(iris_1) / len(df_iris)

    iris_0_mean = np.mean(iris_0["Length"])
    iris_0_variance = np.var(iris_0["Length"], ddof=0)
    print('Câu hỏi 11: Giá trị mean và variance của biến đầu vào (Length) cho "Class"="0" lần lượt là:')
    print(round(iris_0_mean, 3), round(iris_0_variance, 5))

    iris_1_mean = np.mean(iris_1["Length"])
    iris_1_variance = np.var(iris_1["Length"], ddof=0)
    print('Câu hỏi 12: Giá trị mean và variance của biến đầu vào (Length) cho "Class"="1" lần lượt là:')
    print(round(iris_1_mean, 3), round(iris_1_variance, 5))

    # Câu hỏi 13: Cho dữ liệu kiểm thử X = (Length=3.4). Xác suất dữ liệu kiểm thử X thuộc vào
    # "Class"="0" và "Class"="1" lần lượt là:
    iris_0_prob = calculate_gaussian_distribution(
        iris_0_mean, iris_0_variance, 3.4) * p_iris_0
    iris_1_prob = calculate_gaussian_distribution(
        iris_1_mean, iris_1_variance, 3.4) * p_iris_1
    print('Câu hỏi 13: Cho dữ liệu kiểm thử X = (Length=3.4). Xác suất dữ liệu kiểm thử X thuộc vào "Class"="0" và "Class"="1" lần lượt là:')
    print(iris_0_prob, iris_1_prob)
