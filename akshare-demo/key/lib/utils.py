import sys
import time
import random

def wait_rand_time(min, max):
    random_seconds = random.randint(min, max)
    time.sleep(random_seconds)
    print("等待中...")