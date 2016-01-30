# -*- coding: utf-8 -*-
"""
Created on 2016/1/18 13:41  

@author: A.Y

本模块目的：获取基金信息
"""


import gmsdk as gs
from gmsdk import md
from Util.Var import GMusername,GMpassword
from Common import FeedInstrumentsList

# dailybar=gs.DailyBar()
# intrabar=gs.Bar()
# tick=gs.Tick()
#
# ret=md.init(GMusername, GMpassword)
# print ret

# 从Goldminer获取所有的股票，返回如('SHSE.600000', u'\u6d66\u53d1\u94f6\u884c')
def FeedAllFundList():
    SymbolList1=[]
    SymbolList1=FeedInstrumentsList('SHSE',2)
    SymbolList2=[]
    SymbolList2=FeedInstrumentsList('SZSE',2)
    SymbolList=SymbolList1+SymbolList2
    print "共计" + str(len(SymbolList)) + "指数"
    return SymbolList
