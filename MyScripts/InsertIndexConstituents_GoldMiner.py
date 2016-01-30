# -*- coding: utf-8 -*-
"""
Created on 2016/1/27 16:00  

@author: A.Y

本模块目的：
"""


import gmsdk as gs
from gmsdk import md
from gmsdk import td
from gmsdk import DailyBar
import  pandas as pd
import pymssql
from Database.General import GetMaxiumIndexID,GetIndexSymbolFullList,GetLatestDayofIndexPrice,ConnectDB
import time
import datetime
from GoldMiner.Index import FeedIndexConstituents, FeedAllIndexList
from StringIO import StringIO

start = time.time()

try:
    conn = ConnectDB()
    cursor=conn.cursor()
    indexID=int(GetMaxiumIndexID())+1
    # print indexID
    IndexSymbolList=FeedAllIndexList() #GetIndexSymbolFullList()

    # 以后更新时是否需要删除现有的所有记录？


    for Symbol in IndexSymbolList:
        IndexSymbol= Symbol[0]
        # print IndexSymbol
        iCount=0
        constituents=FeedIndexConstituents(IndexSymbol)

        sqlvaluelist=[]

        sqlcommand = '''INSERT INTO IndexConstituents (IndexSymbol, ConstituentSymbol,ConstituentWeight)
                              VALUES (%s,%s,%s)'''

        sqlvaluelist=[]

        for constituent in constituents:
            Symbol=IndexSymbol.split(".")[1]
            ConstituentSymbol=constituent[0].split(".")[1]
            # print ConstituentSymbol
            ConstituentWeight=constituent[1]
            # print ConstituentWeight

            sqlvalue=(Symbol,ConstituentSymbol,ConstituentWeight)
            # print sqlvalue
            sqlvaluelist.append(sqlvalue)
            # print sqlvaluelist
        print sqlvaluelist
        cursor.executemany(sqlcommand,sqlvaluelist)

    conn.commit()
except Exception,e:
    raise e
finally:
    cursor.close()
    conn.close()

end = time.time()
print "Use " + str(end-start) + " Seconds"