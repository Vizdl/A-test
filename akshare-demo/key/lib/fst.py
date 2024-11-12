import akshare as ak
import pandas as pd
import time
import random
import os
from pathlib import Path

min_retry_time = 3
max_retry_time = 6

def fs_exists(date, code):
    file_path = Path(f"cache/fs/{date}/{code}_1min_data.csv")
    # 检查文件是否已存在
    return file_path.exists()

def fs_down(date, code):
    start = date + " 09:30:00"  # 起始日期
    end = date + " 15:00:00"  # 结束日期，通常和起始日期相同，获取单日数据
    # 使用 os.makedirs 创建文件夹，如果文件夹已存在不会报错
    os.makedirs(f"cache/fs/{date}", exist_ok=True)
    # 最大重试次数和每次重试的间隔时间（单位：秒）
    max_retries = 3
    retries = 0  # 当前重试次数
    while retries < max_retries:
        try:
            # 获取该股票的1分钟分时数据
            df = ak.stock_zh_a_hist_min_em(symbol=str(code), start_date=start, end_date=end, period="1", adjust="")
            
            # 检查是否获取到数据
            if df.empty:
                print(f"No data for {code} on {date}")
            else:
                # 将数据保存到 CSV 文件
                df.to_csv(f"cache/fs/{date}/{code}_1min_data.csv", index=False)
                print(f"Saved {date}/{code}_1min_data.csv")
            
            # 如果获取数据成功，跳出重试循环
            break
        
        except Exception as e:
            retries += 1
            print(f"Failed to fetch data for {code} on {date}. Attempt {retries}/{max_retries}. Error: {e}")
            
            # 如果达到最大重试次数，则跳出循环
            if retries >= max_retries:
                print(f"Max retries reached for {code} on {date}. Skipping this stock.")
                break
            
            # 等待一段时间后再进行下一次重试
            retry_delay = random.randint(min_retry_time, max_retry_time)
            print(f"Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)