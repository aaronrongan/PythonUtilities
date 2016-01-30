# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 22:07  

@author: A.Y

本模块目的：
"""
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

df = ts.get_tick_data('000001',date='2016-01-06')
print df['time'].sort_index(ascending=False)
    #, df['price']

fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
#x=range[1:5]
ax1.plot(df['price'].sort_index(ascending=False))
#df['time'].sort_index(0)
#ax2.plot(df.iloc[3].sort_index(0))

plt._show()