
#https://www.joinquant.com/help/api/help?name=JQData#%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85%E4%BD%BF%E7%94%A8JQData

import jqdatasdk

from jqdatasdk import *

jqdatasdk.auth('13651829783', 'aaronjoinquant')

#print(__version__)

#print(get_query_count())

q=query(finance.STK_FIN_FORCAST).filter(finance.STK_FIN_FORCAST.code=='300383.XSHE',finance.STK_FIN_FORCAST.pub_date>='2018-07-01').limit(10)
df=finance.run_query(q)
print(df)