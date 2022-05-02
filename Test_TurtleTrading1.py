#选自[21].	https://zhuanlan.zhihu.com/p/73832870
# 手把手教你】用Python量化海龟交易法则 - CuteHand的文章 - 知乎

import pandas as pd
import numpy as np
import talib as ta

from datetime import datetime,timedelta
import matplotlib.pyplot as plt
#对K线图和唐奇安通道进行可视化
from pyecharts import *

# %matplotlib inline #用于Jupyter

import tushare as ts
from pylab import mpl

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False



token='f20927201ecc20e3cea9279abacfbb1d39a9624820d9b2f94613f722'
pro=ts.pro_api(token)
index={'上证综指': '000001.SH',
        '深证成指': '399001.SZ',
        '沪深300': '000300.SH',
        '创业板指': '399006.SZ',
        '上证50': '000016.SH',
        '中证500': '000905.SH',
        '中小板指': '399005.SZ',
        '上证180': '000010.SH'}

#获取当前交易的股票代码和名称
def get_code():
    df = pro.stock_basic(exchange='', list_status='L')
    codes=df.ts_code.values
    names=df.name.values
    stock=dict(zip(names,codes))
    #合并指数和个股成一个字典
    stocks=dict(stock,**index)
    return stocks
#获取行情数据
def get_daily_data(stock,start,end):
    #如果代码在字典index里，则取的是指数数据
    code=get_code()[stock]
    if code in index.values():
        df=pro.index_daily(ts_code=code,start_date=start, end_date=end)
    #否则取的是个股数据
    else:
        df=pro.daily(ts_code=code, adj='qfq',start_date=start, end_date=end)
    #将交易日期设置为索引值
    df.index=pd.to_datetime(df.trade_date)
    df=df.sort_index()
    #计算收益率
    df['ret']=df.close/df.close.shift(1)-1
    return df

def my_strategy(data):
    x1=data.close>data.up
    x2=data.close.shift(1)<data.up.shift(1)
    x=x1&x2
    y1=data.close<data.down
    y2=data.close.shift(1)>data.down.shift(1)
    y=y1&y2
    data.loc[x,'signal']='buy'
    data.loc[y,'signal']='sell'
    buy_date=(data[data.signal=='buy'].index).strftime('%Y%m%d')
    sell_date=(data[data.signal=='sell'].index).strftime('%Y%m%d')
    buy_close=data[data.signal=='buy'].close.round(2).tolist()
    sell_close=data[data.signal=='sell'].close.round(2).tolist()
    return (buy_date,buy_close,sell_date,sell_close)

hs=get_daily_data('沪深300','20180101','')[['close','open','high','low','vol']]
#最近N1个交易日最高价
hs['up']=ta.MAX(hs.high,timeperiod=20).shift(1)
#最近N2个交易日最低价
hs['down']=ta.MIN(hs.low,timeperiod=10).shift(1)
#每日真实波动幅度
hs['ATR']=ta.ATR(hs.high,hs.low,hs.close,timeperiod=20)
hs.tail()


grid = Grid()
attr=[str(t) for t in hs.index.strftime('%Y%m%d')]
v1=np.array(hs.loc[:,['open','close','low','high']])
v2=np.array(hs.up)
v3=np.array(hs.down)
kline = Kline("沪深300唐奇安通道",title_text_size=15)
kline.add("K线图", attr, v1.round(1),is_datazoom_show=True,)
# 成交量
bar = Bar()
bar.add("成交量", attr, hs['vol'],tooltip_tragger="axis", is_legend_show=False,
        is_yaxis_show=False, yaxis_max=5*max(hs["vol"]))
line = Line()
line.add("上轨线", attr, v2.round(1),is_datazoom_show=True,
         is_smooth=True,is_symbol_show=False,line_width=1.5)
line.add("下轨线", attr, v3.round(1),is_datazoom_show=True,
         is_smooth=True,is_symbol_show=False,line_width=1.5)
#添加买卖信号
bd,bc,sd,sc=my_strategy(hs)
es = EffectScatter("buy")
es.add( "sell", sd, sc, )
es.add("buy", bd, bc,symbol="triangle",)
overlap = Overlap(width=2000, height=600)
overlap.add(kline)
overlap.add(line)
overlap.add(bar,yaxis_index=1, is_add_yaxis=True)
overlap.add(es)
grid.add(overlap, grid_right="10%")

