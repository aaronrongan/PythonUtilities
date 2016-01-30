# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 15:12  

@author: A.Y

本模块目的：
"""

import  tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

# result= td.get_gdp_year()
#result.to_csv("test.csv")
result=ts.get_hist_data('000001')
# plt.figure()
#plt.interactive(False)
#plt.subplot(nrows=2, ncols=1)
fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

ax1.plot(result.iloc[:,1].sort_index(0))
ax2.plot(result.iloc[:,2].sort_index(0))

#fig=result.iloc[:,1].sort_index(0).plot()
#plt.plot(result.iloc[:,2].sort_index(0))
#result.iloc[:,2].sort_index(0).plot()
plt.show()
#result._getitem_column(0).plot()
# plt.figure()

# for _ in result:
#     print _

#print result.icol(1), result.icol(2)
#.icol(2)
#row(10)