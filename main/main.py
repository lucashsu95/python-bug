import subprocess

def fs_getImage(pyFileName):
    subprocess.run(
        ['python', pyFileName])


print('1. 要使用多個資料夾做分類嗎? 請直接(Enter)')
print('2. 要使用一個資料夾做分類嗎? 請按(y)')

flag = input()
if(flag == 'y' or flag == 'Y'):
    fs_getImage('getImage-no-has-dir.py')
else:
    fs_getImage('getImage.py')


#https://yuc.wiki/202304/ 爬蟲範例網站