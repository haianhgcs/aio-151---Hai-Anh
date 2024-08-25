import numpy as np
import pandas as pd
import matplotlib.image as mping
import sys
sys.path.append("..")


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


if __name__ == "__main__":
    from util import img_util

    print("Câu #1: A")
    arr = np.arange(0, 10, 1)
    print(arr)

    print("Câu #2: D")
    arr = np.full((3, 3), fill_value=True, dtype=bool)
    print(arr)
    arr = np.ones((3, 3)) > 0
    print(arr)
    arr = np.ones((3, 3), dtype=bool)
    print(arr)

    print("Câu #3: A")
    arr = np.arange(0, 10)
    print(arr[arr % 2 == 1])

    print("Câu #4: B")
    arr = np.arange(0, 10)
    arr[arr % 2 == 1] = -1
    print(arr)

    print("Câu #5: B")
    arr = np.arange(10)
    arr_2d = arr.reshape(2, -1)
    print(arr_2d)

    print("Câu #6: A")
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=0)
    print("Result: \n", c)

    print("Câu #7: C")
    arr1 = np.arange(10).reshape(2, -1)
    arr2 = np.repeat(1, 10).reshape(2, -1)
    c = np.concatenate([arr1, arr2], axis=1)
    print("Result: \n", c)

    print("Câu #8: A")
    arr = np.array([1, 2, 3])
    print(np.repeat(arr, 3))
    print(np.tile(arr, 3))

    print("Câu #9: C")
    a = np.array([2, 6, 1, 9, 10, 3, 27])
    index = np.where((a >= 5) & (a <= 10))
    print("result", a[index])

    print("Câu #10: C")
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])

    pair_max = np.vectorize(maxx, otypes=[float])
    print(pair_max(a, b))

    print("Câu #11: B")
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    print("Result", np.where(a < b, b, a))

    print("Câu #12: A")
    img = mping.imread("./data/dog.jpeg")
    gray_img_01 = img_util.img_convert_to_gray_lightness(img)
    print(gray_img_01[0, 0])

    print("Câu #13: A")
    gray_img_01 = img_util.img_convert_to_gray_average(img)
    print(gray_img_01[0, 0])

    print("Câu #14: C")
    gray_img_01 = img_util.img_convert_to_gray_luminosity(img)
    print(gray_img_01[0, 0])

    df = pd.read_csv('./data/advertising.csv')
    data = df.to_numpy()

    print("Câu #15: C")
    max_values = np.max(data[:, 3], axis=0)
    max_indices = np.argmax(data[:, 3], axis=0)
    print("Max: ", max_values, " - Index: ", max_indices)

    print("Câu #16: B")
    avg_values = np.average(data[:, 0], axis=0)
    print("Avg: ", avg_values)

    print("Câu #17: A")
    count = np.sum(data[:, 3] >= 20)
    print(count)

    print("Câu #18: B")
    # Filter rows have Sales >= 15
    filtered_data = data[data[:, 3] >= 15]
    # Calculate average of Radio from filtered row
    average_radio = np.mean(filtered_data[:, 1])
    print(average_radio)

    print("Câu #19: C")
    average_newspaper = np.mean(data[:, 2])
    filtered_data = data[data[:, 2] >= average_newspaper]
    sum_newspaper = np.sum(filtered_data[:, 3])
    print(sum_newspaper)

    print("Câu #20: C")
    mean_sale = np.mean(data[:, 3])
    scores = np.array(["Good" if x > mean_sale else "Average" if x ==
                      mean_sale else "Bad" for x in data[:, 3]])
    print(scores[7:10])

    print("Câu #21: C")
    mean_sale = np.mean(data[:, 3])
    min_abs_to_mean_sale = data[:, 3][np.abs(data[:, 3] - mean_sale).argmin()]
    scores = np.array(["Good" if x > min_abs_to_mean_sale else "Average" if x ==
                      min_abs_to_mean_sale else "Bad" for x in data[:, 3]])
    print(scores[7:10])
