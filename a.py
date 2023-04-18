import os
import requests
from bs4 import BeautifulSoup
import subprocess
import importlib



def hasRequests():
    try:
        importlib.import_module('requests')
    except ImportError:
        result = subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    else:
        print('requests模块已安装')


def hasBeautifulSoup():
    try:
        importlib.import_module('BeautifulSoup')
    except ImportError:
        result = subprocess.run(['pip', 'install', 'BeautifulSoup'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    else:
        print('requests模块已安装')


# 要爬取的網址
url = input('請輸入網址:')
# 建立資料夾
if not os.path.exists('images'):
    os.makedirs('images')
# 發送 HTTP GET 請求並取得回應
response = requests.get(url)
# 解析回應的 HTML 內容
soup = BeautifulSoup(response.content, 'html.parser')
# 找到所有的圖片
img_tags = soup.find_all('img')
# 下載圖片
for img in img_tags:
    img_url = img.get('src')
    # 從 URL 中獲取關鍵詞
    keyword = img_url.split('/')[-2]
    folder = os.path.join('images', keyword)
    # 建立分類資料夾
    if not os.path.exists(folder):
        os.makedirs(folder)
    # 下載圖片並存放到對應的資料夾
    filename = img_url.split('/')[-1]
    filepath = os.path.join(folder, filename)
    with open(filepath, 'wb') as f:
        f.write(requests.get(img_url).content)
