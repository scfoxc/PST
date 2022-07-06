import efinance as ef
import pandas as pd

pd.set_option('display.max_rows',5000) # 设置行，列不忽略
pd.set_option('display.max_columns',15)

# df = ef.stock.get_all_company_performance() #获取季报
freq = 1 #获取频率
df = ef.stock.get_quote_history('159949', klt=freq,beg='20200101',end='20201231') #get stock info
print(df)

# df.to_csv('csv/fan.csv', encoding='utf-8-sig', index=None) # 存入csv文件