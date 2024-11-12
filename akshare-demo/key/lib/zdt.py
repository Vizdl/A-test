import akshare as ak
import pandas as pd
from pathlib import Path

# 涨停池
def down_zt_pool(date):
    df = ak.stock_zt_pool_em(date=date)
    df.to_csv(f'cache/zt/{date}.csv', index=False)

def exist_zt_pool(date):
    path = Path(f'cache/zt/{date}.csv')
    return path.exists()

def update_zt_pool(date):
    if not exist_zt_pool(date):
        down_zt_pool(date)

def get_zt_pool(date):
    update_zt_pool(date)
    df = pd.read_csv(f'cache/zt/{date}.csv', dtype={'代码': str})
    return df

# 炸板池
def down_zb_pool(date):
    df = ak.stock_zt_pool_zbgc_em(date=date)
    df.to_csv(f'cache/zb/{date}.csv', index=False)

def exist_zb_pool(date):
    path = Path(f'cache/zb/{date}.csv')
    return path.exists()

def update_zb_pool(date):
    if not exist_zb_pool(date):
        down_zb_pool(date)

def get_zb_pool(date):
    update_zb_pool(date)
    df = pd.read_csv(f'cache/zb/{date}.csv', dtype={'代码': str})
    return df

# 跌停池
def down_dt_pool(date):
    df = ak.stock_zt_pool_dtgc_em(date=date)
    df.to_csv(f'cache/dt/{date}.csv', index=False)

def exist_dt_pool(date):
    path = Path(f'cache/dt/{date}.csv')
    return path.exists()

def update_dt_pool(date):
    if not exist_dt_pool(date):
        down_dt_pool(date)

def get_dt_pool(date):
    update_dt_pool(date)
    df = pd.read_csv(f'cache/dt/{date}.csv', dtype={'代码': str})
    return df