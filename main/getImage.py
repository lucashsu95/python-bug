from bs4 import BeautifulSoup
import requests
import os
import datetime

folder_path = 'images'

def openImages():
    print('2. 爬圖片需要一點時間，等等吧')

    os.startfile(folder_path)
    # if os.name == 'nt':
    #     os.startfile(folder_path)
    # elif os.name == 'posix':
    #     opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
    #     subprocess.call([opener,folder_path])


now = datetime.datetime.now().strftime("%Y%m%d")

input_image = input('請輸入網址:')
cookie = input('cookie:')
limit = int(input('需要幾張呢? :'))

headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cookie':cookie
        }
response = requests.get(input_image,headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
results = soup.find_all("img")  
print(response)
image_links = [result.get("src") for result in results]  # 取得圖片來源連結


if not os.path.exists(folder_path):
    os.mkdir(folder_path)  # 建立資料夾
openImages()

for i in range(limit):
    try:
        img = requests.get(image_links[i])  # 下載圖片
        with open(f"{folder_path}\\" + now + str(i+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼
    except:
        print('err')

# for index, link in enumerate(image_links):
#     try:
#         img = requests.get(link)  # 下載圖片
#         with open(f"{folder_path}\\" + now + str(index+1) + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
#             file.write(img.content)  # 寫入圖片的二進位碼
#     except:
#         print('err')
