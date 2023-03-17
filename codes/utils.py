#!/usr/bin/env python

import cv2
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc, ndimage

def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")
    s = pts.sum(axis = 1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
 
    return rect

def four_point_transform(image, pts):
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
 
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
 
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = "float32")
 
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped
    
def SIFT_Rect(img1, img2, qimg, thresh):
    image = img2

    sift = cv2.SIFT_create()# SIFT特征提取对象

    kp1, des1 = sift.detectAndCompute(img1,None)# 关键点位置，des为特征向量
    kp2, des2 = sift.detectAndCompute(img2,None)

    bf = cv2.BFMatcher()# 匹配对象
    matches = bf.knnMatch(des1,des2, k=2) # 进行两个特征矩阵的匹配

    good = []
    for m,n in matches:
            if m.distance < thresh*n.distance:#根据Lowe的论文，丢弃任何距离大于0.7的值，则可以避免几乎90%的错误匹配，但是好的匹配结果也会很少。
                good.append(m)

    if len(good)>5:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w = img1.shape  # 获得原图像的高和宽
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)  # 使用得到的变换矩阵对原图像的四个角进行变换,获得在目标图像上对应的坐标。
        dst = cv2.perspectiveTransform(pts,M)

        img2 = cv2.polylines(img2,[np.int32(dst)],True,[0,255,0],3, cv2.LINE_AA) # 在原图中画出目标所在位置框, cv2.LINE_AA表示闭合框

    draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                       singlePointColor = None,
                       matchesMask = matchesMask, # draw only inliers
                       flags = 2)

    pts = np.int32(dst)[:,0]

    warped = four_point_transform(image, pts)
    
    res = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

    cv2.imwrite('{}_match_result.jpg'.format(qimg), res)
    cv2.imwrite('{}_warped.jpg'.format(qimg), warped)

    return 0
