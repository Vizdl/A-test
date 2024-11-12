import akshare as ak
import pandas as pd
import time
import random
import os
from pathlib import Path

# 读取存储股票代码的 CSV 文件
codes_df = pd.read_csv('cache/all/codes.csv', dtype={'code': str})

# 设置日期（可以修改为当前日期或自定义日期）
date = "2024-11-08"
start = date + " 09:30:00"  # 起始日期
end = date + " 15:00:00"  # 结束日期，通常和起始日期相同，获取单日数据

# 使用 os.makedirs 创建文件夹，如果文件夹已存在不会报错
os.makedirs(date, exist_ok=True)

min_retry_time = 3
max_retry_time = 6

# 循环遍历每个股票代码，下载分时数据并保存为 CSV
for index, row in codes_df.iterrows():
    stock_code = row['code']  # 股票代码
    stock_name = row['name']  # 股票名称

    print(f"开始下载 {stock_name}({stock_code}) 于 {date} 的分时数据...")
    

    file_path = Path(f"{date}/{stock_code}_1min_data.csv")
    # 检查文件是否已存在
    if fs_exists(date, stock_code):
        print(f"文件 {file_path} 已存在，跳过保存。")
        continue

    fs_down(date, stock_code)
    random_seconds = random.randint(min_retry_time, max_retry_time)
    # 等待一段时间后再进行下一次重试
    print("下载成功 " + str(code) + " 于 " + date + " 的分时图等待" + str(random_seconds) + "秒")
    time.sleep(random_seconds)


print("程序运行成功")