## THIS IS THE TEST ASSIGNMENT CODE
##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = ('http://py4e-data.dr-chuck.net/comments_42.xml')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##bowl = []
##tags = soup('count')
####print(tags)
##
##for tag in tags:
####    Look at the parts of a tag
####   print('TAG:',tag)
####   print('URL:',tag.get('href', None))
####   print('Contents:',tag.contents[0])
####   print('Attrs:',tag.attrs)
####   print('Span:',tag.span)
####   print(soup.find("span", class_="comments"))
##   bowl.extend(tag.contents)
##
####print(bowl)
##
####shock = ['97', '97', '90', '90']
##tally = sum(int(x) for x in bowl)
##print(tally)

## THIS IS THE FINAL ASSIGNMENT CODE
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net/comments_15169.xml')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
bowl = []
tags = soup('count')

for tag in tags:
   bowl.extend(tag.contents)

tally = sum(int(x) for x in bowl)
print(tally)

