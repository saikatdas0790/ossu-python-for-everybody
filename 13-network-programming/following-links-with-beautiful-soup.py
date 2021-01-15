import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# url = "http://py4e-data.dr-chuck.net/known_by_Maxx.html"

url = input('Enter URL: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"

count = input('Enter count: ')
if len(count) < 1:
    count = 4
else:
    count = int(count)

position = input('Enter position: ')
if len(position) < 1:
    position = 3
else:
    position = int(position)


def getTags(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup('a')


text = ""
tags = getTags(url)

for iteration in range(count):
    text = tags[position-1].text
    url = tags[position-1].get("href")
    tags = getTags(url)

print(text)
