# -*- coding: utf-8 -*-
"""
Created on 2016/1/22 16:48  

@author: A.Y

本模块目的：仿照TradeStation、 同花顺中的用法，将如10内涨幅第一的列出
"""
import pymssql
import Database.General
import datetime
import time
from Database.General import GetStockShortNamebySymbol,ConnectDB


def GetStockVaration(symbol, ThisDate, Lastday):
    conn = ConnectDB()
    cur= conn.cursor()
    # VIP 如何调用存储过程的代码，很有用，注意要声明变量和Select ...as
    # cur.execute('''DECLARE @Change float
    #             EXEC PSD_GetNDaysChange_ClosePrice @Symbol=%s, @TheDate=%s, @NDays=%s, @Change=@Change output
    #             SELECT @Change as N'@Change'
    #             ''',
    #             (Symbol,ThisDate,NDays))

    cur.execute('''DECLARE @Change float
                EXEC PSD_GetNDaysChange_ClosePrice @Symbol=%s, @TheDate=%s, @LastDay=%s, @Change=@Change output
                SELECT @Change as N'@Change'
                ''',
                (symbol,ThisDate,Lastday))
    resList = cur.fetchone()
    cur.close()
    conn.close()
    return resList[0]

# result=GetStockVaration('000010','2016-01-21',5)
# print result[0]

# 前N日内涨幅最大的股票列表
def GetTopNHighestChange(topNumbers=10, NDays=5):
    conn = ConnectDB()
    cur= conn.cursor()
    # 应该用昨日的数据?或者最后一天的数据

    # Today=datetime.date.today()
    LatestValidDay=Database.General.GetLatestDayofAllStockPrice() #'2016-01-21' #
    print LatestValidDay
    LastDay=Database.General.GetLastNDay(LatestValidDay,NDays)
    SymbolList=Database.General.GetStockSymbolList()
    # print SymbolList
    ChangeDict={}
    for symbol in SymbolList:
        # GetStockVaration(symbol, Today,topN)
        # print symbol

        cur.execute('''DECLARE @Change float
                EXEC PSD_GetNDaysChange_ClosePrice @Symbol=%s, @TheDate=%s, @LastDay=%s, @Change=@Change output
                SELECT @Change as N'@Change'
                ''',
                (symbol,LatestValidDay,LastDay))
        result = cur.fetchone()
        # print result
        if result[0]<>None:
            ChangeDict.setdefault(symbol, result[0])

        # cur.execute("select max(TheDate) from StockPriceDaily where symbol=%s and ",(symbol))

        # resList = cur.fetchone()
        # print resList
        # return resList[0]
    cur.close()
    conn.close()
    ChangeDict= sorted(ChangeDict.iteritems(), key=lambda d:d[1], reverse = True)
    i=0
    TopNSymbolList=[]
    for symbol in ChangeDict:
        if i<topNumbers:
            TopNSymbolList.append(symbol)
        i+=1
    return TopNSymbolList


start = time.time()
# '求出5天涨幅前100位的列表
result1= GetTopNHighestChange(100,5)
i=1
for symbol in result1:
    print i, "-", symbol[0],"-",str(GetStockShortNamebySymbol(symbol[0])), "-", str("%.2f" % (symbol[1]*100)) +"%"
    i+=1

# '求出30天涨幅前100位的列表
result2= GetTopNHighestChange(100,30)
i=1
for symbol in result2:
    print i, "-", symbol[0],"-",str(GetStockShortNamebySymbol(symbol[0])), "-", str("%.2f" % (symbol[1]*100)) +"%"
    i+=1

# VIP
# 前2个列表的交集list(set(result1).intersection(set(result2)))
result=list(set(result1).intersection(set(result2)))

# 这是并集
# list(set(a).union(set(b)))
# 这是b中有而a中没有的
# print list(set(b).difference(set(a))) # b中有而a中没有的

print "30日与5日涨幅最大的交集为："
i=1
ThisDay=Database.General.GetLatestDayofAllStockPrice()
LastDay=Database.General.GetLastNDay(ThisDay,30)
print result[0][0], ThisDay, LastDay
for symbol in result:
    PriceChangePercent=GetStockVaration(symbol[0], ThisDay, LastDay)
    print i, "-", symbol[0],"-",str(GetStockShortNamebySymbol(symbol[0])),"30日涨幅:",str("%.2f" % (PriceChangePercent*100)) +"%"
    i+=1

end = time.time()
print "用时" + end-start + "秒"