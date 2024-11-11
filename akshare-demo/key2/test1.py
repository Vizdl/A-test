import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('zt.csv', encoding='utf-8-sig')

# 提取的股票代码列表
target_codes = ['000557', '002065']  # 你可以根据需要修改这个数组

# 遍历股票代码列表，提取对应信息
for code in target_codes:
    # 筛选出对应的股票信息
    stock_info = df[df['代码'] == code]

    # 检查是否找到了对应的股票数据
    if not stock_info.empty:
        # 提取各字段信息
        name = stock_info['名称'].values[0]
       成交额 = stock_info['成交额'].values[0]
        流通市值 = stock_info['流通市值'].values[0]
        总市值 = stock_info['总市值'].values[0]
        换手率 = stock_info['换手率'].values[0]
        封板资金 = stock_info['封板资金'].values[0]
        首次封板时间 = stock_info['首次封板时间'].values[0]

        # 打印结果
        print(f"代码: {code}")
        print(f"名称: {name}")
        print(f"成交额: {成交额}")
        print(f"流通市值: {流通市值}")
        print(f"总市值: {总市值}")
        print(f"换手率: {换手率}")
        print(f"封板资金: {封板资金}")
        print(f"首次封板时间: {首次封板时间}")
        print("-" * 40)
    else:
        print(f"未找到代码 {code} 的股票数据")
