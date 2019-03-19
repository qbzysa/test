# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/3/11 9:49

import cv2
import numpy as np


def showpiclocation(img, findimg):
    w = img.shape[1]
    h = img.shape[0]
    fw = findimg.shape[1]
    fh = findimg.shape[0]
    findpt = None
    for now_h in range(0, h-fh):
        for now_w in range(0, w-fw):
            comp_tz = img[now_h:now_h+fh, now_w:now_w+fw, :] - findimg
            if np.sum(comp_tz) < 1:
                findpt = now_w, now_h
    if findpt != None:
        cv2.rectangle(img, findpt, (findpt[0]+fw, findpt[1]+fh), (0, 0, 255))
    return img


if __name__ == "__main__":
    fn = './timg.jpg'
    fn1 = './1.png'
    fn2 = './2.png'
    myimg = cv2.imread(fn)
    myimg1 = cv2.imread(fn1)
    myimg2 = cv2.imread(fn2)
    myimg = showpiclocation(myimg, myimg1)
    myimg = showpiclocation(myimg, myimg2)
    cv2.namedWindow('3')
    cv2.imshow('3', myimg)
    cv2.imwrite('3.jpg', myimg)
    cv2.waitKey()
    cv2.destroyWindow()