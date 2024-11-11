import akshare as ak

stock_sector_fund_flow_rank_df = ak.stock_sector_fund_flow_rank(indicator="今日", sector_type="行业资金流")
print(stock_sector_fund_flow_rank_df)