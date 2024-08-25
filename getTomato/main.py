from hsuBug import Bug
from hsuBug.functions import getEnv, downloadByExcel
from dotenv import load_dotenv

load_dotenv()


class Home(Bug):
    def __init__(self, url) -> None:
        self.data = [
            # {'影片名稱':'','導演':'','編劇':'','發行商':''},
        ]
        self.getColumn = {0: "導演", 2: "編劇", 3: "發行商"}
        self.getColumnIdx = [0, 2, 3]
        super().__init__(url)

    def find_table(self, limit: int = 3) -> None:
        table = self.soup.find_all(
            "div", class_="ordered-layout__list ordered-layout__list--carousel"
        )
        if not table:
            print("未找到表格。")
            return

        targetTable = table[1]
        rows = targetTable.find_all("tiles-carousel-responsive-item-deprecated")
        for row in rows[: limit + 1]:
            link = row.find("a")
            if link and link.get("href"):
                subpage_url = self.domain + link.get("href")
                self.get_text(subpage_url)

    def get_text(self, subpage_url: str) -> None:
        subpage = self._create_subpage(subpage_url)
        movie_data = self._extract_movie_data(subpage)
        self.data.append(movie_data)

    def _create_subpage(self, subpage_url: str) -> Bug:
        subpage = Bug(subpage_url)
        subpage.setup(
            {
                "User-Agent": getEnv("SUBPAGE_USER_AGENT"),
                "Cookie": getEnv("SUBPAGE_COOKIE"),
            }
        )
        return subpage

    def _extract_movie_data(self, subpage: Bug) -> dict:
        movie_data = {"影片名稱": subpage.soup.find("h1", class_="unset").text.strip()}
        sec = subpage.soup.find("section", class_="media-info")
        divs = sec.find_all(class_="category-wrap")

        for i, div in enumerate(divs):
            if i in self.getColumn:
                dd = div.find("dd")
                movie_data[self.getColumn[i]] = dd.text.strip().replace("\n", "")

        return movie_data


if __name__ == "__main__":
    home = Home(getEnv("HOME_URL"))
    home.setup(
        {"User-Agent": getEnv("HOME_USER_AGENT"), "Cookie": getEnv("HOME_COOKIE")}
    )
    home.find_table()
    try:
        downloadByExcel(home.data)
        print('output.xlsx 下載成功')
    except Exception as e:
        print(f'output.xlsx 下載失敗 {e}')
