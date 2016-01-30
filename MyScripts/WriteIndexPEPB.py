# -*- coding: utf-8 -*-
"""
Created on 2016/1/27 20:35  

@author: A.Y

本模块目的：根据指数的成分计算每日的PE、PB值
"""

from Database.General import GetStockPEPB,ConnectDB,GetAllStockPEPBbyDay
from Database.General import GetIndexConstitutents, GetStockSymbolList,GetValidTradeDateList,GetStockPEPB,\
    GetLastestDayIndexValuation
from GoldMiner.Stock import FeedAllStockList
from GoldMiner.Index import FeedAllIndexList
import datetime, time

# 从2010年1月4日开始统计
def InsertIndexPEPB():

    start = time.time()

    # 这里如果取PE值，会出现负数，不知什么原因。暂取PE1值
    IndexList=[('SZSE.399812', u'\u4e0a\u8bc1\u7efc\u6307')]#FeedAllIndexList()#
    # print IndexList
    try:
        conn = ConnectDB()
        cursor=conn.cursor()

        for index in IndexList:
            indexsymbol=index[0].split(".")[1]

            #仅从2010年开始
            DateList=GetValidTradeDateList()
            # print DateList

            TotalWeight=0
            TotalPEValue=0
            TotalPBValue=0
            TotalPE=0
            TotalPB=0

            for thedate in DateList:
                StockList=GetIndexConstitutents(indexsymbol)
                # print StockList

                PEPBDic=GetAllStockPEPBbyDay(thedate)

                for Stock in StockList:
                    # print "Stock", Stock
                    StockSymbol=Stock[0]
                    Weight=Stock[1]
                    # print StockSymbol,Weight
                    #
                    # print StockSymbol,thedate

                    # 如果为B股则跳过，不进行统计
                    # print StockSymbol
                    if StockSymbol[0]<>'9':
                        PE_PB_Result=PEPBDic.get(StockSymbol,'')
                        if PE_PB_Result<>'':

                            PE=PE_PB_Result[0]
                            PB=PE_PB_Result[1]
                            # PE,PB=GetStockPEPB(StockSymbol,thedate)
                            # print "Dict", StockSymbol,thedate,PE,PB
                            # PE=PE_PB[0]
                            # PB=PE_PB[1]
                            if PE<>None and PB<>None:
                                TotalWeight=TotalWeight+(Weight/100)
                                TotalPEValue=TotalPEValue+PE*Weight/100
                                TotalPBValue=TotalPBValue+PB*Weight/100

                        # print TotalWeight,TotalPEValue,TotalPBValue


                            # print "TotalPEValue is:" + str(TotalPEValue)
                            # print "TotalPBValue is:" + str(TotalPBValue)
                            # print "TotalWeight is:" + str(TotalWeight)
                            # print "PE is:" + str(TotalPE)
                            # print "PB is:" + str(TotalPB)
                    else:
                        print "不统计B股指数"

                    # sqlvaluelist=[]
                if TotalWeight<>0:
                    TotalPE=TotalPEValue/TotalWeight
                    TotalPB=TotalPBValue/TotalWeight

                sqlcommand = '''INSERT INTO IndexValuationData (IndexSymbol,TheDate ,PE,PB)
                                              VALUES (%s,%s,%s,%s)'''

                sqlvalue=(indexsymbol,thedate,TotalPE,TotalPB)
                # print sqlcommand,sqlvalue
                # sqlvaluelist.append(sqlvalue)
                cursor.execute(sqlcommand,sqlvalue)
                conn.commit()
    except Exception,e:
            raise e

    finally:
        cursor.close()
        conn.close()

    end = time.time()
    print "Use " + str(end-start) + " Seconds"

# 从最近的日期开始统计
def UpdateIndexPEPB():

    start = time.time()

    # 这里如果取PE值，会出现负数，不知什么原因。暂取PE1值
    IndexList=[('SZSE.399812', u'\u4e0a\u8bc1\u7efc\u6307')]#FeedAllIndexList()#

    try:
        conn = ConnectDB()
        cursor=conn.cursor()

        for index in IndexList:
            indexsymbol=index[0].split(".")[1]

            #仅从2010年开始
            DateList=GetValidTradeDateList()
            LastestDay=GetLastestDayIndexValuation(indexsymbol)
            NewDateList=[]
            for DateValue in DateList:
                if DateValue>=LastestDay:
                    NewDateList.append(DateValue)
            print NewDateList

            TotalWeight=0
            TotalPEValue=0
            TotalPBValue=0
            TotalPE=0
            TotalPB=0

            for thedate in NewDateList:
                StockList=GetIndexConstitutents(indexsymbol)

                PEPBDic=GetAllStockPEPBbyDay(thedate)

                for Stock in StockList:
                    # print "Stock", Stock
                    StockSymbol=Stock[0]
                    Weight=Stock[1]
                    # print StockSymbol,Weight
                    #
                    # print StockSymbol,thedate

                    # 如果为B股则跳过，不进行统计
                    # print StockSymbol
                    if StockSymbol[0]<>'9':
                        PE_PB_Result=PEPBDic.get(StockSymbol,'')
                        if PE_PB_Result<>'':

                            PE=PE_PB_Result[0]
                            PB=PE_PB_Result[1]
                            # PE,PB=GetStockPEPB(StockSymbol,thedate)
                            # print "Dict", StockSymbol,thedate,PE,PB
                            # PE=PE_PB[0]
                            # PB=PE_PB[1]
                            if PE<>None and PB<>None:
                                TotalWeight=TotalWeight+(Weight/100)
                                TotalPEValue=TotalPEValue+PE*Weight/100
                                TotalPBValue=TotalPBValue+PB*Weight/100

                        # print TotalWeight,TotalPEValue,TotalPBValue


                            # print "TotalPEValue is:" + str(TotalPEValue)
                            # print "TotalPBValue is:" + str(TotalPBValue)
                            # print "TotalWeight is:" + str(TotalWeight)
                            # print "PE is:" + str(TotalPE)
                            # print "PB is:" + str(TotalPB)
                    else:
                        print "不统计B股指数"

                    # sqlvaluelist=[]
                if TotalWeight<>0:
                    TotalPE=TotalPEValue/TotalWeight
                    TotalPB=TotalPBValue/TotalWeight

                sqlcommand = '''INSERT INTO IndexValuationData (IndexSymbol,TheDate ,PE,PB)
                                              VALUES (%s,%s,%s,%s)'''

                sqlvalue=(indexsymbol,thedate,TotalPE,TotalPB)
                # print sqlcommand,sqlvalue
                # sqlvaluelist.append(sqlvalue)
                cursor.execute(sqlcommand,sqlvalue)
                conn.commit()
    except Exception,e:
            raise e

    finally:
        cursor.close()
        conn.close()

    end = time.time()
    print "Use " + str(end-start) + " Seconds"