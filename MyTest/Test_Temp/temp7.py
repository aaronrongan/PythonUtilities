# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 13:50  

@author: A.Y

本模块目的：
"""
import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# def func1(*arg):
#     arg1=arg[0]
#     print arg1
#
# def func2(arg1,arg2):
#     arg1=arg1
#     arg2=arg2
#     print arg1, arg2
#
# func1("hello")
# func2('yes','no')
#
# def print_all(f):
#     print f.read()
#
# def print_rewind(f):
#     print f.seek(0)
#
# def print_readline(f):
#     print f.readline()
#
#
# file=open('d:/2.txt')
#
# print_all(file)
# print "==============="
# print_rewind(file)
# print "==============="
# print_readline(file)
# print_readline(file)
# print_readline(file)
# print_readline(file)

# def func_cal1(stuff):
#     "ffdf"
#     return stuff.split(' ')
#
# print func_cal1('gekkkfd fdfd lfdf')

# def func_comp(d1,d2):
#     if d1<>d2:
#         print "不相等"
#         if d1>d2:
#             print"大于"
#         else:
#             print "小于"
#     elif d1==d2:
#         print"相等"
#
# func_comp(3,3)

#
# list1=[10,2,3,'fdfd']
# list2=['fdf','dfd','de','bfd']
#
# result=list2[1:2]
# print result
# print(list2.__len__())
# for value in list2:
#     print value.len()

# i=0
# numbers=[]
#
# # numbers.append(7)
#
# while i<7:
#     numbers.append(i)
#     print numbers[i]
#     i+=1
#
# raw_input()
#
# class parent():
#     def __init__(self):
#         print(10)
#
#     def fun1(self):
#         print "parent"
#
# class child(parent):
#     def fun1(self):
#
#         print "child"
#
#     def fun1(self,var):
#         print var
#
# dad=parent()
# dad.fun1()
# child=child()
# child.fun1()
# child.fun1(10)

# s=pd.Series([1,2,3,4,5,np.nan])
# print s
#
# dates=pd.date_range('20130101',periods=3)
# print dates
#
# df=pd.DataFrame(np.random.rand(3,3),dates,list('ABC'))
# print df
#
#
# # df2=pd.DataFrame({'A':'1','B':'2'})
# # print df2
#
# print df.dtypes
#
# print df.head(1)
#
# print df.values
#
# #print df.columns()   Why not work?
#
# print df.describe()
#
#
# print df['A']
# print '========='
# print df[1:2]
# print '========='
# print df.at[dates[0],'A']
# print '========='
# print df.mean(0)

# df=pd.DataFrame(np.random.randn(10,4))
# print df
#
# pieces=[df[0:3],df[3:7],df[7:]]
# print pieces[0]
# pd.concat(pieces)

ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
#ts=ts.cumsum()
ts.plot()

