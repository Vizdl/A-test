import pandas as pd
import akshare as ak
from pathlib import Path
import os

# 未炸板的首板的板上抛压测试
# 板前交易量
# 换手率(实)
# 交易额与近期对比

# 判断交易额数据是否存在
def exists_trading_volume(date, code):
    file_path = Path(f'cache/jye/{date}/{code}.csv')
    # 检查文件是否已存在
    return file_path.exists()

# 下载交易额数据
def down_trading_volume(date, code):
    stock_zh_a_tick_tx_js_df = ak.stock_zh_a_tick_tx_js(symbol="sh" + code)
    # 使用 os.makedirs 创建文件夹，如果文件夹已存在不会报错
    os.makedirs(f'cache/jye/{date}', exist_ok=True)
    print(stock_zh_a_tick_tx_js_df)
    # 保存为 CSV 文件
    stock_zh_a_tick_tx_js_df.to_csv(f'cache/jye/{date}/{code}.csv', index=False)

def update_trading_volume(date, code):
    if not exists_trading_volume(date, code):
        down_trading_volume(date, code)

# 查看交易额
# 1. 股票代码
# 2. 开始时间
# 2. 结束时间
def get_trading_volume(date, code, start_time, end_time):
    update_trading_volume(date, code)

    # 读取 CSV 文件，并使用 `parse_dates` 和 `date_format` 来解析时间
    df = pd.read_csv(
        f'cache/jye/{date}/{code}.csv',
        parse_dates=['成交时间'],  # 自动解析为 datetime 类型
        date_format='%H:%M:%S'   # 使用 date_format 指定时间格式
    )

    # 筛选出在时间区间内的数据
    filtered_df = df[(df['成交时间'] >= start_time) & (df['成交时间'] <= end_time)]

    # 计算该时间区间内的成交金额之和
    total_amount = filtered_df['成交金额'].sum()

    # 输出结果
    # print(f"从 {start_time.time()} 到 {end_time.time()} 的成交金额之和为: {total_amount}")
    return total_amount
