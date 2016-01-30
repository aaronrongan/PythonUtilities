# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 13:40  

@author: A.Y

本模块目的：读写文件
"""
import sys
import os.path

# file=open("d:/2.txt",'r')
# #file.truncate(5)
# #file.write('this is ok\nthe second line')
# str=file.read()
# print str.__len__()
# file.close()

if os.path.exists('d:/5.txt'):
    print('file exist')
else:
    print('file not exist')
