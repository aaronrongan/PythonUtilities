# -*- coding: utf-8 -*-
"""
Created on 2016/1/19 20:34  

@author: A.Y

本模块目的：
"""
import pymssql
import mssql, time, timeit
import datetime
from GoldMiner.Common import SymbolAddedPrefix

def ConnectDB():
    conn=pymssql.connect(host="localhost",user="", password="",database= "TradingSystem",charset="utf8",port = '1433')
    return conn

def GetLatestDayofIndexPrice(symbol):

    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(TheDate) from IndexPriceDaily where symbol=%s",(symbol))
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

def GetMaxiumIndexID():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(indexID) from IndexPriceDaily")
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

def GetIndexSymbolList():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select distinct Symbol from IndexPriceDaily")
    resList = cur.fetchall()
    SymbolList=[]
    for symbol in resList:
        SymbolList.append(symbol[0].rstrip())
    return SymbolList
    cur.close()
    conn.close()

def GetIndexSymbolFullList():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select distinct Symbol from [IndexInfo]")
    resList = cur.fetchall()
    SymbolList=[]
    for symbol in resList:
        SymbolList.append(symbol[0].rstrip())
    return SymbolList
    cur.close()
    conn.close()

def GetStockSymbolList():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select distinct Symbol from StockPriceDaily order by Symbol")
    resList = cur.fetchall()
    SymbolList=[]
    for symbol in resList:
        SymbolList.append(symbol[0].rstrip())
    return SymbolList
    cur.close()
    conn.close()

def GetStockSymbolFullList():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select distinct Symbol from [StockInfo]")
    resList = cur.fetchall()
    SymbolList=[]
    for symbol in resList:
        SymbolList.append(symbol[0].rstrip())
    return SymbolList
    cur.close()
    conn.close()


def GetLatestDayofStockPrice(symbol):

    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(TheDate) from StockPriceDaily where symbol=%s",(symbol))
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

# 得出库中最大的日期
def GetLatestDayofAllStockPrice():

    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(TheDate) from StockPriceDaily")
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

def GetFundSymbolFullList():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select distinct Symbol from [FundInfo]")
    resList = cur.fetchall()
    SymbolList=[]
    for symbol in resList:
        SymbolList.append(symbol[0].rstrip())
    return SymbolList
    cur.close()
    conn.close()


def GetMaxiumFundID():
    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(fundID) from FundPriceDaily")
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()


def GetLatestDayofFundPrice(symbol):

    conn = ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(TheDate) from FundPriceDaily where symbol=%s",(symbol))
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

# 临时方法：得到错误的最大日期，纠正成交量和成交金额弄反的问题
def GetLatestDayofFundPrice_Correction(symbol):

    conn =ConnectDB()
    cur= conn.cursor()
    cur.execute("select max(TheDate) from IndexPriceDaily where preClosePrice is NULL and Symbol=%s", (symbol))
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

# 得到距离当前日期N天的日期，从TradeCalendar表取数。这里的SQL 用到了row_number函数。目的是为了不取到非交易日

def GetLastNDay(ThisDate, Ndays):

    conn = ConnectDB()
    cur= conn.cursor()
    sqlcommand='''
                select tmp.calendarDate from (select ROW_NUMBER() OVER (ORDER BY calendarDate) as rownumber, calendarDate from TradeCalendar where isOpen=1) as tmp
                where tmp.rownumber=(select tmp.rownumber from
                (select ROW_NUMBER() OVER (ORDER BY calendarDate) as rownumber, calendarDate from TradeCalendar where isOpen='1') as tmp
                where  calendarDate=%s)-%s
                '''
    cur.execute(sqlcommand, (ThisDate,Ndays))
    resList = cur.fetchone()
    # print resList
    return resList[0]
    cur.close()
    conn.close()

def GetStockShortNamebySymbol(symbol):
    conn = ConnectDB()
    cur= conn.cursor()
    # 这里无法解决使用存储过程输出乱码的问题，Æ½°²ÒøÐÐ  。暂时仍用select语句
    # cur.execute(u'''DECLARE @ShortName varchar(20)
    #             EXEC ISI_GetStockShortNamebySymbol @Symbol=%s, @ShortName=@ShortName output
    #             SELECT @ShortName as '@ShortName'
    #             ''',
    #             (symbol))
    cur.execute("select ShortName from StockInfo where Symbol=%s",symbol)
    resList = cur.fetchone()
    # print resList
    return resList[0].encode('utf8')#.encode("utf8")#.encode('gb2312')#.encode("utf-8")
    cur.close()
    conn.close()

