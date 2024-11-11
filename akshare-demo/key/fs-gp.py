import akshare as ak

# 获取 1 分钟分时数据，使用 东方财富网提供的 stock_zh_a_hist_min_em
stock_code = "000001"  # 股票代码，例子是上证指数
date = "2024-11-08"
start = date + " 09:30:00"  # 起始日期
end = date + " 15:00:00"  # 结束日期，通常和起始日期相同，获取单日数据

# 注意：该接口返回的数据只有最近一个交易日的有开盘价，其他日期开盘价为 0
stock_zh_a_hist_min_em_df = ak.stock_zh_a_hist_min_em(symbol=stock_code, start_date=start, end_date=end, period="1", adjust="")
print(stock_zh_a_hist_min_em_df)
stock_zh_a_hist_min_em_df.to_csv(f"{stock_code}_1min_data_{date}.csv", index=False)