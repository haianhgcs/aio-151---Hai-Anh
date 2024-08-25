import numpy as np
import cv2
import math
import matplotlib.pyplot as plt


def compute_difference(bg_img, input_img):
    if bg_img.shape != input_img.shape:
        raise ValueError("Two matrixes must have same shape")

    difference_single_channel = bg_img - input_img

    return difference_single_channel


def compute_binary_mask(matrix, threshold=0):
    binary_mask = matrix > threshold
    binary_mask = np.where(binary_mask == True, 255, 0)

    return binary_mask


def replace_background(bg1_image, bg2_image, ob_image):
    diference_single_channel = compute_difference(bg1_image, ob_image)
    plt.imshow(diference_single_channel)
    plt.show()

    binary_mask = compute_binary_mask(diference_single_channel)
    plt.imshow(binary_mask)
    plt.show()

    output = np.where(binary_mask == 255, ob_image, bg2_image)
    plt.imshow(output)
    plt.show()

    return output


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
