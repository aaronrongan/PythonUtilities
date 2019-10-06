



import numpy as np
import pandas as pd
import talib as ta
# 这个是聚宽网(joinquant)的数据下载API，免费账户每天能下载100万条数据
from jqdatasdk import *
import matplotlib.pyplot as plt

# 登录验证

# auth("你的手机号", "你的密码")
auth("13651829783",'aaronjoinquant')

# %matplotlib inline

# 下载2015-2018年的沪深300指数，频率为每天，只要收盘价
# price = get_price("000300.XSHG", start_date="2010-01-01", end_date="2019-09-30", frequency="Xm", fields=['close'])['close']
price = get_price("000300.XSHG", start_date="2010-01-01", end_date="2019-09-30", frequency="1d", fields=['close'])['close']

# 用python自带的tseries库中的pct_change()函数计算日收益率
ret = price.pct_change()
# 画图
plt.figure(figsize=(18,8))
ax1 = plt.subplot(2,1,1)
ax1.plot(price)
ax2 = plt.subplot(2,1,2)
ax2.plot(ret)
plt.show()


# 用talib库中的相应函数计算MACD指标
dif, dea, hist = ta.MACD(price)
# 计算EMA12和EMA26
ema12 = ta.EMA(price, 12)
ema26 = ta.EMA(price, 26)


# sig1只考虑HIST指标，HIST转正时开仓买入，转负时清仓
sig1 = (hist>0)
# sig2同时考虑HIST指标和DEA指标，只有当HIST转正，且DEA在0以上时，才开仓买入，任何一个指标变负即清仓。
# 这是文献中建议的方法
sig2 = (hist>0) & (dea>0)
# sig3同时考虑HIST和EMA指标，只有当HIST为正，而且当前价格在慢线（26日指数加权平均价）上方时，才开仓买入，任何一个指标转负即清仓。
# 网上有人建议过这种方法（如果我没有理解错的话）
sig3 = (hist>0) & (price>ema26)

# sig2滞后一期、去除空值、转换成整数
sig2_lag = sig2.shift(1).fillna(0).astype(int)
# sig2_lag与股票日收益率相乘，即可得策略日收益率。python能自动对齐时间序列的日期。
sig2_ret = sig2_lag*ret
# 计算策略累计收益
cum_sig2_ret = (1+sig2_ret).cumprod()
# 把股票价格转换成从1开始，方便比较
price_norm = price/price[0]
# 开始作图
plt.figure(figsize=(18,8))
plt.plot(price_norm)
plt.plot(cum_sig2_ret)
plt.legend(["benchmark", "strategy cumulative return"], loc="upper left")
plt.show()