import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
import sys
sys.path.append("..")

if __name__ == "__main__":
    from util import cv_util as cvuti

IMAGE_PATH = os.path.abspath(os.getcwd()) + \
    "/data/kaggle_medical_dataset/1.jpg"

print(IMAGE_PATH)
# Read image and display image
img = cv2.imread(IMAGE_PATH, 0)
# Display image using Matplotlib
plt.imshow(img, cmap='gray')
plt.show()

# Increase / Decrease brightness
# Read image
img = cv2.imread(IMAGE_PATH, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print("Original")
plt.imshow(img, cmap='gray')
plt.show()

# Increase brightness
print("Increase brightness")
new_img_inc = cvuti.change_brightness(img, 50)
# Display image using Matplotlib
plt.imshow(new_img_inc, cmap='gray')
plt.show()

# Decrease brightness
print("Decrease brightness")
new_img_dec = cvuti.change_brightness(img, -80)
# Display image using Matplotlib
plt.imshow(new_img_dec, cmap='gray')
plt.show()