def GetStockPEPB(symbol, date):
    try:
        conn = ConnectDB()
        cur= conn.cursor()
        if date=='':
            date=datetime.date.today()
        # PE为滚动市盈率，这里取PE1 市盈率
        cur.execute("select PE1,PB from StockPriceDaily where Symbol=%s and TheDate=%s ",(symbol, date))
        resList = cur.fetchone()
        # print resList
        if resList==None:
            return (None,None)
        else:
            return resList
    except Exception,e:
        raise e
        return (None,None)
    finally:
        cur.close()
        conn.close()

# 得到某日所有股票的PE/PB，存成字典，stock:(PE1,PB)
def GetAllStockPEPBbyDay(date):
    try:
        conn = ConnectDB()
        cur= conn.cursor()
        if date=='':
            date=datetime.date.today()
        # PE为滚动市盈率，这里取PE1 市盈率
        cur.execute("select Symbol, PE1,PB from StockPriceDaily where TheDate=%s order by Symbol",date)
        resList = cur.fetchall()
        # print resList
        PEPBDic={}
        for result in resList:
            PEPBDic.setdefault(result[0],(result[1],result[2]))
            print result[0],(result[1],result[2])
        return PEPBDic

        # if resList==None:
        #     return (None,None)
        # else:
        #     return resList
    except Exception,e:
        raise e
        return (None,None)
    finally:
        cur.close()
        conn.close()

# print GetStockPEPB('2016-01-27')
# PE,PB=GetStockPEPB('601777', '')
# if PE==None:
#     print "ok"

# 得到某个指数的成分股和权重
def GetIndexConstitutents(IndexSymbol):

    conn = ConnectDB()
    cur= conn.cursor()
    # IndexSymbol=SymbolAddedPrefix(IndexSymbol)
    # print IndexSymbol
    cur.execute("select ConstituentSymbol,ConstituentWeight  from IndexConstituents where IndexSymbol=%s order by ConstituentSymbol",IndexSymbol)

    resList = cur.fetchall()
    SymbolList=[]

    for symbol in resList:
        SymbolList.append((symbol[0].rstrip(),symbol[1]))
    return SymbolList

    cur.close()
    conn.close()

# 得到某个指数PEPB库的最新在库日期
def GetLastestDayIndexValuation(IndexSymbol):

    conn = ConnectDB()
    cur= conn.cursor()
    # IndexSymbol=SymbolAddedPrefix(IndexSymbol)
    # print IndexSymbol
    cur.execute("select max(TheDate) from IndexValuationData where IndexSymbol=%s",IndexSymbol)

    resList = cur.fetchone()
    # print resList
    if resList==None:
        return None
    else:
        return resList[0]

    cur.close()
    conn.close()

# # 得到某个指数PEPB库的最新待补充库日期
# def GetLastestDayListIndexValuation(IndexSymbol):
#


# print GetLastestDayIndexValuation('000002')
# 从TradeCalendar中得到有效交易日期
def GetValidTradeDateList():
    conn = ConnectDB()
    cur= conn.cursor()
    # IndexSymbol=SymbolAddedPrefix(IndexSymbol)
    # print IndexSymbol

    # 'cur.execute("select calendarDate from TradeCalendar where isOpen=1 and calendarDate<=getdate()")
    # 因为1990年时的股票太少，这里为了统计指数的市盈率，就从2010年开始
    cur.execute("select calendarDate from TradeCalendar where isOpen=1 and calendarDate>='2010-01-01' and calendarDate<=getdate()")

    resList = cur.fetchall()
    ValidTradeDateList=[]

    for ValidTradeDate in resList:
        ValidTradeDateList.append(ValidTradeDate[0])
    return ValidTradeDateList

    cur.close()
    conn.close()

# print GetValidTradeDateList()
# print GetIndexConstitutents('000001')
# def GetStockPB(symbol, date):
# start = time.time()
# print GetStockShortNamebySymbol('000001') #.encode('gb2312') .encode('utf8')
# end = time.time()
# print end-start
# print GetLastNDay('2016-01-21',13) .
# print GetLatestDayofFundPrice_Correction('000001')