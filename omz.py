import webbrowser
import time
import requests
from bs4 import BeautifulSoup as bs4
import os
from googletrans import Translator

translator = Translator()
wb = webbrowser()

"""
wb.open('http://omz-software.com/pythonista/docs/')
 
for i in range(1,4):
  time.sleep(1)
  print(i)
"""

time.sleep(1)
load_url = "http://omz-software.com/pythonista/docs/"
html = requests.get(load_url)
soup = bs4(html.content, "html.parser")
p = [tag.text for tag in soup()]
#print(p)

trans_en_ja = translator.translate(p,dest='ja')
print(trans_en_ja)
