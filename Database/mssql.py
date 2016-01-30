# -*- coding: utf-8 -*-
"""
Created on 2016/1/18 12:34  

@author: A.Y

本模块目的：
"""

import pymssql
import chardet




class MSSQL:
    """
    对pymssql的简单封装
    pymssql库，该库到这里下载：http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
    使用该库时，需要在Sql Server Configuration Manager里面将TCP/IP协议开启

    用法：

    """

    def __init__(self,host,user,password,db,charset):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
        self.charset=charset

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset=self.charset)
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

    def BulkInsert(self, dbtablename, sql_str, values):
        # conn = pymssql.connect(host='192.168.2.20', user='root',passwd='123456')
        cursor = self.conn.cursor()
        self.conn.select_db(dbtablename)

        cursor.executemany(sql_str, values)
        self.conn.commit()

        cursor.close()
        self.conn.close()

def main():
## ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
## #返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
## ms.ExecNonQuery("insert into WeiBoUser values('2','3')")

    ms = MSSQL(host="localhost",user="",password="",db="TradingSystem",charset='UTF-8')

    resList = ms.ExecQuery("SELECT SecurityID, Symbol,ShortName FROM FundInfo ") #Where Symbol='159903'

    for (SecurityID, Symbol,ShortName) in resList:
        print ShortName#.encode("gb2312")#.decode('utf-8').encode('gb18030') #decode("utf8").encode('gbk')
        #print chardet.detect(str(Symbol))
    #
    #     #print str(ShortName).decode('ascii')#.decode('GB2312')

    # print reslist[0]

    # row = cursor.fetchone()
    # while row:
    #     print("ID=%d, Name=%s" % (row[0], row[1]))
    #     row = cursor.fetchone()

if __name__ == '__main__':
    main()