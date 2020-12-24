from cv2 import cv2  as cv


img = cv.imread("data/lena.jpg",cv.IMREAD_COLOR)

cv.line(img,(0,0),(img.shape[0],img.shape[1]),(100,100,50),6)

cv.rectangle(img,(50,50),(200,200),(0,255,0),8)


print(img.shape[0])

print(type(img))

cv.imshow("my",img)

cv.waitKey()

