# 未炸板的首板的板上抛压测试
# 板前交易量
# 换手率(实)
# 交易额与近期对比
import pandas as pd

# 读取 CSV 文件，并使用 `parse_dates` 和 `date_format` 来解析时间
zt_df = pd.read_csv(
    'zt.csv',
    parse_dates=['首次封板时间'],  # 自动解析为 datetime 类型
    date_format='%H%M%S'   # 使用 date_format 指定时间格式
)

# 读取 CSV 文件，并使用 `parse_dates` 和 `date_format` 来解析时间
df = pd.read_csv(
    'stock_data.csv',
    parse_dates=['成交时间'],  # 自动解析为 datetime 类型
    date_format='%H:%M:%S'   # 使用 date_format 指定时间格式
)

# 设置时间区间（例如：10:05:12 到 15:00:00）
start_time = pd.to_datetime('10:05:12', format='%H:%M:%S')
end_time = pd.to_datetime('15:00:00', format='%H:%M:%S')

# 筛选出在时间区间内的数据
filtered_df = df[(df['成交时间'] >= start_time) & (df['成交时间'] <= end_time)]

# 计算该时间区间内的成交金额之和
total_amount = filtered_df['成交金额'].sum()

# 输出结果
print(f"从 {start_time.time()} 到 {end_time.time()} 的成交金额之和为: {total_amount}")