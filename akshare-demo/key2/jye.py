# 描述: 每个交易日 16:00 提供当日数据; 如遇到数据缺失, 请使用 ak.stock_zh_a_tick_163() 接口(注意数据会有一定差异)
# 限量: 单次返回最近交易日的历史分笔行情数据
# 输入参数-历史行情数据

import pandas as pd
import akshare as ak

stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol="sz000599")
print(stock_zh_a_tick_tx_js_df)

# 保存为 CSV 文件
stock_zh_a_tick_tx_js_df.to_csv('stock_data.csv', index=False)