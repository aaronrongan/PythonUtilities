# -*- coding: utf-8 -*-
"""
Created on 2016/1/8 11:51  

@author: A.Y

本模块目的：测试各种数据库
SQLite太方便、太简洁了。。。
"""

import sqlite3

# conn = sqlite3.connect('test.db')
#
# cursor = conn.cursor()
#
# # ====================创建数据表、插入记录
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
#
# cursor.rowcount
#
# cursor.close()
#
# conn.commit()
#
# conn.close()

# ========================查询
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', '1')
values = cursor.fetchall()
print values
cursor.close()
conn.close()




