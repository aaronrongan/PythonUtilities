
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 21:26:47 2016

@author: MY2570P
"""
from Datayes.dataapi import Client
from Util.Var import DatayesToken as token

# if __name__ == "__main__":
#     try:
#         client = Client()
#         client.init(token)
#         url1='/api/market/getMktIdxd.csv?field=&beginDate=20151230&endDate=20151230&indexID=000001&ticker=&tradeDate=20151230'
#         code, result = client.getData(url1)
#         if code==200:
#             print result.decode('gbk').encode('utf-8')
#         else:
#             print code
#             print result.decode('gbk').encode('utf-8')
#     except Exception, e:
#         #traceback.print_exc()
#         raise e


def GetIndexData(symbol, beginDate,endDate):
    try:
        client = Client()
        client.init(token)

        fullbeginDate=beginDate.split('-')[0] +beginDate.split('-')[1]+beginDate.split('-')[2]
        fullendDate=endDate.split('-')[0] +endDate.split('-')[1]+endDate.split('-')[2]

        # print symbol,fullbeginDate,fullendDate
        url1="/api/market/getMktIdxd.csv?field=&beginDate=%s&endDate=%s&indexID=&ticker=%s&tradeDate=" % (fullbeginDate,fullendDate,symbol)
        # print url1
        code, result = client.getData(url1)
        if code==200:
            print "Data OK"
            # print result.decode('gbk').encode('utf-8')
            return result.decode('gbk').encode('utf-8')
        else:
            print "Data NOT OK"
            # print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e

# GetIndexData('000022','2015-12-11','2016-01-19')

