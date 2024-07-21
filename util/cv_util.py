import numpy as np
import math


def change_brightness(img, delta):
    new_img = img.astype(np.float32) + delta
    new_img = np.clip(new_img, 0, 255)
    new_img = new_img.astype(np.uint8)

    return new_img


def gaussian_kernel(size, sigma):
    if size % 2 == 0:
        size = size + 1

    max_point = size // 2  # both direction (x, y) maximum cell start point
    min_point = - max_point  # both direction (x, y) minimum cell start point

    K = np.zeros((size, size))  # kernel matrix
    for x in range(min_point, max_point + 1):
        for y in range(min_point, max_point+1):
            value = (2 * math.pi * (sigma ** 2)) ** (-1) * \
                math.exp(- (x ** 2 + y ** 2)/2 * (sigma ** 2))
            K[x - min_point, y - min_point] = value

    return K
