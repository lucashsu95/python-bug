'''
下載所有穀保青年的pdf
'''

from bug import Bug
b = Bug('https://www.kpvs.ntpc.edu.tw/files/13-1000-2078.php')
b.setup({})
mm_01 = b.soup.find('table',class_='baseTB')
for a_tag in mm_01.find_all('a')[:5]:
    filename = a_tag.text.strip()
    if filename == '下載附件':continue 

    b.download_file(b.domain + a_tag.get('href'),filename)
    print(f'下載成功',filename)