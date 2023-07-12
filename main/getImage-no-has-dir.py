# 沒有資料夾

import requests
from bs4 import BeautifulSoup
import os

folder_path = 'images'

def openImages():
    print('2.爬圖片需要一點時間，等等吧')

    if os.name == 'nt':
        os.startfile(folder_path)
    elif os.name == 'posix':
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        subprocess.call([opener,folder_path])

# 要爬取的網址
url = input('請輸入網址:')
# 建立資料夾
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
openImages()
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
    folder = os.path.join(folder_path, keyword)
    # 建立分類資料夾
    if not os.path.exists(folder):
        os.makedirs(folder)
    # 下載圖片並存放到對應的資料夾
    filename = img_url.split('/')[-1]
    filepath = os.path.join(folder, filename)
    try:
        with open(filepath, 'wb') as f:
            f.write(requests.get(img_url).content)
    except :
        errFile = open('./images/err.txt','w')
        errFile.write('好像哪裡出錯了XD')
