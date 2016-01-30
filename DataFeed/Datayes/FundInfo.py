# -*- coding: utf-8 -*-
"""
Created on 2016/1/21 9:37  

@author: A.Y

本模块目的：
"""


from Datayes.dataapi import Client
import pandas as pd
from  StringIO import StringIO

from Util.Var import DatayesToken as token


# if __name__ == "__main__":
#     try:
#         client = Client()
#         client.init(token)
#         url1='/api/fund/getFund.csv?field=&secID=&ticker=&etfLof=&listStatusCd=L'  #secID,secShortName
#         code, result = client.getData(url1)
#         if code==200:
#             # print result.decode('gbk').encode('utf-8')
#             file_object = open('D:\MyDoc\Database\MyTradingSystem\Datayes\Fundinfo.csv', 'w')
#             file_object.write(result)
#             file_object.close( )
#         else:
#             print code
#             print result.decode('gbk').encode('utf-8')
#     except Exception, e:
#         #traceback.print_exc()
#         raise e
# dataframe1=pd.read_csv('D:\MyDoc\Database\MyTradingSystem\Datayes\Fundinfo.csv')
# print dataframe1

def GetFundInfo():
    try:
        client = Client()
        client.init(token)
        url1='/api/fund/getFund.csv?field=&secID=&ticker=&etfLof=&listStatusCd=L'
        code, result = client.getData(url1)
        if code==200:
            return result.decode('gbk').encode('utf-8')
        else:
            print code
            print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e

def GetFundList():
    try:
        client = Client()
        client.init(token)
        url1='/api/fund/getFund.csv?field=&secID=&ticker=&etfLof=&listStatusCd=L'

        code, result = client.getData(url1)
        # return result.decode('gbk').encode('utf-8')
        dataframe1=pd.read_csv(StringIO(result.decode('gbk').encode('utf-8')))
        totalLen=len(dataframe1)
        SymbolList=[]
        for iCount in range(totalLen):
            SymbolList.append(dataframe1.loc[iCount].secID.split('.')[0])
        return SymbolList

    except Exception, e:
        #traceback.print_exc()
        raise e
    # print FundInfo
#
# test=GetFundInfo()
# dataframe1=pd.read_csv(StringIO(GetFundInfo()))
# print dataframe1
