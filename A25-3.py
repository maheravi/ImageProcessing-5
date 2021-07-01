import cv2
import numpy as np

image = cv2.imread('building.tif', cv2.IMREAD_GRAYSCALE)
print(image.shape)
mask1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
mask2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

result = np.zeros((600, 600), dtype='uint8')

rows, cols = image.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_image = image[i-1:i+2, j-1:j+2]
        besco = np.multiply(small_image, mask2)
        out = np.sum(besco)
        if out <=0:
            out=0
        result [i, j] = out

cv2.imshow('output', result)
cv2.imwrite('buildin2_output.jpg', result)
cv2.waitKey()