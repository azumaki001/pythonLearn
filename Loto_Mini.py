import random
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

basic_url='https://www.mizuhobank.co.jp/retail/takarakuji/loto/backnumber/index.html'
headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
response=requests.get(basic_url, headers=headers, timeout=10)
response.encoding='utf-8'
htm=response.text

soup=BeautifulSoup(htm,'html.parser')

def ball():
    ball_list=[]
    while 1:
        a=random.randint(1,31)
        if a not in ball_list:
            ball_list.append(a)
        if len(ball_list)==5:
            break

    ball_list.sort()
    while 1:
        b=random.randint(1,31)
        if b not in ball_list:
            ball_list.append(b)
        if len(ball_list)==6:
            break
    print(ball_list)

ball()