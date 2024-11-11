import akshare as ak
import pandas as pd

# 目标地址: https://quote.eastmoney.com/ztb/detail#type=ztgc
# 描述: 东方财富网-行情中心-涨停板行情-涨停股池
# 限量: 单次返回指定 date 的涨停股池数据; 该接口只能获取近期的数据

stock_zt_pool_em_df = ak.stock_zt_pool_em(date='20241111')
print(stock_zt_pool_em_df)

# 保存为 CSV 文件
stock_zt_pool_em_df.to_csv('zt.csv', index=False)