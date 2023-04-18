import subprocess

# 执行命令并等待完成
result = subprocess.run(['python', 'hello.py'], capture_output=True, text=True)

# 获取命令输出和返回值
output = result.stdout
returncode = result.returncode

print(output)
print(returncode)
