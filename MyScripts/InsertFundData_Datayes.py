# -*- coding: utf-8 -*-
"""
Created on 2016/1/21 11:45  

@author: A.Y

本模块目的：用Datayes的基金价格数据填充SQL 数据库
"""

import  pandas as pd
import csv
import chardet
import Database.General

import Datayes.FundDaily, Datayes.FundInfo
import pymssql
import Database.mssql,Database.General
from Database.General import ConnectDB
from Database.General import GetLatestDayofFundPrice,GetMaxiumFundID,GetFundSymbolFullList
import time
import datetime
from StringIO import StringIO

def InsertFundData_Datayes():
    start = time.time()

    try:
        conn = ConnectDB()
        cursor=conn.cursor()

        # print indexID
        SymbolList=Datayes.FundInfo.GetFundList() #['000023'] ['512210'] #
        # print SymbolList
        for Symbol in SymbolList:
            print Symbol
            iCount=0
            MaxID=GetMaxiumFundID()
            # print MaxID
            if MaxID<>None:
                FundID=int(MaxID)+1
            else:
                FundID=1

            LastWorkingDay=GetLatestDayofFundPrice(Symbol)
            # print LastWorkingDay
            if LastWorkingDay<>None:
                year= int(LastWorkingDay.split('-')[0])
                month= int(LastWorkingDay.split('-')[1])
                day=int(LastWorkingDay.split('-')[2])
                LastWorkingDay= datetime.date(year, month, day)#time.strptime(GetLatestDayofIndexPrice(Symbol), "%Y-%m-%d")
            else:
                LastWorkingDay=datetime.date(2000, 1, 1)

            Today=datetime.date.today()
            FundData=Datayes.FundDaily.GetFundData(Symbol,str(LastWorkingDay + datetime.timedelta(1)),str(Today))
            # print FundData
            # 这里用StringIO读取内存中的CSV文件
            dataframe1=pd.read_csv(StringIO(FundData))
            # print dataframe1
            # 此处必须重新copy 为新对象，否则dataframe1不变 VIP
            dataframe1=dataframe1.fillna(-1)
            # print dataframe1
            # print dataframe1
            TotalLen=len(dataframe1)
            sqlvaluelist=[]

            for iCount in range(TotalLen):

                Symbol=dataframe1.loc[iCount].secID.split('.')[0].encode('utf8')
                TheDate=dataframe1.loc[iCount].tradeDate
                preClosePrice=float(dataframe1.loc[iCount].preClosePrice)
                openPrice=float(dataframe1.loc[iCount].openPrice)
                highestPrice=float(dataframe1.loc[iCount].highestPrice)
                lowestPrice=float(dataframe1.loc[iCount].lowestPrice)
                closePrice=float(dataframe1.loc[iCount].closePrice)
                CHG=float(dataframe1.loc[iCount].CHG)
                CHGPct=float(dataframe1.loc[iCount].CHGPct)
                # VIP 必须要加int? 否则会报错ValueError: expected a simple type, a tuple or a list
                turnoverVol=int(dataframe1.loc[iCount].turnoverVol)
                turnoverValue=int(dataframe1.loc[iCount].turnoverValue)

                discount=float(dataframe1.loc[iCount].discount)
                discountRatio=float(dataframe1.loc[iCount].discountRatio)
                circulationShares=float(dataframe1.loc[iCount].circulationShares)
                accumAdjFactor=float(dataframe1.loc[iCount].accumAdjFactor)

                sqlcommand = '''INSERT INTO FundPriceDaily (Symbol,TheDate,preClosePrice,
                                OpenPrice,HighPrice,LowPrice,ClosePrice,
                                 TurnoverVolume,TurnoverValue,CHG,CHGPct,
                                 discount,discountRatio,circulationShares,accumAdjFactor)
                                  VALUES (%s,%s,%s,
                                    %s,%s,%s,%s,
                                    %s,%s,%s,%s,
                                  %s,%s,%s,%s)'''
                # print "sqlcommand: " + sqlcommand
                # fundID,  %s,str(FundID),
                sqlvalue=(Symbol,TheDate,preClosePrice,
                          openPrice,highestPrice,lowestPrice,closePrice,
                          turnoverVol,turnoverValue,CHG,CHGPct,
                          discount,discountRatio,circulationShares,accumAdjFactor)

                sqlvaluelist.append(sqlvalue)

                FundID+=1
                # print sqlcommand,sqlvalue
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
                print
                # print "No records added"


    except Exception,e:
        raise e
    finally:
        cursor.close()
        conn.close()

    end = time.time()
    print "Use " + str(end-start) + " Seconds"