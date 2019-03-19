# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/2/22 11:27
import cv2

imagepath = "./timg.jpg"

image = cv2.imread(imagepath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(r'D:/python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# 探测人脸
# 根据训练的数据来对新图片进行识别的过程。
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.15,
                                      minNeighbors=5,
                                      minSize=(5, 5),
                                      # flags = cv2.HAAR_SCALE_IMAGE
                                      )

print ("发现{0}个人脸!".format(len(faces)))
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+w), (0, 255, 0), 2)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()