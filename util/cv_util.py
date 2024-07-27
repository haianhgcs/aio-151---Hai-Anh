import numpy as np
import cv2
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
