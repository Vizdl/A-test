import pandas as pd
from jye import *

# 读取 CSV 文件
df = pd.read_csv('zt.csv', dtype={'代码': str})

# 提取的股票代码列表
target_codes = ['000599', '603928']  # 你可以根据需要修改这个数组

# 遍历股票代码列表，提取对应信息
for code in target_codes:
    # 筛选出对应的股票信息
    stock_info = df[df['代码'] == code]

    # 检查是否找到了对应的股票数据
    if not stock_info.empty:
        # 提取所有字段信息
        代码 = stock_info['代码'].values[0]
        名称 = stock_info['名称'].values[0]
        涨跌幅 = stock_info['涨跌幅'].values[0]
        最新价 = stock_info['最新价'].values[0]
        成交额 = stock_info['成交额'].values[0]
        流通市值 = stock_info['流通市值'].values[0]
        总市值 = stock_info['总市值'].values[0]
        换手率 = stock_info['换手率'].values[0]
        封板资金 = stock_info['封板资金'].values[0]
        首次封板时间 = stock_info['首次封板时间'].values[0]
        最后封板时间 = stock_info['最后封板时间'].values[0]
        炸板次数 = stock_info['炸板次数'].values[0]
        涨停统计 = stock_info['涨停统计'].values[0]
        连板数 = stock_info['连板数'].values[0]
        所属行业 = stock_info['所属行业'].values[0]
        
        # 设置时间区间（例如：10:05:12 到 15:00:00）
        start_time = pd.to_datetime(首次封板时间, format='%H%M%S')
        end_time = pd.to_datetime('150000', format='%H%M%S')
        if not exists_trading_volume(代码):
            down_trading_volume(代码)

        板上交易额 = get_trading_volume(代码, start_time, end_time)

        # 打印所有字段信息
        print(f"代码: {代码}")
        print(f"名称: {名称}")
        print(f"涨跌幅: {涨跌幅}")
        print(f"最新价: {最新价}")
        print(f"成交额: {成交额}")
        print(f"流通市值: {流通市值}")
        print(f"总市值: {总市值}")
        print(f"换手率: {换手率}")
        print(f"封板资金: {封板资金}")
        print(f"首次封板时间: {首次封板时间}")
        print(f"最后封板时间: {最后封板时间}")
        print(f"炸板次数: {炸板次数}")
        print(f"涨停统计: {涨停统计}")
        print(f"连板数: {连板数}")
        print(f"所属行业: {所属行业}")
        print(f"板上交易额: {板上交易额}")
        print("-" * 50)
    else:
        print(f"未找到代码 {code} 的股票数据")