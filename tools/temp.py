# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:57:19 2022

@author: zm3171
"""

import os
import re
import sys
import cv2 
import numpy as np
 
 
mypath = r'D:\Workspace\PatchCore_anomaly_detection\mvtec_anomaly_detection\carpet0\ground_truth\thread'
fileList = os.listdir(mypath)                 # 待修改文件夹
print("修改前："+str(fileList))         # 输出文件夹中包含的文件
 
currentpath = os.getcwd()                   # 得到进程当前工作目录
os.chdir(mypath)                              # 将当前工作目录修改为待修改文件夹的位置
                                     # 名称变量
for fileName in fileList:                   # 遍历文件夹中所有文件
    pat=".+\.(jpg|png|jpeg)"                # 匹配文件名正则表达式
    pattern = re.findall(pat,fileName)
    new_name = int(fileName[:3])+70    # 进行匹配
    os.rename(fileName,(f'{new_name:03}'+'_mask'+'.'+pattern[0]))     #文件重新命名
                                 # 改变编号，继续下一项
                                     
#for fileName in fileList:
#    img_path = os.path.join(mypath,fileName)
#    img=cv2.imread(img_path)
#    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#    im_gray_th_otsu = 255-im_gray
#
#    cv2.imwrite(img_path,im_gray_th_otsu)                          
 
os.chdir(currentpath)                       # 改回程序运行前的工作目录
sys.stdin.flush()                           # 刷新
print("修改后："+str(os.listdir(mypath))) 


