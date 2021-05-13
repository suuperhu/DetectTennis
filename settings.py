# -*- coding: utf-8 -*-
"""
# @FileName             : settings.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    : 
# @EnFileDescription    : 
"""
from pathlib import Path
import cv2 as cv
import numpy as np
from utils import createCircleKernel

PROJECT_PATH = Path(__file__).resolve().parent

# 相机设备文件
DEVICE = "./data/3.mp4"

# 彩色图像均衡化参数
HIS_EQU_COLOR = True

# 高斯滤波参数
GAUSSIAN_BLUR_KSIZE = (3, 3)
GAUSSIAN_BLUR_SIGMAX = 0
GAUSSIAN_BLUR_SIGMAY = 0

# 均值滤波参数
BLUR_KSIZE = (5, 5)

# 中值滤波参数
MEDIAN_BLUR_KSIZE = 5

# 色域分割参数
HSV_LOWER = np.array([15, 50, 60])
HSV_UPPER = np.array([45, 255, 255])

# 膨胀腐蚀参数
# DILATE_KERNEL = createCircleKernel(5)
# DILATE_ITERATIONS = 1
# ERODE_KERNEL = createCircleKernel(5)
# ERODE_ITERATIONS = 1
DILATE_KERNEL = None
DILATE_ITERATIONS = 1
ERODE_KERNEL = None
ERODE_ITERATIONS = 1

# 形态检测参数
PI = 3.14
AREA_RATE = 0.7
METHOD = cv.HOUGH_GRADIENT
DP = 1
MIN_DIST = 5
PARAM1 = 200
PARAM2 = 0.5
MIN_RADIUS = 10
MAX_RADIUS = 80
MAX_ABS_X = 20
MAX_ABS_Y = 20
MAX_ABS_R = 20
MIN_VOTE = 25

if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))


    def test_project_path():
        """
        test project path
        """
        project_name = str(PROJECT_PATH).split('/')[-1]
        assert project_name == "DetectTennis"


    test_project_path()