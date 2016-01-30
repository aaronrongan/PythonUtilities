# -*- coding: utf-8 -*-
"""
Created on 2016/1/18 10:09  

@author: A.Y

本模块目的：测试SQL Server，使用pyodbc和pymssql
"""

# import pyodbc
#
# # cnxn = pyodbc.connect('Integrated Security=True;Data Source=LocalHost;Initial Catalog=TradingSystem;') #UID=sa;PWD=myPassword'
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=LocalHost;DATABASE=TradingSystem;')
# cursor = cnxn.cursor()
#
# cursor.execute("select * from FundInfo")
#
# cnxn.close()

import pymssql

#数据库连接

# conn = pymssql.connect(host =".",database ="master",user="sa",password="1")

# conn = pymssql.connect('Integrated Security=True;Data Source=LocalHost;Initial Catalog=TradingSystem;')
# host = '127.0.0.1',port = '49155',user = 'sa',password = '123456',database = 'Test',charset = 'utf8'

conn = pymssql.connect(host = '127.0.0.1',database = 'TradingSystem',charset = 'utf8')
#定义游标

cur = conn.cursor()

#执行指定的sql

cur.execute("select * from FundInfo")

#游标读取第一行

row = cur.fetchone()

for i in range(2):

   if i ==2:

       print row[0]," ".ljust(10-len(row[0])," "),row[1]," ".ljust(20-len(row[1])," "),row[2]

   row = cur.fetchone()
#关闭数据库连接

conn.close()


