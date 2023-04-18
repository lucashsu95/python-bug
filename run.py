import subprocess

# 使用subprocess執行命令，把stdout和stderr輸出給PIPE變數
result = subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 使用result的stdout屬性，得到命令的輸出結果
print(result.stdout.decode('utf-8'))
