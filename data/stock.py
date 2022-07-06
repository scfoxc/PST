import efinance as ef
import pandas as pd


def get_market_list(type):
    '''
    获取需要获取的市场列表
    'None' 沪深京A股市场行情
    '沪深A股' 沪深A股市场行情
    '沪A' 沪市A股市场行情
    '深A' 深市A股市场行情
    '北A' 北证A股市场行情
    '可转债' 沪深可转债市场行情
    '期货' 期货市场行情
    '创业板' 创业板市场行情
    '美股' 美股市场行情
    '港股' 港股市场行情
    '中概股' 中国概念股市场行情
    '新股' 沪深新股市场行情
    '科创板' 科创板市场行情
    '沪股通' 沪股通市场行情
    '深股通' 深股通市场行情
    '行业板块' 行业板块市场行情
    '概念板块' 概念板块市场行情
    '沪深系列指数' 沪深系列指数市场行情
    '上证系列指数' 上证系列指数市场行情
    '深证系列指数' 深证系列指数市场行情
    'ETF' ETF 基金市场行情
    'LOF' LOF 基金市场行情
    :return: 市场列表
    '''
    market = ef.stock.get_realtime_quotes(fs=type)
    return market

# def get_stock_price_min(code):
#     '''
#     获取指定股票当天分钟行情
#     '''
#     data_min = ef.stock.get_quote_history(stock_codes=code,klt='1')
#     return data_min

def get_stock_price(code,freq):
    '''
    获取股票行情
    :param code_day: 股票代码
    :return:
    '''
    data = ef.stock.get_quote_history(stock_codes=code,klt=freq)
    return data

def export_csv(data,filename):
    '''
    导出股票行情数据到csv文件
    :param data: 导出到日期
    :param filename:导出的文件
    :return:
    '''
    fileroot = '/Users/dan/PycharmProjects/dan/csv/' + filename + '.csv'
    data.to_csv(fileroot)
    print('成功存储到:', fileroot)

def read_csv(code):
    '''

    :param code: 股票代码
    :return: 读取的csv值
    '''
    fileroot = '/Users/dan/PycharmProjects/dan/csv/' + code + '.csv'
    return pd.read_csv(fileroot)

def transfer_price_freq(data,fime_freq):
    '''
    转换股票行情周期
    :return:
    '''

    df['日期'] = pd.to_datetime(df['日期']) #把日期“格式化”
    df = df.set_index('日期') #定义日期为index项
    df_trans=pd.DataFrame()
    df_trans['开盘']=data['开盘'].resample(fime_freq).first() # open 周k W 月k M
    df_trans['收盘']=data['收盘'].resample(fime_freq).last() # close
    df_trans['最高']=data['最高'].resample(fime_freq).max() # high
    df_trans['最低']=data['最低'].resample(fime_freq).min() # low
    return df_trans

# - 行情数据写入数据库
# - 获取单个股票财务指标
# - 获取单个股票估值
# - 获取对应基金的组成
# - 获取价格/权重
# - 获取基金净值