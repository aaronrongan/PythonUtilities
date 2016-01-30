# -*- coding: utf-8 -*-
"""
Created on 2016/1/21 15:30  

@author: A.Y

本模块目的：
"""


import csv
import chardet
import  pandas as pd

import pymssql
import Database.mssql
from Datayes.FundInfo import GetFundInfo,GetFundList
import time
from StringIO import  StringIO
from Database.General import  ConnectDB

start = time.time()

try:

    conn = ConnectDB()
    cursor=conn.cursor()
    # FundInfo=GetFundInfo()
    dataframe1=pd.read_csv('D:\MyDoc\Database\MyTradingSystem\Datayes\Fundinfo.csv',encoding="gbk")
    print dataframe1
    # dataframe1=pd.read_csv(StringIO(FundInfo))
    # print dataframe1
    dataframe1=dataframe1.fillna('')
    # print dataframe1
    TotalLen=len(dataframe1)
    iCount=0
    TotalLen=len(dataframe1)

    for iCount in range(TotalLen):
        Symbol=str(dataframe1.loc[iCount].ticker)
        print dataframe1.loc[iCount].custodianFullName
        custodianFullName=dataframe1.loc[iCount].custodianFullName#不解码会在SQL中乱码   基金托管人中文全称 .decode('utf-8')
        establishDate=dataframe1.loc[iCount].establishDate #
        listDate=dataframe1.loc[iCount].listDate
        indexFund=dataframe1.loc[iCount].indexFund #基金指数型属性，I为指数型，EI为指数增强型
        # if indexFund==None:
        #     indexFund='NULL'
        isClass=dataframe1.loc[iCount].isClass #是否分级基金,1为母基金,2为子基金A,3为子基金B,0为否
        category=str(dataframe1.loc[iCount].category)  #按投资对象分基金类型，E为股票型，H为混合型，B为债券型，SB为短期理财债券，M为货币型，O为其他
        operationMode=dataframe1.loc[iCount].operationMode #基金运作模式，O为开放式，C为封闭式
        circulationShares=dataframe1.loc[iCount].circulationShares

        sqlcommand = '''
                    Update FundInfo
                    Set custodianFullName=%s,establishDate=%s,listDate=%s,indexFund=%s,
                    isClass=%s,category=%s,operationMode=%s,circulationShares=%s
                     Where Symbol=%s
                    '''
        print sqlcommand
        # Value=(lambda x:x if x<>-1 else '')
        # print Value(indexFund)
        sqlvalue=(custodianFullName,establishDate,listDate,indexFund,isClass,category,operationMode,circulationShares,Symbol)
        print sqlvalue
        # iCount+=1
        # print str(iCount) + ":" + Symbol
        cursor.execute(sqlcommand,sqlvalue)
        conn.commit()

except Exception, e:
    print "error is:" + e.message
    raise e
finally:
    cursor.close()
    conn.close()

# 计算运算时间

end = time.time()
print end-start
