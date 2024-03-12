import requests
from bs4 import BeautifulSoup
import time
from FunPy import getDetail


url = 'https://jbprogramnotes.com/2020/05/tqc-%e7%a8%8b%e5%bc%8f%e8%aa%9e%e8%a8%80python-%e7%ac%ac4%e9%a1%9e%ef%bc%9a%e9%80%b2%e9%9a%8e%e6%8e%a7%e5%88%b6%e6%b5%81%e7%a8%8b/'
response = requests.get(url)
time.sleep(1)
soup = BeautifulSoup(response.text, 'html.parser')

a_tags = soup.select('div.post-content > p:nth-of-type(2) a')

if a_tags:
    for a_tag in a_tags:
        link = a_tag['href']
        getDetail(link)
        time.sleep(5)

else:
    print("找不到符合條件的元素。")