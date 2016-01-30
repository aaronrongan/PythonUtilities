# -*- coding: utf-8 -*-
"""
Created on  2016/1/4  19:10 

@author: A.Y
"""

from Datayes.dataapi import Client
from Util.Var import DatayesToken as token


def GetStockData(symbol, beginDate,endDate):
    try:
        client = Client()
        client.init(token)

        fullbeginDate=beginDate.split('-')[0] +beginDate.split('-')[1]+beginDate.split('-')[2]
        fullendDate=endDate.split('-')[0] +endDate.split('-')[1]+endDate.split('-')[2]

        # print symbol,fullbeginDate,fullendDate
        url1="/api/market/getMktEqud.csv?field=&beginDate=%s&endDate=%s&secID=&ticker=%s&tradeDate=" % (fullbeginDate,fullendDate,symbol)
        # print url1
        code, result = client.getData(url1)
        if code==200:
            # print "Data OK"
            # print result.decode('gbk').encode('utf-8')
            return result.decode('gbk').encode('utf-8')
        else:
            # print "Data NOT OK"
            print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e

def GetStockFAFactor(symbol,beginDate,endDate):

    try:
        client = Client()
        client.init(token)

        fullbeginDate=beginDate.split('-')[0] +beginDate.split('-')[1]+beginDate.split('-')[2]
        fullendDate=endDate.split('-')[0] +endDate.split('-')[1]+endDate.split('-')[2]

        # print symbol,fullbeginDate,fullendDate
        url1="/api/market/getMktAdjf.json?field=&secID=&ticker=%s&exDivDate=&beginDate=&endDate=20151123" % (symbol, fullbeginDate,fullendDate,symbol)
        # print url1
        code, result = client.getData(url1)
        if code==200:
            # print "Data OK"
            # print result.decode('gbk').encode('utf-8')
            return result.decode('gbk').encode('utf-8')
        else:
            # print "Data NOT OK"
            print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e
# GetStockData('000001','2016-01-12','2016-01-19')