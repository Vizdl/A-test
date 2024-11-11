import akshare as ak

# 获取 A股所有股票列表
stock_list = ak.stock_info_a_code_name()

# 打印股票代码和股票名称
print(stock_list)
stock_list.to_csv("A_shares_stock_codes.csv", index=False)