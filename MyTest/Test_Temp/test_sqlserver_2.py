# -*- coding: utf-8 -*-
"""
Created on 2016/1/18 10:34  

@author: A.Y

本模块目的：
"""
#,charset="UTF-8"
from os import getenv
import pymssql

print 'dbversion' + pymssql.get_dbversion()

#server = getenv("TradingSystem") #PYMSSQL_TEST_SERVER
#print server
#user = getenv("PYMSSQL_TEST_USERNAME")
#password = getenv("PYMSSQL_TEST_PASSWORD")

conn = pymssql.connect(host="localhost",user="", password="",database= "TradingSystem",charset="UTF-8",port = '1433')

cur= conn.cursor()

# cur.execute("select * from Fundinfo where ShortName like '%中证500%'" )

# row = cur.fetchone()
#
# while row:
#     #print("Symbol=%s, ShortName=%s" % (row[1], row[2]))
#     row = cur.fetchone()

# print cursor.fetchone()[0]
cur.execute("select * from Fundinfo where ShortName like '%中证500%'" )

c2_list=cur.fetchall()

#print(c2_list[1][2])

for row in c2_list:
   print row[2]#.decode('GB2312')

conn.close()