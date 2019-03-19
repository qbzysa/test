# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2019/3/11 10:37
# 大量噪声定位图像

import cv2
import numpy as np


def get_EuclideanDistance(x, y):
    myx = np.array(x)
    myy = np.array(y)
    return np.sqrt(np.sum((myx-myy)*(myx-myy)))


def findpic(img, findimg, h, fh, w, fw):
    minds = 1E8
    mincb_h = 0
    mincb_w = 0
    for now_h in range(h-fh):
        for now_w in range(w-fw):
            my_img = img[now_h:now_h+fh, now_w:now_w+fw, :]
            my_findimg = findimg
            dis = get_EuclideanDistance(my_img, my_findimg)
            if dis < minds:
                minds = dis
                mincb_h = now_h
                mincb_w = now_w
    findpt = mincb_w, mincb_h
    cv2.rectangle(img, findpt, (findpt[0] + fw, findpt[1] + fh), (0, 0, 255))
    return img


def showpiclocation2(img, findimg):
    # 定位图像
    w = img.shape[1]
    h = img.shape[0]
    fw = findimg.shape[1]
    fh = findimg.shape[0]
    return findpic(img, findimg, h, fh, w, fw)


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
    fn1 = './1.png'
    fn2 = './2.png'
    myimg = cv2.imread(fn)
    myimg1 = cv2.imread(fn1)
    myimg2 = cv2.imread(fn2)
    addnoise(myimg)
    myimg = showpiclocation2(myimg, myimg1)
    myimg = showpiclocation2(myimg, myimg2)
    cv2.namedWindow('img1')
    cv2.imshow('img1', myimg)
    cv2.imwrite('img1.jpg', myimg)
    cv2.waitKey()
    cv2.destroyWindow()

