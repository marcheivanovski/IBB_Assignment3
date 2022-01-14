import cv2
import os
import numpy as np

def histogram_equlization_rgb(img):
    # Simple preprocessing using histogram equalization 
    # https://en.wikipedia.org/wiki/Histogram_equalization

    intensity_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    intensity_img[:, :, 0] = cv2.equalizeHist(intensity_img[:, :, 0])
    img = cv2.cvtColor(intensity_img, cv2.COLOR_YCrCb2BGR)

    # For Grayscale this would be enough:
    # img = cv2.equalizeHist(img)

    return img

def equalize_and_write():
    directory = os.listdir('../../test_reshaped')
    #print(directory)

    for file in directory: 
        img = cv2.imread("../../test_reshaped/" + file, cv2.IMREAD_COLOR)
        img=histogram_equlization_rgb(img)
        cv2.imwrite("../../test_reshaped_equilized/" + file, img)


#SHARPEN IMAGES
def unsharp_mask(image, kernel_size=(5, 5), sigma=2.0, amount=1.0, threshold=0):
    blurred = cv2.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    sharpened = sharpened.round().astype(np.uint8)
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    return sharpened

def sharpen(image):
    kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    return image_sharp

def sharpen_and_write():
    directory = os.listdir('../../train_reshaped')
    #print(directory)

    for file in directory: 
        img = cv2.imread("../../train_reshaped/" + file, cv2.IMREAD_COLOR)
        img=sharpen(img)
        cv2.imwrite("../../dataset_sharpened/train/" + file, img)


sharpen_and_write()