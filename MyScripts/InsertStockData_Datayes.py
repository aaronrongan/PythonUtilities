# -*- coding: utf-8 -*-
"""
Created on 2016/1/20 17:23  

@author: A.Y

本模块目的：
"""

import  pandas as pd
import csv
import chardet
import Database.General

import Datayes.StockDaily
import pymssql
import Database.mssql
from Database.General import GetStockSymbolFullList,GetStockSymbolList,GetLatestDayofStockPrice,ConnectDB
import time
import datetime
from StringIO import StringIO

def InsertStockData_Datayes():
    start = time.time()

    try:
        conn = ConnectDB()
        cursor=conn.cursor()

        # print indexID
        SymbolList= GetStockSymbolFullList() #['601766'] #

        for Symbol in SymbolList:
            print Symbol
            iCount=0
            LastWorkingDay=GetLatestDayofStockPrice(Symbol)
            # print LastWorkingDay
            if LastWorkingDay<>None:
                year= int(LastWorkingDay.split('-')[0])
                month= int(LastWorkingDay.split('-')[1])
                day=int(LastWorkingDay.split('-')[2])
                LastWorkingDay= datetime.date(year, month, day)#time.strptime(GetLatestDayofIndexPrice(Symbol), "%Y-%m-%d")
            else:
                LastWorkingDay=datetime.date(1991, 1, 1)

            Today=datetime.date.today()
            StockData=Datayes.StockDaily.GetStockData(Symbol,str(LastWorkingDay + datetime.timedelta(1)),str(Today))
            # print IndexData
            # 这里用StringIO读取内存中的CSV文件
            dataframe1=pd.read_csv(StringIO(StockData))
            # print dataframe1
            # 此处必须重新copy 为新对象，否则dataframe1不变 VIP
            dataframe1=dataframe1.fillna(-1)
            # print dataframe1
            TotalLen=len(dataframe1)
            sqlvaluelist=[]

            sqlcommand = '''INSERT INTO StockPriceDaily
                            (SecurityID, Symbol,TheDate,PreClosePrice,ActPreClosePrice,
                              OpenPrice,HighPrice,LowPrice,ClosePrice,
                              TurnoverVolume,TurnoverValue,DealAmount,TurnoverRate,
                              AccumAdjFactor,NegMarketValue,MarketValue,
                              PE,PE1,PB,
                              OpenPrice_FA,HighPrice_FA,LowPrice_FA,ClosePrice_FA)
                                  VALUES
                                  (%s,%s,%s,%s,%s,
                                    %s,%s,%s,%s,
                                    %s,%s,%s,%s,
                                    %s,%s,%s,
                                    %s,%s,%s,
                                  %s,%s,%s,%s)'''

            for iCount in range(TotalLen):
                SecurityID=str(dataframe1.loc[iCount].secID)
                Symbol=str(dataframe1.loc[iCount].secID.split('.')[0])
                # Symbol=dataframe1.loc[iCount]..split('.')[0].encode('utf8')
                TheDate=str(dataframe1.loc[iCount].tradeDate)
                preClosePrice=float(dataframe1.loc[iCount].preClosePrice)
                actPreClosePrice=float(dataframe1.loc[iCount].actPreClosePrice)
                openPrice=float(dataframe1.loc[iCount].openPrice)
                highestPrice=float(dataframe1.loc[iCount].highestPrice)
                lowestPrice=float(dataframe1.loc[iCount].lowestPrice)
                closePrice=float(dataframe1.loc[iCount].closePrice)
                # VIP 必须要加int? 否则会报错ValueError: expected a simple type, a tuple or a list
                turnoverVol=int(dataframe1.loc[iCount].turnoverVol)
                turnoverValue=int(dataframe1.loc[iCount].turnoverValue)
                dealAmount=float(dataframe1.loc[iCount].dealAmount)
                turnoverRate=float(dataframe1.loc[iCount].turnoverRate)
                accumAdjFactor=float(dataframe1.loc[iCount].accumAdjFactor)
                negMarketValue=float(dataframe1.loc[iCount].negMarketValue)
                marketValue=float(dataframe1.loc[iCount].marketValue)
                PE=float(dataframe1.loc[iCount].PE)
                PE1=float(dataframe1.loc[iCount].PE1)
                PB=float(dataframe1.loc[iCount].PB)
                OpenPrice_FA=float(dataframe1.loc[iCount].openPrice)
                HighPrice_FA=float(dataframe1.loc[iCount].highestPrice)
                LowPrice_FA=float(dataframe1.loc[iCount].lowestPrice)
                ClosePrice_FA=float(dataframe1.loc[iCount].closePrice)


                # print "sqlcommand: " + sqlcommand

                sqlvalue=(SecurityID,Symbol,TheDate,preClosePrice,actPreClosePrice,
                          openPrice,highestPrice,lowestPrice,closePrice,
                          turnoverVol,turnoverValue,dealAmount,turnoverRate,
                          accumAdjFactor,negMarketValue,marketValue,
                          PE,PE1,PB,
                          OpenPrice_FA,HighPrice_FA,LowPrice_FA,ClosePrice_FA)
                # print sqlvalue
                sqlvaluelist.append(sqlvalue)

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
                print "" #"No records added"


    except Exception,e:
        raise e
    finally:
        cursor.close()
        conn.close()

    end = time.time()
    print "Use " + str(end-start) + " Seconds"