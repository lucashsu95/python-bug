from FunPy import getDetail
from hsuBug.functions import getEnv,createFolder
from hsuBug.bug import Bug
from dotenv import load_dotenv

load_dotenv()

home: Bug = Bug(getEnv("URL"))
home.setup()
a_tags = home.soup.select("div.post-content > p:nth-of-type(2) a")

createFolder("topic")

if a_tags:
    for a_tag in a_tags:
        link = a_tag["href"]
        getDetail(link)
else:
    print("找不到符合條件的元素。")
