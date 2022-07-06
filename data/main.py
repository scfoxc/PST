import efinance as ef
import pandas as pd

pd.set_option('display.max_rows',5000) # 设置行，列不忽略
pd.set_option('display.max_columns',15)

# df = ef.stock.get_realtime_quotes('ETF') #获取指定市场实时数据

'''获取基金的组成'''
# public_dates = ef.fund.get_public_dates('159949')#获取行业
# dates = public_dates[:1]
# df = ef.fund.get_industry_distribution('159949',dates)
# df = ef.fund.get_invest_position('159949')#获取具体股票

#csv中获取数据

print(df)