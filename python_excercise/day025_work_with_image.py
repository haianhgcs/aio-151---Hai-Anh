import cv2
import sys
import os
import matplotlib.pyplot as plt
sys.path.append("..")

IMAGE_PATH = os.path.abspath(os.getcwd()) + \
    "/data/kaggle_medical_dataset/2.jpg"

if __name__ == "__main__":
    from util import cv_util as cvuti

    print("original")
    img = cv2.imread(IMAGE_PATH, 0)
    plt.imshow(img, cmap='gray')
    plt.show()

    print("Kernel sigma=1.4")
    kernel = cvuti.gaussian_kernel(5, 1.4)
    img_gaussian = cv2.filter2D(img, -1, kernel)
    plt.imshow(img_gaussian, cmap='gray')
    plt.show()

    print("Kernel sigma=2.5")
    kernel = cvuti.gaussian_kernel(5, 2.5)
    img = cv2.imread(IMAGE_PATH, 0)
    img_gaussian = cv2.filter2D(img, -1, kernel)
    plt.imshow(img_gaussian, cmap='gray')
    plt.show()

    print("Kernel sigma=5.0")
    kernel = cvuti.gaussian_kernel(5, 5.0)
    img = cv2.imread(IMAGE_PATH, 0)
    img_gaussian = cv2.filter2D(img, -1, kernel)
    plt.imshow(img_gaussian, cmap='gray')
    plt.show()

    print("Kernel sigma=10.0")
    kernel = cvuti.gaussian_kernel(5, 10.0)
    img = cv2.imread(IMAGE_PATH, 0)
    img_gaussian = cv2.filter2D(img, -1, kernel)
    plt.imshow(img_gaussian, cmap='gray')
    plt.show()
