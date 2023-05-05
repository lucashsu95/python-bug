# 有資料夾

from bs4 import BeautifulSoup
import requests
import os
import datetime

now = datetime.datetime.now().strftime("%Y%m%d")
input_image = input('網址:')
response = requests.get(input_image)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("img")
print(response)
image_links = [result.get("src") for result in results]  # 取得圖片來源連結

if not os.path.exists("images"):
    os.mkdir("images")  # 建立資料夾

for index, link in enumerate(image_links):
    try:
        img = requests.get(link)  # 下載圖片
        with open("images\\" + now + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼
    except:
        print('err')
