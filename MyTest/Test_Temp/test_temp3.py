
import pandas as pd
import tushare as ts
#result=ts.get_sz50s()
#result=ts.get_area_classified()
#result=ts.get_h_data('000001', start='2015-12-01')
#df = ts.get_realtime_quotes('002777') #Single stock symbol

#df[['code','name','price','bid','ask','volume','amount','time']]
#print(result)
#print(df)

#df=ts.get_hist_data('000777','20151230','20160106','D',3)
#print(df)
#df =ts.cap_tops(5)
df = ts.top_list('2016-01-05')
#df.to_csv("1.csv")


print(df)
