import cv2
import numpy as np

image = cv2.imread('lion.png', cv2.IMREAD_GRAYSCALE)
print(image.shape)
mask = np.ones((3, 3), dtype='uint8') * (1/255)
print(mask)

result = np.zeros((1024, 1024), dtype='uint8')

rows, cols = image.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_image = image[i-1:i+2, j-1:j+2]
        besco = np.multiply(small_image, mask)
        out = np.sum(besco)
        result[i, j] = out

cv2.imshow('output', result)
cv2.imwrite('lion_output.jpg', result)
cv2.waitKey()