# -*- coding: utf-8 -*-
"""
Created on 2016/1/22 13:48  

@author: A.Y

本模块目的：获取股票数据
"""


import gmsdk as gs
from gmsdk import md
from gmsdk import td
import  pandas as pd
from gmsdk import DailyBar
from gmsdk import StrategyBase
import Database.General
from Common  import FeedInstrumentsList, SymbolAddedPrefix

from Util.Var import GMusername,GMpassword

# dailybar=gs.DailyBar()
# intrabar=gs.Bar()
# tick=gs.Tick()

# ret=md.init(GMusername, GMpassword)


# print FeedIndexConstituents()

# 从Goldminer获取所有的股票，返回如('SHSE.600000', u'\u6d66\u53d1\u94f6\u884c')
def FeedAllStockList():
    SymbolList1=[]
    SymbolList1=FeedInstrumentsList('SHSE',1)
    SymbolList2=[]
    SymbolList2=FeedInstrumentsList('SZSE',1)
    SymbolList=SymbolList1+SymbolList2
    print "共计" + str(len(SymbolList)) + "股票"
    return SymbolList




# FeedInstrumentsList('SHSE')
# print FeedAllFundList()

# FeedInstrumentsList('SZSE')
# FeedInstrumentsList('CFFEX')
# FeedInstrumentsList('SHFE')

# 求出当前tick值距昨日收盘价的涨跌幅
def GetTickVariation(Symbol):
    try:
        ticks=md.get_last_ticks(SymbolAddedPrefix(Symbol)) #,SZSE.000001
        # for tick in ticks:
            # print "Today Open:" + str(tick.open)
            # print "Today High:" + str(tick.high)
            # print "Today Low:" + str(tick.low)
            # print "Pre_Close:" + str(tick.pre_close)

        i=4
        # asksreverse=tick.asks[::-1]
        # for ask in asksreverse:
            # print "ask" + str(i) + ":" + str(ask)
            # print "ask" + str(i) + ":" + str("%.2f" % asksreverse[i][0]) + ";" + str("%.0f" % asksreverse[i][1])
            # i-=1
        i=0
        # for bid in tick.bids:
            # print "bid" + str(i) + ":" + str("%.2f" % tick.bids[i][0]) + ";" + str("%.0f" % tick.bids[i][1])
            # i+=1
        # print ticks[0].bids[0][0],ticks[0].pre_close
        variation=(ticks[0].bids[0][0]-ticks[0].pre_close)/ticks[0].pre_close
        # print "Variation" + str(".2f" % variation)
        # print variation
        # print "股价今日变动："+ str("%.2f" % (variation*100)) + str('%')
        return variation
    except Exception, e:
        print "error is:" + e.message
        # raise e
        return None
    # finally:


# v1=GetTickVariation('000001')
# print str("%.2f" % (v1*100))
        self.symbol = ''                         #股票代码
        # self.pub_date = ''                       #公告日期
        # self.eps = 0.0                           #每股收益
        # self.bvps = 0.0                          #每股净资产
        # self.cfps = 0.0                          #每股现金流
        # self.afps = 0.0                          #每股公积金
        # self.total_asset = 0.0                   #总资产
        # self.current_asset = 0.0                 #流动资产
        # self.fixed_asset = 0.0                   #固定资产
        # self.liability = 0.0                     #负债合计
        # self.current_liability = 0.0             #流动负债
        # self.longterm_liability = 0.0            #长期负债
        # self.equity = 0.0                        #所有者权益
        # self.income = 0.0                        #主营业务收入
        # self.operating_profit = 0.0              #主营业务利润
        # self.net_profit = 0.0                    #净利润

# 获取股票的财务数据
def FeedStockFinancialData(Symbol, date1,date2):
    md.init(GMusername, GMpassword)
    # fi=md.FinancialIndex()
    fi=md.get_financial_index(SymbolAddedPrefix(Symbol), date1, date2)
    return fi

# print FeedStockFinancialData('000001','1990-01-01','2016-01-27')

# symbollist=FeedAllStockList()
# for symbol in symbollist:
#     symbolname= symbol[0].split('.')[1]
#     print symbolname
#     fi=FeedStockFinancialData(symbolname,'1990-01-01  00:00:00','2016-01-27  00:00:00')
#     for f in fi:
#         print f.pub_date, f.eps, f.bvps,f.cfps,f.afps,f.total_asset

# #获取浦发银行(SHSE.600000)和平安银行(SZSE.000001)最新的市场指标
# get_last_market_index('SHSE.600000,SZSE.000001')
# #获取平安银行(SZSE.000001)最新10笔市场指标
# get_last_n_market_index('SHSE.000001', 10)
#         self.symbol = ''               #股票代码
#         self.pub_date = ''             #公告日期
#         self.pe_ratio = 0.0            #市盈率
#         self.pb_ratio = 0.0            #市净率
#         self.ps_ratio = 0.0            #市销率
#         self.market_value = 0.0        #市值
#         self.market_value_flow = 0.0   #流通市值
# 获取股票的市值数据
def FeedStockMarketData(Symbol,date1,date2):
    md.init(GMusername, GMpassword)
    # fi=md.FinancialIndex()
    fi=md.get_market_index(SymbolAddedPrefix(Symbol), date1, date2)
    return fi

# 获取最新的市场指标
def FeedRecentStockMarketData(Symbol):
    md.init(GMusername, GMpassword)
    fi=md.get_last_market_index(SymbolAddedPrefix(Symbol))
    return fi

# 获取最新的N笔市场指标
def FeedRecentStockMarketData(Symbol,N=5):
    md.init(GMusername, GMpassword)
    fi=md.get_last_n_market_index(SymbolAddedPrefix(Symbol),N)
    return fi


# 得到代码列表中当日实时涨幅最高的N个股
def GetTopNSymbol_HighestChange(topN=10):
    SymbolList=Database.General.GetStockSymbolList() # ['000001','00004','000005','000006','000008','000009','000010']#,
                 #'600000','600004','600005','600006','600008','600009'] #['000001','000006','600000','600004']#
    # Database.General.GetStockSymbolList() #
    # print SymbolList
    md.init(GMusername, GMpassword)
    SymbolChangeDict={}
    for symbol in SymbolList:
        print symbol
        v1=GetTickVariation(symbol)
        if v1<>None:
            SymbolChangeDict[symbol]=v1

    # print SymbolChangeDict
    SymbolChangeDict= sorted(SymbolChangeDict.iteritems(), key=lambda d:d[1], reverse = True)
    # print SymbolChangeDict
    i=0
    TopNSymbolList=[]
    for symbol in SymbolChangeDict:
        if i<topN:
            TopNSymbolList.append(symbol)
        i+=1
    return TopNSymbolList

# list1=GetTopNSymbol_HighestChange(3)
# print list1

# fi=FinancialIndex()
# fi=md.get_financial_index('SHSE.600000', '2013-01-01 00:00:00', '2015-12-31 00:00:00')
# print fi[0].total_asset

# print FeedIndexConstituents('000001')

