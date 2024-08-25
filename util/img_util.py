import numpy as np


def img_convert_to_gray_lightness(image):
    """
    Calculate image to gray using Lightness approach.

    Parameters:
    image (numpy.ndarray): input color image with shape (Height, Width, 3).

    Returns:
    numpy.ndarray: output gray image with shape (Height, Width).
    """
    # Get max and min corresponding to each pixel
    max_rgb = np.max(image, axis=2)
    min_rgb = np.min(image, axis=2)

    # Calculate lightness value
    lightness = (max_rgb + min_rgb) / 2

    return lightness  # .astype(np.uint8)


def img_convert_to_gray_average(image):
    """
    Calculate image to gray using Average approach.

    Parameters:
    image (numpy.ndarray): input color image with shape (Height, Width, 3).

    Returns:
    numpy.ndarray: output gray image with shape (Height, Width).
    """
    # Calculate average value
    average = np.mean(image, axis=2)

    return average  # .astype(np.uint8)


def img_convert_to_gray_luminosity(image):
    """
    Calculate image to gray using Luminosity method.

    Parameters:
    image (numpy.ndarray): input color image with shape (Height, Width, 3).

    Returns:
    numpy.ndarray: output gray image with shape (Height, Width).
    """
    # Tính giá trị luminosity
    luminosity = 0.21 * image[:, :, 0] + 0.72 * \
        image[:, :, 1] + 0.07 * image[:, :, 2]

    return luminosity  # .astype(np.uint8)
