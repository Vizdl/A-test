import akshare as ak
import pandas as pd
from datetime import datetime
from pathlib import Path

# 获取当前日期
current_date = datetime.now()
# 格式化为 "YYYYMMDD" 格式
formatted_date = current_date.strftime('%Y%m%d')

# 赚钱效应
def down_zqxy():
    df = ak.stock_market_activity_legu()
    df.to_csv(f'cache/zqxy/{formatted_date}.csv', index=False)

def exists_zqxy():
    file_path = Path(f'cache/zqxy/{formatted_date}.csv')
    # 检查文件是否已存在
    return file_path.exists()

def update_zqxy():
    if not exists_zqxy():
        down_zqxy()
        
def get_trading_volume():
    update_zqxy()
