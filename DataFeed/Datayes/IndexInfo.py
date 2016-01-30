# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 21:57:43 2016

@author: MY2570P
"""

from Datayes.dataapi import Client
import pandas as pd

from Util.Var import DatayesToken as token
if __name__ == "__main__":
    try:
        client = Client()
        client.init(token)
        url1='/api/idx/getIdx.csv?field=&ticker=&secID='  #secID,secShortName
        code, result = client.getData(url1)
        if code==200:
            print result.decode('gbk').encode('utf-8')
            file_object = open('D:\MyDoc\Database\MyTradingSystem\Datayes\indexinfo.csv', 'w')
            file_object.write(result)
            file_object.close( )
        else:
            print code
            print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e

def GetIndexInfo():
    try:
        client = Client()
        client.init(token)
        url1='/api/idx/getIdx.csv?field=&ticker=&secID='
        code, result = client.getData(url1)
        if code==200:
            return result.decode('gbk').encode('utf-8')
        else:
            print code
            print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e

