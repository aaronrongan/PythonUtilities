# -*- coding: utf-8 -*-
"""
Created on 2016/1/19 16:28  

@author: A.Y

本模块目的：插入指数数据，
"""

import gmsdk as gs
from gmsdk import md
from gmsdk import td
from gmsdk import DailyBar
import  pandas as pd
import csv
import chardet
import Database.General

#import Datayes.IndexInfo
import pymssql
import Database.mssql
from GoldMiner.Index import GetIndexData
from Database.General import GetLatestDayofIndexPrice,GetMaxiumIndexID,GetIndexSymbolList,GetIndexSymbolFullList,ConnectDB
import time
import datetime

start = time.time()

try:
    conn = ConnectDB()
    cursor=conn.cursor()
    indexID=int(GetMaxiumIndexID())+1
    # print indexID
    SymbolList=GetIndexSymbolFullList()
    for Symbol in SymbolList:
        print Symbol
        iCount=0
        LastingWorkingDay=GetLatestDayofIndexPrice(Symbol)
        if LastingWorkingDay<>None:
            year= int(LastingWorkingDay.split('-')[0])
            month= int(LastingWorkingDay.split('-')[1])
            day=int(LastingWorkingDay.split('-')[2])
            LastingWorkingDay= datetime.date(year, month, day)#time.strptime(GetLatestDayofIndexPrice(Symbol), "%Y-%m-%d")
        else:
            LastingWorkingDay=datetime.date(2000, 1, 1)
        print LastingWorkingDay
        Today=datetime.date.today()
        # print Today
        # if LastingWorkingDay<Today:
        #     print LastingWorkingDay
        dailybars=GetIndexData(Symbol,str(LastingWorkingDay + datetime.timedelta(1)),str(Today))
        sqlvaluelist=[]

        sqlcommand = '''INSERT INTO IndexPriceDaily (indexID, Symbol,TheDate,preClosePrice,openIndex,
                            highestIndex,lowestIndex,closeIndex,
                             turnoverVol,turnoverValue)
                              VALUES (%s,%s,%s,%f,%f,
                                %f,%f,%f,
                              %f,%f)'''

        for db in dailybars:
            preClosePrice=db.pre_close
            openIndex=db.open
            highestIndex=db.high
            lowestIndex=db.low
            closeIndex=db.close
            turnoverVol=db.volume
            turnoverValue=db.amount
            TheDate=db.strtime.split("T")[0]
            iCount+=1

            # ??? TypeError: an integer is required ???
            #这里的%d会有问题，因为是整数，而不是分数。可以直接用%s，导入数据库时自动转为浮点数

            indexID+=1
            sqlvalue=(str(indexID),Symbol,TheDate,preClosePrice,openIndex,highestIndex,lowestIndex,closeIndex,turnoverVol,turnoverValue)
            sqlvaluelist.append(sqlvalue)

            # cursor.execute(sqlcommand)
        # print sqlvaluelist
        # 批量执行插入
        if len(dailybars)>0:
            cursor.executemany(sqlcommand,sqlvaluelist)
            conn.commit()
            print "Total %s Rows Added" % iCount
        else:
            print "No records added"


except Exception,e:
    raise e
finally:
    cursor.close()
    conn.close()

end = time.time()
print "Use " + str(end-start) + " Seconds"