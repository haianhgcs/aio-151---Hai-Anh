import numpy as np


def compute_correlation_cofficient(X, Y):
    N = len(X)
    numerator = 0
    denominator = 0
    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    for x, y in zip(X, Y):
        numerator += x * y
    numerator = sum((X - mean_x) * (Y - mean_y))

    denominator = np.sqrt(sum((X - mean_x)**2) * sum((Y - mean_y) ** 2))

    return np.round(numerator / denominator, 2)


# Tạo hai mảng dữ liệu
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])
# Tính toán hệ số tương quan
corr_coff = compute_correlation_cofficient(X, Y)
print("Hệ số tương quan giữa X_new và Y_new là: ", corr_coff)

X_new = np.array([10, 20, 30, 40, 50])
Y_new = np.array([5, 15, 25, 35, 45])
corr_coff = compute_correlation_cofficient(X_new, Y_new)
print("Hệ số tương quan giữa X_new và Y_new là: ", corr_coff)

X_new = np.array([10, 20, 30, 40, 50])
Y_new = np.array([5, 1, 3, 7, 2])
corr_coff = compute_correlation_cofficient(X_new, Y_new)
print("Hệ số tương quan giữa X_new và Y_new là: ", corr_coff)

X_new = np.array([10, 20, 30, 40, 50])
Y_new = np.array([45, 35, 25, 15, 5])
corr_coff = compute_correlation_cofficient(X_new, Y_new)
print("Hệ số tương quan giữa X_new và Y_new là: ", corr_coff)
