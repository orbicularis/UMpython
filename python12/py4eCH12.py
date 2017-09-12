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
    
####THIS IS ASSIGNMENT 1 URL: 'http://py4e-data.dr-chuck.net/comments_42.html'
##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
####ctx = ssl.create_default_context()
####ctx.check_hostname = False
####ctx.verify_mode = ssl.CERT_NONE
##
##
####url = input('Enter - ')
##url = ('http://py4e-data.dr-chuck.net/comments_42.html')
##print(url)
##
##html = urllib.request(url)
##
####.urlopen(url).read()
##print(html)
##
####soup = BeautifulSoup(html, 'html.parser')
##
####words = str(soup)
####letters = list(words)
####print(letters[0:20])
####
####count = 0
####
####for letter in letters:
####    count += 1
####
####print(count)

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()


# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")
print(soup)


### Retrieve all of the anchor tags
##tags = soup('t')
##print(tags)

##for tag in tags:
##    # Look at the parts of a tag
##    print('TAG:', tag)
##    print('URL:', tag.get('href', None))
##    print('Contents:', tag.contents[0])
##    print('Attrs:', tag.attrs)

    
