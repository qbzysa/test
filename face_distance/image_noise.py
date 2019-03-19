# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/3/11 10:18
import cv2
import numpy as np


def addnoise(img):
    cout = 50000
    for k in range(cout):
        xi = int(np.random.uniform(0, img.shape[1]))
        xj = int(np.random.uniform(0, img.shape[0]))
        img[xj, xi, 0] = 255 * np.random.rand()
        img[xj, xi, 1] = 255 * np.random.rand()
        img[xj, xi, 2] = 255 * np.random.rand()


if __name__ == "__main__":
    fn = './timg.jpg'
    myimg = cv2.imread(fn)
    addnoise(myimg)
    cv2.namedWindow('noise')
    cv2.imshow('noise', myimg)
    cv2.imwrite('noise.jpg', myimg)
    cv2.waitKey()
    cv2.destroyWindow()