# -*- coding: utf-8 -*-
"""
Created on:     

@author: A.Y
Purpose: 
"""
#获取版本信息"

import tushare as ts
#print('ok')
#print(ts.__version__)
ts.set_token('f20927201ecc20e3cea9279abacfbb1d39a9624820d9b2f94613f722')

pro = ts.pro_api()
df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001', fields='exchange,cal_date,is_open,pretrade_date', is_open='1')