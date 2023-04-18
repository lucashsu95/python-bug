import subprocess


def installRequests():
    subprocess.run(
        ['pip', 'install', 'requests'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def installBeautifulSoup():
    subprocess.run(
        ['pip', 'install', 'BeautifulSoup4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


installRequests()
installBeautifulSoup()
