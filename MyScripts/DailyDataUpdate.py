# -*- coding: utf-8 -*-
"""
Created on 2016/1/21 22:10  

@author: A.Y

本模块目的：日常股票、基金、指数等数据更新批处理
"""
# import MyScripts.UpdateStockData_Datayes
import MyScripts.InsertStockData_Datayes
import MyScripts.InsertIndexData_Datayes
import MyScripts.InsertFundData_Datayes
from MyScripts.InsertStockData_Datayes import InsertStockData_Datayes
from MyScripts.InsertIndexData_Datayes import  InsertIndexData_Datayes
from MyScripts.InsertFundData_Datayes import  InsertFundData_Datayes

print '补全股票数据'
InsertStockData_Datayes()

print '补全指数数据'
InsertIndexData_Datayes()

print '补全基金数据'
InsertFundData_Datayes()

