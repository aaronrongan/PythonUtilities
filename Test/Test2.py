import tushare as ts
#ts.set_token('f20927201ecc20e3cea9279abacfbb1d39a9624820d9b2f94613f722')
#获取股票列表
pro = ts.pro_api()

#获取公司清单
#data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

#获取龙虎榜数据
#data = pro.top_list(trade_date='20190215')
#print(data)

#获取某股区间涨幅

#获取开户人数
#data = pro.stk_account(start_date='20190104', end_date='20190215')

#获取当日票房排名及总收入
#data= pro.bo_daily(date='20190217')
#print(data.name,data.total)
