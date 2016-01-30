# -*- coding: utf-8 -*-
"""
Created on 2016/1/6 17:53  

@author: A.Y

本模块目的：
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#plt.figure()


# ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
#ts.plot()
# ts=ts.cumsum()
# ts.plot()

df=pd.DataFrame(np.random.rand(100),index=pd.date_range('1/1/2000',periods=100))
# ,columns=['A','B','C','D']
#print df
#df=df.cumsum()
#plt.figure()
#plt.interactive(False)
df.plot()
plt._show()
# plt.legend(loc='best')