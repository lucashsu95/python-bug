from bs4 import BeautifulSoup
from hsuBug import Bug
from hsuBug.functions import downloadFile, getEnv, checkLink
from tqdm.rich import trange
from dotenv import load_dotenv

load_dotenv()

class Home(Bug):
    def __init__(self, url) -> None:
        super().__init__(url)

    def find_table(self, limit: int = 5) -> str:
        table = self.soup.find("table")
        if not table:
            return "未找到表格。"

        a_tags = table.find_all("a", href=True)[:limit]
        for a_tag in a_tags:
            link = self.domain + "/" + a_tag["href"]
            if checkLink(link):
                print(f"處理連結：{link}")
                self.get_files(link)
            else:
                print(f"連結 {link} 無效")

        return "表格處理完成"

    def get_files(self, subpage_url: str) -> None:
        subpage = self._setup_subpage(subpage_url)
        file_divs = self._find_file_divs(subpage, subpage_url)
        if not file_divs:
            return

        self._download_files(file_divs, subpage_url)

    def _setup_subpage(self, subpage_url: str) -> Bug:
        subpage = Bug(subpage_url)
        user_agent = getEnv("SUBPAGE_USER_AGENT")
        cookie = getEnv("SUBPAGE_COOKIE")
        subpage.setup({"User-Agent": user_agent, "Cookie": cookie})
        return subpage

    def _find_file_divs(self, subpage: Bug, subpage_url: str) -> list:
        file_divs = subpage.soup.find_all(
            "div", class_="list-text file-download-multiple"
        )
        if not file_divs:
            print(f"在子頁面 {subpage_url} 未找到文件。")
        return file_divs

    def _download_files(self, file_divs: list, subpage_url: str) -> None:
        for div in file_divs:
            a_tags = div.find_all("a", href=True)
            for a_tag in trange(len(a_tags)):
                self._download_file(a_tags[a_tag], subpage_url)

    def _download_file(self, a_tag: BeautifulSoup, subpage_url: str) -> None:
        filename = a_tag.get("title", "未知文件名")
        downloaded_file = downloadFile(a_tag["href"], filename)
        print(f"下載完成: {downloaded_file} 下載地點：{subpage_url}")


if __name__ == "__main__":
    web_url = getEnv("WEB_URL")
    user_agent = getEnv("HOME_USER_AGENT")
    cookie = getEnv("HOME_COOKIE")

    home = Home(web_url)
    home.setup({"User-Agent": user_agent, "Cookie": cookie})
    print(home.find_table())
