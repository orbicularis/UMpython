##handy website placeholder
## http://data.pr4e.org/romeo.txt


####THIS is exercise 1
##import socket
##
##userURL = input('Please enter a URL: ')
####print(userURL)
##splitURL = userURL.split('/')
####print(splitURL)
##domain = splitURL[2]
####print(domain)
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect((domain, 80))
##
##cmd = 'GET ' + userURL + ' HTTP/1.0\r\n\r\n'
##cmd1 = cmd.encode()
##
####print(cmd1)
##
##mysock.send(cmd1)
##
##while True:
##    data = mysock.recv(512)
##    if (len(data) < 1):
##        break
##    print(data.decode())
##
##mysock.close()

####THIS is exercise 1 with a try statement
##import socket
##
##try:
##    userURL = input('Please enter a URL: ')
##    ##print(userURL)
##    splitURL = userURL.split('/')
##    ##print(splitURL)
##    domain = splitURL[2]
##    ##print(domain)
##
##    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##    mysock.connect((domain, 80))
##
##except:
##   print('Unable to parse that URL, please check spelling') 
##    
##try:
##    cmd = 'GET ' + userURL + ' HTTP/1.0\r\n\r\n'
##    cmd1 = cmd.encode()
##
##    ##print(cmd1)
##
##    mysock.send(cmd1)
##
##    while True:
##        data = mysock.recv(512)
##        if (len(data) < 1):
##            break
##        print(data.decode())
##
##    mysock.close()
##
##except:
##    print('')

####THIS is exercise 2 counting characters returned
##import socket
##bucket = list()
##
####userURL = input('Please enter a URL: ')
##userURL = 'http://data.pr4e.org/romeo.txt'
##splitURL = userURL.split('/')
##domain = splitURL[2]
##tank = list()
##count = 0
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect((domain, 80))
##
##cmd = 'GET ' + userURL + ' HTTP/1.0\r\n\r\n'
##cmd1 = cmd.encode()
##mysock.send(cmd1)
##
##while True:
##    data = mysock.recv(512)
##    if (len(data) < 1):
##        break
####    print(data.decode())
##    bucket = data.decode()
##    for letter in bucket:
##        tank.extend(letter)
##        count += 1
##print('First 100 chracters: \n', tank[0:100])
##print('Total characters in document is', count)

####THIS is exercise 3, using URLLIB
##import urllib.request, urllib.parse, urllib.error
##
##fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
##
##words = list()
##for line in fhand:
##    word = list(line.decode().split())
##    words.extend(word)
##
##wordString = str(words)
##out = "[],'"
##for char in out:
##    wordString = wordString.replace(char, '')
####print(wordString)
##
##letters = list(wordString)
##print(letters[0:10])
##
##count = 0
##for letter in letters:
##    count += 1
##
##print(count)

##x = list(letters[1:])
##
##print(x)

    
##print(letters)

##    for word in words:
##        theWord.extend(word)
##        count += 1
        
##print(theWord[0:5])
##print(count)

####THIS is exercise 4
##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
####url = input('Enter - ')
##url = ('http://www.dr-chuck.com/page1.htm')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##
####print(soup)
##
##words = str(soup)
##letters = list(words)
##print(letters[0:20])
##
##count = 0
##
##for letter in letters:
##    count += 1
##
##print(count)
    
######THIS IS ASSIGNMENT 1 URL: 'http://py4e-data.dr-chuck.net/comments_42.html'
### EXTRA CODE EXAMPLE To run this, you can install BeautifulSoup
### https://pypi.python.org/pypi/beautifulsoup4
### Or download the file
### http://www.py4e.com/code3/bs4.zip
### and unzip it in the same directory as this file
##
##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##import ssl
##import re
##
### Ignore SSL certificate errors
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = ('http://py4e-data.dr-chuck.net/comments_42.html')
##html = urlopen(url, context=ctx).read()
####print(html)
##
### html.parser is the HTML parser included in the standard Python 3 library.
### information on other HTML parsers is here:
### http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
##soup = BeautifulSoup(html, "html.parser")
####print(soup)
##
##### Retrieve all of the anchor tags
####tags = soup('td')
####print(tags)
##
### Retrieve all of the anchor tags
##summer = []
##tags = soup('span')
##for tag in tags:
####    Look at the parts of a tag
####   print('TAG:',tag)
####   print('URL:',tag.get('href', None))
####   print('Contents:',tag.contents[0])
####   print('Attrs:',tag.attrs)
####   print('Span:',tag.span)
####   print(soup.find("span", class_="comments"))
##   adder = int(tag.contents[0])
##   summer.append(adder)
##   fall = sum(summer)
####   print(adder)
##
##print(summer)
##print(fall)

######THIS IS ASSIGNMENT 1 URL: 'http://py4e-data.dr-chuck.net/comments_15167.html'
### EXTRA CODE EXAMPLE To run this, you can install BeautifulSoup
### https://pypi.python.org/pypi/beautifulsoup4
### Or download the file
### http://www.py4e.com/code3/bs4.zip
### and unzip it in the same directory as this file
##
##from urllib.request import urlopen
##from bs4 import BeautifulSoup
##import ssl
##import re
##
### Ignore SSL certificate errors
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = ('http://py4e-data.dr-chuck.net/comments_15167.html')
##html = urlopen(url, context=ctx).read()
####print(html)
##
### html.parser is the HTML parser included in the standard Python 3 library.
### information on other HTML parsers is here:
### http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
##soup = BeautifulSoup(html, "html.parser")
####print(soup)
##
### Retrieve all of the anchor tags
##summer = []
##tags = soup('span')
##for tag in tags:
####    Look at the parts of a tag
####   print('TAG:',tag)
####   print('URL:',tag.get('href', None))
####   print('Contents:',tag.contents[0])
####   print('Attrs:',tag.attrs)
####   print('Span:',tag.span)
####   print(soup.find("span", class_="comments"))
##   adder = int(tag.contents[0])
##   summer.append(adder)
##   fall = sum(summer)
####   print(adder)
##
####print(summer)
##print(fall)

