# Function

def getDetail(url):
    import requests
    from bs4 import BeautifulSoup
    import os

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    h1_tags = soup.select_one('h1').text
    h1 = h1_tags.split()
    # 這裡可能會有問題
    folder_path = f'topic/{h1[2]}'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"已創建資料夾：{folder_path}")
    else:
        print(f"資料夾已存在：{folder_path}")

    with open(f'topic/{h1[2]}/{h1[2]}.md' , 'w',encoding='utf-8') as f:
        p = soup.select_one('div.post-content > p').text
        div = soup.select_one('div.post-content > div').text
        wpHead = soup.select('div.post-content > .wp-block-heading')
        wpBlock = soup.select('div.post-content > .wp-block-code')
        blockquote = soup.select_one('div.post-content > blockquote')

        f.write('# ' + h1_tags)
        f.write('\n')
        f.write(p)
        f.write(div)
        f.write('\n')

        if blockquote:
            f.write('> ' + blockquote.text)
            f.write('\n')

        flag = 1
        for i,j in zip(wpHead,wpBlock[:-1]):
            f.write('### ' + i.text)
            f.write('\n')
            f.write('```py')
            f.write('\n')
            f.write(j.text)
            f.write('```')
            f.write('\n')

            if i.text == '範例輸入' or i.text[:-1] == '範例輸入':
                with open(f'topic/{h1[2]}/in{flag}.txt', 'a+', encoding='utf-8') as f2: f2.write(j.text)
            else:
                with open(f'topic/{h1[2]}/out{flag}.txt', 'a+', encoding='utf-8') as f2: f2.write(j.text)
                flag += 1