import akshare as ak
import pandas as pd
import os
from pathlib import Path

import sys
sys.path.append('lib')
from fst import *
from utils import *
from info import *

# 读取存储股票代码的 CSV 文件
codes_df = get_all_stock()

# 设置日期（可以修改为当前日期或自定义日期）
date = "2024-11-11"

# 循环遍历每个股票代码，下载分时数据并保存为 CSV
for index, row in codes_df.iterrows():
    stock_code = row['code']  # 股票代码
    stock_name = row['name']  # 股票名称

    print(f"开始下载 {stock_name}({stock_code}) 于 {date} 的分时数据...")
    

    # 检查文件是否已存在
    if fs_exists(date, stock_code):
        print(f"文件已存在，跳过保存。")
        continue

    fs_down(date, stock_code)
    
    wait_rand_time(3, 6)

print("程序运行成功")