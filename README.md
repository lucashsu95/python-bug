# python-bug

## 下載需要的套件

```
pip install -r requirements.txt
```


## 升級套件

```
pip install --upgrade requests
```


### `User-Agent`和`Cookie`

可以在想要爬的網頁的`F12`裡的`Network`找到，選擇`文件`來過濾，找到`zh-tw`，找到`user-agent`和`cookie`複制他們(打開F12後記得重新刷新頁面才可以看到)

## class Bug

引用`Bug 類別`的時候記得要先執行`setup()`，<br>並且把`headers`裡的`User-Agent`和`Cookie`準備好

```py
import typing
import re
import time
import os
import requests
from bs4 import BeautifulSoup

class Bug:
    def __init__(self, url) -> None:
        self.url = url
        self.domain = self.get_domain(url)
        self.response = None
        self.soup = None

    def get_domain(self, url: str) -> typing.Union[str, None]:
        domain = re.search(r'(https?://[^/]+)', url)
        if domain:
            return domain.group(1)
        return None

    def setup(self, headers):
        time.sleep(2)
        self.response = requests.get(self.url, headers=headers)
        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, "html.parser")
        else:
            raise Exception(f"Failed to fetch the URL: {self.url}, Status code: {self.response.status_code}")

    def download_file(self, a_tag_href: str,local_filename:str) -> str:
        time.sleep(3)
        if not os.path.exists('files'):
            os.makedirs('files')
            print(f'已創建資料夾: files')
        
        with requests.get(a_tag_href, stream=True) as r:
            r.raise_for_status()
            with open(os.path.join('files', local_filename), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
        return local_filename
```"# python-bug" 
