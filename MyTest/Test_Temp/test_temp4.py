# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 10:23  

@author: A.Y

本模块目的：
"""


import os,sys
print sys.argv
print(os.listdir("d:/tmp/"))

def cdWalker(cdrom, cdcfile):
    export=''

    for root, dirs,files in os.walk(cdrom):
        #print root, dirs,files
        export+='\n %s %s %s' % (root,dirs,files)
    open(cdcfile,'w').write(export)