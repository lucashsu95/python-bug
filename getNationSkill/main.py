import os
from bs4 import BeautifulSoup
from hsuBug import Bug
from hsuBug.functions import downloadFile, getEnv
from rich.text import Text
from tqdm.rich import trange

from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv

load_dotenv()


class Home(Bug):
    def __init__(self, url: str) -> None:
        super().__init__(url)

    def get_home_page_table(self) -> list:
        return self.find_table()

    def find_table(self, limit: int = 5) -> list:
        table: BeautifulSoup = self.soup.find("table", class_="table table-bordered")
        if not table:
            return "未找到表格。"

        data: list = []
        rows: list = table.find_all("tr")[: limit + 1]

        for row in rows:
            cols: list = row.find_all(["td", "th"])
            ary: list = self._process_row(cols)
            data.append(ary)

        return data

    def _process_row(self, cols: list) -> list:
        ary: list = []
        for i, col in enumerate(cols):
            if i in {1, 2, 5, 6}:
                continue
            text: str = self._clean_text(col.get_text())
            link: BeautifulSoup = col.find("a", {"href": True})
            if link:
                link_url: str = self.domain + link.get("href")
                ary.extend([Text(text, style=f"link {link_url}"), link_url])
                subpage: Bug = self._setup_subpage(link_url)
                self.get_files(subpage)
            else:
                ary.append(text)
        return ary

    def _setup_subpage(self, subpage_url: str) -> Bug:
        subpage: Bug = Bug(subpage_url)
        subpage.setup(
            {
                "User-Agent": getEnv("SUBPAGE_USER_AGENT"),
                "Cookie": getEnv("SUBPAGE_COOKIE"),
            }
        )
        return subpage

    def get_files(self, subpage: Bug) -> None:
        fileUl: BeautifulSoup = subpage.soup.find("ul", id="FileUl")
        if not fileUl:
            return

        a_tags: list = fileUl.find_all("a", {"href": True})

        table2: BeautifulSoup = subpage.soup.find("table", class_="table2")
        td_tag: BeautifulSoup = table2.find("tr").find("td")
        title: str = self._clean_text(td_tag.text)
        for a_tag_index in trange(len(a_tags)):
            a_tag: BeautifulSoup = a_tags[a_tag_index]
            a_url: str = self.domain + "/" + a_tag.get("href").replace("../", "")

            os.makedirs(os.path.join("download_files", title), exist_ok=True)
            filename = os.path.join(title, a_tag.text.strip())
            downloadFile(a_url, filename)
            print(f"下載完成: {filename} 下載地點：{subpage.url}")

    @staticmethod
    def _clean_text(text: str) -> str:
        return text.strip().replace(" ", "").replace("\r", "").replace("\n", "")

    @staticmethod
    def print_table(title: str, data: list) -> None:
        table: Table = Table(title=title)
        for row in data[0]:
            table.add_column(row)

        for row in data[1:]:
            table.add_row(*row)

        Console().print(table)


if __name__ == "__main__":
    home: Home = Home(getEnv("HOME_URL"))
    home.setup(
        {
            "User-Agent": getEnv("HOME_USER_AGENT"),
            "Cookie": getEnv("HOME_COOKIE"),
        }
    )
    table: list = home.get_home_page_table()
    home.print_table("首頁表格", table)
