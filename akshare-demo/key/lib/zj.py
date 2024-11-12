import akshare as ak
import pandas as pd
from pathlib import Path

# 行业资金流向
def down_hyzj():
    stock_fund_flow_industry_df = ak.stock_fund_flow_industry(symbol="即时")
    print(stock_fund_flow_industry_df)

# 概念资金流向
def down_gnzj():
    stock_fund_flow_concept_df = ak.stock_fund_flow_concept(symbol="即时")
    print(stock_fund_flow_concept_df)

## 大盘资金流向
def down_pdzj():
    stock_market_fund_flow_df = ak.stock_market_fund_flow()
    print(stock_market_fund_flow_df)