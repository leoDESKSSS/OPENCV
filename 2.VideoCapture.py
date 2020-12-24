from cv2 import cv2
import time


capture = cv2.VideoCapture(0)

while(True):
    # 获取一帧
    ret, frame = capture.read()
    # 将这帧转换为灰度图
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    time.sleep(0.5)
    print(ret)
    if cv2.waitKey(1) == ord('q'):
        break