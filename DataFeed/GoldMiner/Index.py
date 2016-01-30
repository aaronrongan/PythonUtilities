# -*- coding: utf-8 -*-
"""
Created on 2016/1/18 13:41  

@author: A.Y

本模块目的：获取指数信息
"""

import gmsdk as gs
from gmsdk import md
from gmsdk import td
import  pandas as pd
from gmsdk import DailyBar
from gmsdk import StrategyBase
import Common

from Util.Var import GMusername,GMpassword

# dailybar=gs.DailyBar()
# intrabar=gs.Bar()
# tick=gs.Tick()

# print md.get_share_index('SHSE.600000', '2015-8-14 00:00:00', '2015-8-15 00:00:00')
# print md.get_constituents('SHSE.000001')[0]
# print md.get_instruments("SHSE", 1, 1)
# instruments=md.get_instruments("SHSE", 1, 1)
#
# for value in instruments:
#     print value

# 必须写成01-01，而不是1-1。。。
# dataframe1=md.get_dailybars('SHSE.000001','2016-01-01 00:00:00','2016-01-18 00:00:00')
# dailybar=DailyBar()
# dailybar=dataframe1[1]
# print dailybar.open
# print dailybar.close
# print dailybar.volume
# print dailybar.position
# print dailybar.amount
# print dailybar.bar_type
# print dailybar.flag
# print dailybar.position
# print dailybar.settle_price
# print dailybar.strtime
# print dailybar.upper_limit
# print dailybar.utc_time
# print dailybar.
# print dailybar.
# print dailybar.


def IndexSymbolAddedPrefix(symbol):
    # print "test"
    if symbol[0]=='6' or symbol[0]=='3' or symbol[0]=='2':
        return "SHSE." +symbol
    elif symbol[0]=='0':
        return "SHSE." +symbol

        # self.symbol = ''                ## 交易代码
        # self.sec_type = 0               ## 代码类型 VIP !!!1为股票，2为基金，3为指数,4 为CFFEX(中金?)
        # self.sec_name = ''              ## 代码名称
        # self.multiplier = 0.0           ## 合约乘数
        # self.margin_ratio = 0.0         ## 保证金比率
        # self.price_tick = 0.0           ## 价格最小变动单位
        # self.upper_limit = 0.0          ## 当天涨停板
        # self.lower_limit = 0.0          ## 当天跌停板
        # self.is_active = 0              ## 当天是否交易



def GetIndexData(symbol, beginDate,endDate):
    fullsymbol='SHSE.' + symbol
    fullbeginDate=beginDate + ' 00:00:00'
    fullendDate=endDate + ' 00:00:00'
    ret=md.init(GMusername, GMpassword)
    IndexDataList=md.get_dailybars(fullsymbol,fullbeginDate,fullendDate)
    md.close()
    return IndexDataList


# # 获取指数成分股，字段：Symbol+比重
# def FeedIndexConstituents(IndexSymbol):
#     md.init(GMusername, GMpassword)
#     # print IndexSymbolAddedPrefix(IndexSymbol)
#     stocks =md.get_constituents(IndexSymbolAddedPrefix(IndexSymbol))
#     # print stocks
#     Constituents=[]
#     for stock in stocks:
#         Consituent=(stock.symbol,stock.weight)
#         Constituents.append(Consituent)
#         # print stock.symbol,Database.General.GetStockShortNamebySymbol(stock.symbol.split('.')[1]) ,stock.weight*100
#     return Constituents

# 获取指数成分股
def FeedIndexConstituents(symbol='SHSE.000001'):
    md.init(GMusername, GMpassword)
    constituents=md.get_constituents(symbol)
    symbollist=[]
    for constituent in constituents:
        symbollist.append((constituent.symbol,constituent.weight))
    return symbollist

# print FeedAllFundList()，如('SHSE.000001', u'\u4e0a\u8bc1\u7efc\u6307')
def FeedAllIndexList():
    SymbolList1=[]
    SymbolList1=Common.FeedInstrumentsList('SHSE',3)
    SymbolList2=[]
    SymbolList2=Common.FeedInstrumentsList('SZSE',3)
    SymbolList=SymbolList1+SymbolList2
    print "共计" + str(len(SymbolList)) + "指数"
    return SymbolList


#
# dailybars=GetIndexData('000001','2016-01-01','2016-01-18')
#
# dailybar=DailyBar()
# for db in dailybars:
    # print db.close