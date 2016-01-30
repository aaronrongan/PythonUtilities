# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 11:18  
@author: A.Y

@本模块目的
"""
import sys
from sys import argv

filename=argv[0]
print "File name:" + filename
#print "you input:" + first

txt=open(filename)
print txt.read().decode('utf-8').encode('gb18030') #decode('utf-8', 'ignore').encode('utf-8')