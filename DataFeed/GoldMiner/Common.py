# -*- coding: utf-8 -*-
"""
Created on 2016/1/27 16:01  

@author: A.Y

本模块目的：
"""

import gmsdk as gs
from gmsdk import md
from gmsdk import td
import  pandas as pd
from gmsdk import DailyBar
from gmsdk import StrategyBase
# import Database.General

from Util.Var import GMusername,GMpassword

#获取上交所SHSE、深交所SZSE所有可交易股票代码
# 上交所，市场代码 SHSE
# 深交所，市场代码 SZSE
# 中金所，市场代码 CFFEX
# 上期所，市场代码 SHFE
# 大商所，市场代码 DCE
# 郑商所，市场代码 CZCE
# 纽约商品交易所， 市场代码 CMX (GLN, SLN)
# 伦敦国际石油交易所， 市场代码 IPE (OIL, GAL)
# 纽约商业交易所， 市场代码 NYM (CON, HON)
# 芝加哥商品期货交易所，市场代码 CBT (SOC, SBC, SMC, CRC)
# 纽约期货交易所，市场代码 NYB (SGN)
# get_instruments('SHSE', 1, 1)
def FeedInstrumentsList(market='SHSE',sec_type=1):
    md.init(GMusername, GMpassword)
    instruments=md.get_instruments(market,sec_type,1)
    i=0
    SymbolList1=[]
    for instrument in instruments:
        SymbolList1.append((instrument.symbol,instrument.sec_name.decode('gbk')))
        #.encode('gb2312')#.decode('gb2312')
        i+=1
    print "Total:" + str(i)
    return SymbolList1


def SymbolAddedPrefix(symbol):
    # print "test"
    if symbol[0]=='6' or symbol[0]=='3' or symbol[0]=='2':
        return "SHSE." +symbol
    elif symbol[0]=='0':
        return "SZSE." +symbol
