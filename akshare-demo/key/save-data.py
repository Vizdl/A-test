import pandas as pd

# 示例数据：二维数组
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]

# 将数据转换为 DataFrame
df = pd.DataFrame(data[1:], columns=data[0])
# 打印保存的数据
print(df)

# 将 DataFrame 存入 CSV 文件
df.to_csv("output.csv", index=False)


# 从 CSV 文件读取数据
df_restored = pd.read_csv("output.csv")

# 打印恢复的数据
print(df_restored)






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
                df.to_csv(f"{stock_code}_1min_data_{date}.csv", index=False)
                print(f"Saved {stock_code}_1min_data_{date}.csv")
            
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


    # 生成一个随机数，范围在 120 到 240 秒之间（2分钟到4分钟）
    random_seconds = random.randint(min_retry_time, max_retry_time)
    # 等待一段时间后再进行下一次重试
    print("下载成功 " + str(stock_code) + " 于 " + date + " 的分时图等待" + str(random_seconds) + "秒")
    time.sleep(random_seconds)
    break


print("程序运行成功")