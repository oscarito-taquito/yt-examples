import os
from bs4 import BeautifulSoup
cur_path = os.getcwd()
file = os.path.join(cur_path, 'html', 'podcast-mic.html')

with open(file, 'r') as f:
    doc = BeautifulSoup(f, 'html.parser')

tag = doc.title
print(tag.string)

divs = doc.find_all('div')
print(divs)
