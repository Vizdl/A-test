import sys
sys.path.append('lib')
from jye import *
from zdt import *
from zqxy import *

date="20241112"

# 涨跌停股票
update_zt_pool(date=date)
update_zb_pool(date=date)
update_dt_pool(date=date)

# 下载所有涨跌停的股票的交易额
update_trading_volume


# 下载所有涨跌停的股票的分时图


# 当日行情
update_zqxy()