#获取分钟数据
import data.stock as ds
# data = ds.get_stock_price('159949',freq=101)
# print(data)
# 存入csv
# ds.export_csv(data=data,filename='159949')
# data = ds.read_csv('159949')
# print(data)
df = ds.get_market_list('沪深A股')
print(df)