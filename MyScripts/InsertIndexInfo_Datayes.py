# -*- coding: utf-8 -*-
"""
Created on 2016/1/18 14:38  

@author: A.Y

本模块目的：将指数信息导入数据库
"""

import csv
import chardet
import  pandas as pd
from Database.General import ConnectDB

#import Datayes.IndexInfo
import pymssql
import Database.mssql
from Datayes.IndexInfo import GetIndexInfo
import time
#
# def ipager(serial, pagesize):
#     """make serial page by page"""
#     buff = []
#     for row in serial:
#         buff.append(row)
#         if len(buff) >= pagesize:
#             send, buff, = buff, []
#             yield send
#     if len(buff):
#         yield buff

# indexlist=GetIndexInfo()

dataframe1=pd.read_csv('D:\MyDoc\Database\MyTradingSystem\Datayes\indexinfo.csv',encoding="gb2312")
dataframe1=dataframe1.fillna('NULL')
# print dataframe1
# print dataframe1.head(10)
# print len(dataframe1)
# print dataframe1.index
# print dataframe1.columns
# print dataframe1[[0,1,2]]
# print dataframe1['secID']
# print dataframe1.publishDate
# print dataframe1.loc[0]
# print dataframe1.iloc[[0,1]]
# print dataframe1.at[iCount,'secShortName']


# print len(dataframe1)
# for i in dataframe1:
#     series1= dataframe1.ix[[iCount]]
#     print series1
#     iCount+=1


# series1= dataframe1.ix[[0]]
#
# for column in series1.columns:
#     print series1[[column]]

# sqlcommand = "INSERT INTO IndexInfo VALUES ({}, {}, {}, {})"

start = time.time()


try:

    conn = ConnectDB()
    cursor=conn.cursor()

    iCount=0
    TotalLen=len(dataframe1)

    for iCount in range(TotalLen):
        # print dataframe1.loc[iCount]
        # sqlcommand="INSERT INTO IndexInfo (SecurityID,Symbol,ShortName"

        symbol=dataframe1.loc[iCount].secID.encode('utf8')
        symbol=symbol.split('.')[0]

        secShortName=dataframe1.loc[iCount].secShortName.encode('utf8')
        if dataframe1.loc[iCount].publishDate=="NULL":
            publishDate=''
        else:
            publishDate=dataframe1.loc[iCount].publishDate.encode('utf8')
        indexTypeCD=dataframe1.loc[iCount].indexTypeCD
        indexType=dataframe1.loc[iCount].indexType.encode('utf8')
        if dataframe1.loc[iCount].pubOrgCD=="NULL":
            pubOrgCD=-1
        else:
            pubOrgCD=dataframe1.loc[iCount].pubOrgCD
        porgFullName=dataframe1.loc[iCount].porgFullName.encode('utf8')
        if porgFullName=="NULL":
            porgFullName=''
        baseDate=dataframe1.loc[iCount].baseDate.encode('utf8')
        if baseDate=='NULL':
            baseDate=''
        basePoint=dataframe1.loc[iCount].basePoint
        if basePoint=='NULL':
            basePoint=999
        endDate=dataframe1.loc[iCount].endDate.encode('utf8')
        if endDate=="NULL":
            endDate=''
        # endDate='1992-1-1'
        # print endDate

        sqlcommand = '''
                    INSERT INTO IndexInfo (SecurityID,Symbol,ShortName,
                    publishDate,indexTypeCD,indexType,pubOrgCD,
                     porgFullName,baseDate,basePoint,endDate)
                      VALUES (%d,'%s','%s',
                        '%s',%d,'%s',%d,
                      '%s','%s',%d,'%s')
                    ''' % (iCount,symbol,secShortName,publishDate,indexTypeCD,indexType,pubOrgCD,porgFullName,baseDate,basePoint,endDate)
         # """ % (iCount,symbol,secShortName,publishDate,int(indexTypeCD),indexType,pubOrgCD,porgFullName,baseDate,int(basePoint))
        # sqlcommand = "INSERT INTO IndexInfo (SecurityID,Symbol,ShortName) VALUES ('1','000001','ssss')"
        # sqlcommand = """
        #             INSERT INTO IndexInfo (SecurityID,Symbol,ShortName,publishDate)
        #               VALUES (0,'%s','%s',Null)
        #             """ % (symbol,secShortName)
#,indexTypeCD,indexType,pubOrgCD,porgFullName,baseDate,basePoint,endDate
        # ?,'%s','%s',
        #             ?,%d,'%s',%d,
        #               '%s','%s',%d,%s
 # ?,?,?,?,
 #                      ?,?,?,?)

        # ,
        #              publishDate,indexTypeCD,indexType,pubOrgCD,
        #              porgFullName,baseDate,basePoint,endDate

        iCount+=1
        print str(iCount) + ":" + symbol
        # cursor.execute(sqlcommand,(1,'000001','fdfd','1995-01-1',2110,'ffdf',1,'fdfd','1900-1-1',100,'1900-1-1'))
        # print (iCount,symbol,secShortName,publishDate,indexTypeCD,indexType,pubOrgCD,porgFullName,baseDate,basePoint,endDate)
        # cursor.execute(sqlcommand,(iCount, symbol, secShortName, publishDate, int(indexTypeCD), indexType,int(pubOrgCD),porgFullName,baseDate,int(basePoint),'NULL'))

        # cursor.execute(sqlcommand,[(iCount,symbol,secShortName,publishDate,indexTypeCD,indexType,pubOrgCD,porgFullName,baseDate,basePoint,endDate)])
        cursor.execute(sqlcommand)
        conn.commit() #务必要加入commit这行 ,nan,nan,nan,nan,nan,nan,nan,nan

except Exception, e:
    print "error is:" + e.message
    raise e
finally:
    cursor.close()
    conn.close()

# 计算运算时间

end = time.time()
print end-start
# ms = Database.mssql.MSSQL(host="localhost",user="",pwd="",db="TradingSystem",charset='UTF-8')

# conn = pymssql.connect(host="localhost",user="",password="",database="TradingSystem",charset='UTF-8')


# cursor.execute("select * from Fundinfo where ShortName like '%中证500%'" )
# c2_list=cursor.fetchall()
# for row in c2_list:
#    print row[2]



# for i in items:
#     cursor.execute(sql.format(ID, shuju[0], xiangmu [i],shuju [i+2]))
#
# conn.commit()

# for row in indexlist:
#     print ', '.join(row)

# for rows in ipager(indexlist, 512):
#     #print chardet.detect(rows[0])
#     print rows[1].decode('utf-8').encode('gbk')
#     #print rows[0].decode("utf-8")
# #print indexlist

