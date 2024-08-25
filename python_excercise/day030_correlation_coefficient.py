import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

    return np.round(numerator / denominator, 4)


# Tạo hai mảng dữ liệu
data = pd.read_csv("./data/advertising.csv")
x = data['TV']
y = data['Radio']
# Tính toán hệ số tương quan
corr_coff = compute_correlation_cofficient(x, y)
print(f"Correlation between TV and Sales: {corr_coff}")

features = ['TV', 'Radio', 'Newspaper', 'Sales']
correlation_rows = []
i, j = 0, 0
for feature_1 in features:
    correlation_values = []
    for feature_2 in features:
        correlation_values.append(compute_correlation_cofficient(
            data[feature_1], data[feature_2]))
    correlation_rows.append(correlation_values)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_rows, annot=True, fmt=".2f", linewidths=.5)
plt.xticks(ticks=np.arange(4) + 0.5, labels=features, rotation=0)
plt.yticks(ticks=np.arange(4) + 0.5, labels=features, rotation=90)
plt.show()
