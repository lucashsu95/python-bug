# Function
from hsuBug.bug import Bug
from hsuBug.functions import createFolder
import time


def write_blockquote(f, blockquote):
    lines = [i for i in blockquote.text.split("。") if i != ""]
    for line in lines:
        f.write("> " + line + "。\n")


def write_table(f, table):
    ths = table.select("th")
    tds = table.select("td")
    tds_len = len(tds)
    ths_len = len(ths)

    f.write("\n")
    f.write("|")
    for th in ths:
        f.write(th.text + "|")
    f.write("\n")

    f.write("|")
    for th in ths:
        f.write("----|")
    f.write("\n")

    for i in range(tds_len // ths_len):
        f.write("|")
        start = i * ths_len
        for td in tds[start : start + ths_len]:
            f.write(td.text + "|")
        f.write("\n")
    f.write("\n")


def write_code_blocks(f, wpHead, wpBlock, folder_path):
    flag = 1
    for i, j in zip(wpHead, wpBlock[:-1]):
        f.write("### " + i.text)
        f.write("\n")
        f.write("```shell")
        f.write("\n")
        f.write(j.text)
        if j.text[-1] != "\n":
            f.write("\n")
        f.write("```")
        f.write("\n")

        # 需要寫入檔案時使用
        # if i.text == "範例輸入" or i.text[:-1] == "範例輸入":
        #     with open(f"{folder_path}/in{flag}.txt", "a+", encoding="utf-8") as f2:
        #         f2.write(j.text)
        # else:
        #     with open(f"{folder_path}/out{flag}.txt", "a+", encoding="utf-8") as f2:
        #         f2.write(j.text)
        #     flag += 1


def getDetail(url):
    time.sleep(5)
    subpage: Bug = Bug(url)
    subpage.setup()

    soup = subpage.soup
    h1_tags = subpage.soup.select_one("h1").text
    h1 = h1_tags.split()

    createFolder("topic")

    folder_path = f"topic/{h1[2]}"
    # createFolder(folder_path)

    # with open(f"{folder_path}/{h1[2]}.md", "w", encoding="utf-8") as f:
    with open(f"topic/{h1[2]}.md", "w", encoding="utf-8") as f:
        p = soup.select_one("div.post-content > p").text
        div = soup.select_one("div.post-content > div").text

        f.write("# " + h1_tags)
        f.write("\n")
        f.write(p)
        f.write(div)
        f.write("\n")

        blockquote = soup.select_one("div.post-content > blockquote")
        if blockquote:
            write_blockquote(f, blockquote)

        table = soup.select_one("div.post-content table")
        if table:
            write_table(f, table)

        wpHead = soup.select("div.post-content > .wp-block-heading")
        wpBlock = soup.select("div.post-content > .wp-block-code")
        write_code_blocks(f, wpHead, wpBlock, folder_path)
    print(f"已完成 {h1_tags}")