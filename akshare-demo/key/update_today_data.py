import sys
sys.path.append('lib')
from jye import *
from zdt import *
from zqxy import *
from utils import *

date="20241114"

# 涨跌停股票
update_zt_pool(date=date)
update_zb_pool(date=date)
update_dt_pool(date=date)

# 下载所有涨跌停的股票的交易额
zt_df = get_zt_pool(date=date)
for index, row in zt_df.iterrows():
    stock_code = row['代码']  # 股票代码
    stock_name = row['名称']  # 股票名称

    print(f"涨停 : ")
    print(f"代码: {stock_code}")
    print(f"名称: {stock_name}")
    update_trading_volume(date, stock_code)
    wait_rand_time(3, 6)

dt_df = get_dt_pool(date=date)
for index, row in dt_df.iterrows():
    stock_code = row['代码']  # 股票代码
    stock_name = row['名称']  # 股票名称

    print(f"跌停 : ")
    print(f"代码: {stock_code}")
    print(f"名称: {stock_name}")
    update_trading_volume(date, stock_code)
    wait_rand_time(3, 6)

zb_df = get_zb_pool(date=date)
for index, row in zb_df.iterrows():
    stock_code = row['代码']  # 股票代码
    stock_name = row['名称']  # 股票名称

    print(f"炸板 : ")
    print(f"代码: {stock_code}")
    print(f"名称: {stock_name}")
    update_trading_volume(date, stock_code)
    wait_rand_time(3, 6)


# 下载所有涨跌停的股票的分时图


# 当日行情
update_zqxy()