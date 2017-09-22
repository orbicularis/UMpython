import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
bowl = []
bigCount = 0
count = 0
tags = soup('a')
print(tags)


for tag in tags:
   if count < 18:
##      print(tag2.get('href', None))
      bowl.clear()
      bowl.append(tag)
      count += 1

##spoon = str(bowl)
##cup = spoon.split('"')
##newLink = cup[1]
##print(newLink)
##bigCount += 1
##
##while bigCount < 7:
##   url = newLink
##   html = urllib.request.urlopen(url, context=ctx).read()
##   soup = BeautifulSoup(html, 'html.parser')
##   bowl = []
##   count = 0
##   tags = soup('a')
##
##   for tag in tags:
##      if count < 18:
####         print(tag2.get('href', None))
##         bowl.clear()
##         bowl.append(tag)
##         count += 1
##
##   spoon = str(bowl)
##   cup = spoon.split('"')
##   newLink = cup[1]
##   print(newLink)
##   bigCount += 1
##
##print('done')
