from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("data/lena.jpg",cv2.IMREAD_GRAYSCALE)

cv2.imshow('lena',img)

print(cv2.__version__)

ch = cv2.waitKey(0)
if ch == ord('s'):
    cv2.imwrite("mylena.jpg",img)



plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # 隐藏 X 和 Y 轴的刻度值
plt.show()





cv2.destroyWindow("lena")

