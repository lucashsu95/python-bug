import subprocess


def installRequests():
    print('正在幫您安裝')
    subprocess.run(
        ['pip', 'install', 'requests'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('requests庫已安裝')


def installBeautifulSoup():
    print('正在幫您安裝')
    subprocess.run(
        ['pip', 'install', 'BeautifulSoup4'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('BeautifulSoup庫已安裝')


try:
    import requests
except ImportError:
    print('requests庫未安裝')
    installRequests()

try:
    from bs4 import BeautifulSoup
except ImportError:
    print('BeautifulSoup庫未安裝')
    installBeautifulSoup()
