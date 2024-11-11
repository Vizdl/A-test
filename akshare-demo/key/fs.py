import akshare as ak
import pandas as pd
import time
import random
import os
from pathlib import Path

# 读取存储股票代码的 CSV 文件
codes_df = pd.read_csv('codes.csv', dtype={'code': str})

# 设置日期（可以修改为当前日期或自定义日期）
date = "2024-11-08"
start = date + " 09:30:00"  # 起始日期
end = date + " 15:00:00"  # 结束日期，通常和起始日期相同，获取单日数据

# 使用 os.makedirs 创建文件夹，如果文件夹已存在不会报错
os.makedirs(date, exist_ok=True)

# 最大重试次数和每次重试的间隔时间（单位：秒）
max_retries = 3

min_retry_time = 3
max_retry_time = 6

# 循环遍历每个股票代码，下载分时数据并保存为 CSV
for index, row in codes_df.iterrows():
    stock_code = row['code']  # 股票代码
    stock_name = row['name']  # 股票名称

    print(f"开始下载 {stock_name}({stock_code}) 于 {date} 的分时数据...")
    

    file_path = Path(f"{date}/{stock_code}_1min_data.csv")
    # 检查文件是否已存在
    if file_path.exists():
        print(f"文件 {file_path} 已存在，跳过保存。")
        continue

    retries = 0  # 当前重试次数
    while retries < max_retries:
        try:
            # 获取该股票的1分钟分时数据
            df = ak.stock_zh_a_hist_min_em(symbol=str(stock_code), start_date=start, end_date=end, period="1", adjust="")
            
            # 检查是否获取到数据
            if df.empty:
                print(f"No data for {stock_code} on {date}")
            else:
                # 将数据保存到 CSV 文件
                df.to_csv(f"{date}/{stock_code}_1min_data.csv", index=False)
                print(f"Saved {date}/{stock_code}_1min_data.csv")
            
            # 如果获取数据成功，跳出重试循环
            break
        
        except Exception as e:
            retries += 1
            print(f"Failed to fetch data for {stock_code} on {date}. Attempt {retries}/{max_retries}. Error: {e}")
            
            # 如果达到最大重试次数，则跳出循环
            if retries >= max_retries:
                print(f"Max retries reached for {stock_code} on {date}. Skipping this stock.")
                break
            
            # 等待一段时间后再进行下一次重试
            retry_delay = random.randint(min_retry_time, max_retry_time)
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)

    random_seconds = random.randint(min_retry_time, max_retry_time)
    # 等待一段时间后再进行下一次重试
    print("下载成功 " + str(stock_code) + " 于 " + date + " 的分时图等待" + str(random_seconds) + "秒")
    time.sleep(random_seconds)


print("程序运行成功")