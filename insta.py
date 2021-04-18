import webbrowser
import time
import requests
from bs4 import BeautifulSoup
import os

wb = webbrowser
wb.open('https://www.instagram.com/explore/tags/komorebi_memories/')

for i in range(1,4):
  time.sleep(1)
  print(i)

time.sleep(1)
#judge = input()

#if judge == 'y':
load_url = "https://www.instagram.com/explore/tags/komorebi_memories/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")
print(soup)
#else:
#    print('end')

#os.wgetcwd()
