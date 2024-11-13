import akshare as ak
import pandas as pd

def down_all_stock():
    # 获取 A股所有股票列表
    stock_list = ak.stock_info_a_code_name()

    # 打印股票代码和股票名称
    print(stock_list)
    stock_list.to_csv("A_shares_stock_codes.csv", index=False)

def get_all_stock():
    return pd.read_csv('cache/all/codes.csv', dtype={'code': str})

def get_stock_info(code):
    stock_individual_info_em_df = ak.stock_individual_info_em(symbol=code)
    print(stock_individual_info_em_df)