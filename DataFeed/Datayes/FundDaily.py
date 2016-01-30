# -*- coding: utf-8 -*-
"""
Created on 2016/1/21 8:58  

@author: A.Y

本模块目的：获取基金数据
"""


from Datayes.dataapi import Client
from Util.Var import DatayesToken as token


def GetFundData(symbol, beginDate,endDate):
    try:
        client = Client()
        client.init(token)

        fullbeginDate=beginDate.split('-')[0] +beginDate.split('-')[1]+beginDate.split('-')[2]
        fullendDate=endDate.split('-')[0] +endDate.split('-')[1]+endDate.split('-')[2]
        # url1="/api/market/getMktFundd.csv?field=&beginDate=20150101&endDate=&secID=512210.XSHG&ticker=&tradeDate="
        url1="/api/market/getMktFundd.csv?field=&beginDate=%s&endDate=%s&secID=&ticker=%s&tradeDate=" % (fullbeginDate,fullendDate,symbol)
        # print url1
        code, result = client.getData(url1)
        if code==200:
            # print "Data OK"
            # print result.decode('gbk').encode('utf-8')
            return result.decode('gbk').encode('utf-8')
        else:
            print "Data NOT OK"
            # print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e

# GetFundData('000001','2015-12-11','2016-01-18')
