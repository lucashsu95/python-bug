# 有資料夾

from bs4 import BeautifulSoup
import requests
import os
import datetime

folder_path = 'images'

def openImages():
    print('3.爬圖片需要一點時間，等等吧')

    if os.name == 'nt':
        os.startfile(folder_path)
    elif os.name == 'posix':
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        subprocess.call([opener,folder_path])


now = datetime.datetime.now().strftime("%Y%m%d")
input_image = input('請輸入網址:')
response = requests.get(input_image)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("img")
print(response)
image_links = [result.get("src") for result in results]  # 取得圖片來源連結


if not os.path.exists(folder_path):
    os.mkdir(folder_path)  # 建立資料夾
openImages()

for index, link in enumerate(image_links):
    try:
        img = requests.get(link)  # 下載圖片
        with open(f"{folder_path}\\" + now + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼
    except:
        print('err')


