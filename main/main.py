import subprocess

def fs_getImage(pyFileName):
    subprocess.run(
        ['python', pyFileName])

# print('1. 要使用多個資料夾做分類嗎? yes(y) no (n) ')
# flag = input()
# if(flag == 'y'):
#     fs_getImage('getImage-no-has-dir.py')
# else:
#     fs_getImage('getImage.py')
fs_getImage('getImage.py')