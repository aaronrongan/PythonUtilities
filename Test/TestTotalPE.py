# 获取全市场股票PE
import jqdatasdk

from jqdatasdk import *
query_date='2109-3-1'
all_stock = jqdatasdk.get_all_securities(['stock'], date=query_date)
stocks = list(all_stock.index)
print(" 全市场", len(stocks), "只股票信息")

stock1 = stocks[:2000]
stock2 = stocks[2000:]

q1 = jqdatasdk.query(
    jqdatasdk.valuation.code, jqdatasdk.valuation.day, jqdatasdk.valuation.pe_ratio, jqdatasdk.valuation.pb_ratio
).filter(
    jqdatasdk.valuation.code.in_(stock1)
)
df1 = jqdatasdk.get_fundamentals(q1, date=query_date)
df1.to_sql(name='stock_valuations', if_exists='append', con=conn, index=False)

q2 = jqdatasdk.query(
    jqdatasdk.valuation.code, jqdatasdk.valuation.day, jqdatasdk.valuation.pe_ratio, jqdatasdk.valuation.pb_ratio
).filter(
    jqdatasdk.valuation.code.in_(stock2)
)
df2 = jqdatasdk.get_fundamentals(q2, date=query_date)
df2.to_sql(name='stock_valuations', if_exists='append', con=conn, index=False)

stock_fund = pd.concat([df1, df2]).set_index('code')

# 计算全市场等权PE
pe_ew = len(stock_fund["pe_ratio"]) / stock_fund["pe_ratio"].apply(get_pe_trans).sum()
# print(" 全市场等权PE=", pe_ew)

# 计算全市场等权PB
pb_ew = len(stock_fund["pb_ratio"]) / stock_fund["pb_ratio"].apply(get_pe_trans).sum()
# print(" 全市场等权PB=", pb_ew)