##################################################################################

####THIS IS ASSIGNMENT 2 URL: 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
####url = input('Enter - ')
##url = ('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##bowl = []
##count = 0
##
##tags = soup('a')
##for tag in tags:
##   if count < 3:
##      print(tag.get('href', None))
##      bowl.clear()
##      bowl.append(tag)
##      count += 1
##
##print(bowl)
##
##spoon = str(bowl)
##cup = spoon.split('"')
####print(cup[1])
##newLink = cup[1]
##print(newLink)
##
##url2 = newLink
##html2 = urllib.request.urlopen(url2, context=ctx).read()
##soup2 = BeautifulSoup(html2, 'html.parser')
##bowl2 = []
##count2 = 0
##
##tags2 = soup2('a')
##for tag2 in tags2:
##   if count2 < 3:
##      print(tag2.get('href', None))
##      bowl2.clear()
##      bowl2.append(tag2)
##      count2 += 1
##
##print(bowl2)
##spoon2 = str(bowl2)
##cup2 = spoon2.split('"')
####print(cup[1])
##newLink2 = cup2[1]
##print(newLink2)
##
##url3 = newLink2
##html3 = urllib.request.urlopen(url3, context=ctx).read()
##soup3 = BeautifulSoup(html3, 'html.parser')
##bowl3 = []
##count3 = 0
##
##tags3 = soup3('a')
##for tag3 in tags3:
##   if count3 < 3:
##      print(tag3.get('href', None))
##      bowl3.clear()
##      bowl3.append(tag3)
##      count3 += 1
##
##print(bowl3)
##spoon3 = str(bowl3)
##cup3 = spoon3.split('"')
####print(cup[1])
##newLink3 = cup3[1]
##print(newLink3)
##
##url4 = newLink3
##html4 = urllib.request.urlopen(url4, context=ctx).read()
##soup4 = BeautifulSoup(html4, 'html.parser')
##bowl4 = []
##count4 = 0
##
##tags4 = soup4('a')
##for tag4 in tags4:
##   if count4 < 3:
##      print(tag4.get('href', None))
##      bowl4.clear()
##      bowl4.extend(tag4)
##      count4 += 1
##
##print(bowl4)
####spoon2 = str(bowl3)
####cup2 = spoon3.split('"')
######print(cup[1])
####newLink2 = cup3[1]
####print(newLink3)

#################################################################################
### THIS IS ASSIGNMENT 2 STRIPPED DOWN

##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = ('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##bowl = []
##bigCount = 0
##count = 0
##tags = soup('a')
##
##for tag in tags:
##   if count < 3:
####      print(tag2.get('href', None))
##      bowl.clear()
##      bowl.append(tag)
##      count += 1
##
##spoon = str(bowl)
##cup = spoon.split('"')
##newLink = cup[1]
##print(newLink)
##bigCount += 1
##
##while bigCount < 4:
##   url = newLink
##   html = urllib.request.urlopen(url, context=ctx).read()
##   soup = BeautifulSoup(html, 'html.parser')
##   bowl = []
##   count = 0
##   tags = soup('a')
##
##   for tag in tags:
##      if count < 3:
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

###################################################################################
##### THIS IS ASSIGNMENT 2 FOR REAL
##
##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = ('http://py4e-data.dr-chuck.net/known_by_Christian.html')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##bowl = []
##bigCount = 0
##count = 0
##tags = soup('a')
##
##for tag in tags:
##   if count < 18:
####      print(tag2.get('href', None))
##      bowl.clear()
##      bowl.append(tag)
##      count += 1
##
##spoon = str(bowl)
##cup = spoon.split('"')
##newLink = cup[1]
##print(newLink)
##bigCount += 1
##
##while bigCount < 7:
##   ctx = ssl.create_default_context()
##   ctx.check_hostname = False
##   ctx.verify_mode = ssl.CERT_NONE
##   url = newLink
##   html = urllib.request.urlopen(url, context=ctx).read()
##   soup = BeautifulSoup(html, 'html.parser')
##   bowl = []
##   count = 0
##   tags = soup('a')
##
##   while count < 18:
##      for tag in tags:
##         if count < 18:
####      print(tag2.get('href', None))
##            bowl.clear()
##            bowl.append(tag)
##            count += 1
##
##   spoon = str(bowl)
##   cup = spoon.split('"')
##   newLink = cup[1]
##   print(newLink)
##   bigCount += 1
##
##print('done')

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = ('http://py4e-data.dr-chuck.net/known_by_Christian.html')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
bowl = []
bigCount = 0
count = 0
tags = soup('a')

for tag in tags:
   if count < 18:
##      print(tag2.get('href', None))
      bowl.clear()
      bowl.append(tag)
      count += 1

spoon = str(bowl)
cup = spoon.split('"')
newLink = cup[1]
print(newLink)
bigCount += 1

while bigCount < 7:
   url = newLink
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   bowl = []
   count = 0
   tags = soup('a')

   for tag in tags:
      if count < 18:
##         print(tag2.get('href', None))
         bowl.clear()
         bowl.append(tag)
         count += 1

   spoon = str(bowl)
   cup = spoon.split('"')
   newLink = cup[1]
   print(newLink)
   bigCount += 1

print('done')
