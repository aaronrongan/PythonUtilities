# -*- coding: utf-8 -*-
"""
Created on 2016/1/7 10:56  

@author: A.Y

本模块目的：
"""

# 'XSHG'
from Datayes.dataapi import Client
from Util.Var import DatayesToken as token

if __name__ == "__main__":
    try:
        client = Client()
        client.init(token)
        url1="/api/master/getTradeCal.json?field=&exchangeCD=XSHG&beginDate=&endDate="
        code, result = client.getData(url1)

        if code==200:
            print result.decode('gbk').encode('utf-8')

        else:
            print "error"
    except Exception, e:
        #traceback.print_exc()
        raise e