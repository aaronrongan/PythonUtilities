# -*- coding: utf-8 -*-
"""
Created on 2016/1/20 10:30  

@author: A.Y

本模块目的：用Datayes的指数价格数据填充SQL 数据库
"""
import  pandas as pd
import csv
import chardet
import Database.General

import Datayes.IndexDaily
import pymssql
import Database.mssql
from Database.General import GetLatestDayofIndexPrice,GetMaxiumIndexID,GetIndexSymbolList,GetIndexSymbolFullList,ConnectDB
import time
import datetime
from StringIO import StringIO
def InsertIndexData_Datayes():
    start = time.time()

    try:
        conn = ConnectDB()
        cursor=conn.cursor()

        # print indexID
        SymbolList= GetIndexSymbolFullList() #['000023']
        for Symbol in SymbolList:
            print Symbol
            iCount=0
            # indexID=int(GetMaxiumIndexID())+1

            LastWorkingDay=GetLatestDayofIndexPrice(Symbol)

            # print LastWorkingDay
            if LastWorkingDay<>None:
                year= int(LastWorkingDay.split('-')[0])
                month= int(LastWorkingDay.split('-')[1])
                day=int(LastWorkingDay.split('-')[2])
                LastWorkingDay= datetime.date(year, month, day)#time.strptime(GetLatestDayofIndexPrice(Symbol), "%Y-%m-%d")
            else:
                LastWorkingDay=datetime.date(1990, 1, 1)

            Today=datetime.date.today()
            IndexData=Datayes.IndexDaily.GetIndexData(Symbol,str(LastWorkingDay + datetime.timedelta(1)),str(Today))
            # print IndexData
            # 这里用StringIO读取内存中的CSV文件
            dataframe1=pd.read_csv(StringIO(IndexData))
            # print dataframe1
            # 此处必须重新copy 为新对象，否则dataframe1不变 VIP
            dataframe1=dataframe1.fillna(-1)
            # print dataframe1
            # print dataframe1 indexID,
            TotalLen=len(dataframe1)
            sqlvaluelist=[]

            sqlcommand = '''INSERT INTO IndexPriceDaily ( Symbol,TheDate,preClosePrice,openIndex,
                                highestIndex,lowestIndex,closeIndex,
                                 turnoverVol,turnoverValue,CHG,CHGPct)
                                  VALUES (%s,%s,%s,%s,
                                    %s,%s,%s,
                                  %s,%s,%s,%s)'''

            for iCount in range(TotalLen):

                Symbol=dataframe1.loc[iCount].indexID.split('.')[0].encode('utf8')
                preClosePrice=dataframe1.loc[iCount].preCloseIndex
                openIndex=dataframe1.loc[iCount].openIndex
                highestIndex=dataframe1.loc[iCount].highestIndex
                lowestIndex=dataframe1.loc[iCount].lowestIndex
                closeIndex=dataframe1.loc[iCount].closeIndex
                # VIP 必须要加int? 否则会报错ValueError: expected a simple type, a tuple or a list
                turnoverVol=int(dataframe1.loc[iCount].turnoverVol)
                # print turnoverVol
                turnoverValue=int(dataframe1.loc[iCount].turnoverValue)
                TheDate=dataframe1.loc[iCount].tradeDate

                CHG=dataframe1.loc[iCount].CHG
                CHGPct=dataframe1.loc[iCount].CHGPct


                # print "sqlcommand: " + sqlcommand

                # indexID+=1 str(indexID),
                sqlvalue=(Symbol,TheDate,preClosePrice,openIndex,highestIndex,lowestIndex,closeIndex,turnoverVol,turnoverValue,CHG,CHGPct)

                sqlvaluelist.append(sqlvalue)

                # print sqlvalue
                # print turnoverVol,turnoverValue
                # turnoverVol=1000000000

                # cursor.execute(sqlcommand) #,sqlvalue
                # cursor.execute(sqlcommand,(str(indexID), Symbol,TheDate,preClosePrice,openIndex,highestIndex,lowestIndex,closeIndex, turnoverVol, turnoverValue, CHG, CHGPct))
            # print sqlvaluelist
            # 批量执行插入
            # print TotalLen
            if TotalLen>0:
                cursor.executemany(sqlcommand,sqlvaluelist)
                conn.commit()
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