import requests
from bs4 import BeautifulSoup
import sys
import json

'''
pip install requests

pip install beautifulsoup4

pip install lxml
'''
# 獲得php傳的值
input_image = str(sys.argv[1])
# input_image = ''
response = requests.get(input_image)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("img")
# print(response)
image_links = [result.get("src") for result in results]  # 取得圖片來源連結
result = json.dumps(image_links)
print(result)
