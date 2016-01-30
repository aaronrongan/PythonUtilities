# -*- coding: utf-8 -*-
"""
Created on 2016/1/21 20:33  

@author: A.Y

本模块目的：
"""


import  pandas as pd
import csv
import chardet
import Database.General

import Datayes.IndexDaily
import pymssql
import Database.mssql
from Database.General import GetLatestDayofFundPrice_Correction,GetMaxiumIndexID,GetIndexSymbolList,ConnectDB
import time
import datetime
from StringIO import StringIO

start = time.time()

try:
    conn = ConnectDB()
    cursor=conn.cursor()

    # print indexID
    SymbolList=['000001'] #GetIndexSymbolList() #['000023']
    for Symbol in SymbolList:
        print Symbol
        iCount=0
        indexID=int(GetMaxiumIndexID())+1

        # LastWorkingDay=GetLatestDayofIndexPrice(Symbol)
        # # print LastWorkingDay
        # if LastWorkingDay<>None:
        #     year= int(LastWorkingDay.split('-')[0])
        #     month= int(LastWorkingDay.split('-')[1])
        #     day=int(LastWorkingDay.split('-')[2])
        #     LastWorkingDay= datetime.date(year, month, day)#time.strptime(GetLatestDayofIndexPrice(Symbol), "%Y-%m-%d")
        # else:
        #     LastWorkingDay=datetime.date(2000, 1, 1)

        # Today=datetime.date.today()
        EndDate=GetLatestDayofFundPrice_Correction(Symbol)

        # IndexData=Datayes.IndexDaily.GetIndexData(Symbol,str(LastWorkingDay + datetime.timedelta(1)),str(Today))
        IndexData=Datayes.IndexDaily.GetIndexData(Symbol,'1990-01-01',EndDate)
        # print IndexData
        # 这里用StringIO读取内存中的CSV文件
        dataframe1=pd.read_csv(StringIO(IndexData))
        # print dataframe1

        dataframe1=dataframe1.fillna(-1)

        TotalLen=len(dataframe1)
        sqlvaluelist=[]

        sqlcommand = '''
                    Update IndexPriceDaily
                    Set turnoverVol=%s, turnoverValue=%s
                     Where preClosePrice is NULL and TheDate=%s
                    '''

        for iCount in range(TotalLen):
            # VIP 必须要加int? 否则会报错ValueError: expected a simple type, a tuple or a list
            TheDate=dataframe1.loc[iCount].tradeDate
            turnoverVol=int(dataframe1.loc[iCount].turnoverVol)
            # print turnoverVol
            turnoverValue=int(dataframe1.loc[iCount].turnoverValue)

            # sqlcommand = '''INSERT INTO IndexPriceDaily (indexID, Symbol,TheDate,preClosePrice,openIndex,
            #                 highestIndex,lowestIndex,closeIndex,
            #                  turnoverVol,turnoverValue,CHG,CHGPct)
            #                   VALUES (%s,%s,%s,%s,%s,
            #                     %s,%s,%s,
            #                   %s,%s,%s,%s)'''
            # print "sqlcommand: " + sqlcommand
            sqlvalue=(turnoverVol,turnoverValue, TheDate)
            # indexID+=1
            # sqlvalue=(str(indexID),Symbol,TheDate,preClosePrice,openIndex,highestIndex,lowestIndex,closeIndex,turnoverVol,turnoverValue,CHG,CHGPct)

            sqlvaluelist.append(sqlvalue)
            cursor.execute(sqlcommand,sqlvalue)
            conn.commit()
            print sqlcommand,sqlvalue
            # print turnoverVol,turnoverValue
            # turnoverVol=1000000000

            # cursor.execute(sqlcommand) #,sqlvalue
            # cursor.execute(sqlcommand,(str(indexID), Symbol,TheDate,preClosePrice,openIndex,highestIndex,lowestIndex,closeIndex, turnoverVol, turnoverValue, CHG, CHGPct))
        # print sqlvaluelist
        # 批量执行插入
        # print TotalLen
        if TotalLen>0:
            # cursor.executemany(sqlcommand,sqlvaluelist)
            # conn.commit()
            print "Total %s Rows Added" % TotalLen
        else:
            print "No records added"


except Exception,e:
    raise e
finally:
    cursor.close()
    conn.close()

end = time.time()
print "Use " + str(end-start) + " Seconds"