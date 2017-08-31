####THIS retrieves some text from a URL
##import socket
##
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect(('data.pr4e.org', 80))
##cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
##mysock.send(cmd)
##
##while True:
##    data = mysock.recv(512)
##    if (len(data) < 1):
##        break
##    print(data.decode())
##
##mysock.close()

####THIS retrieves a jpeg image from a URL
##
##import socket
##import time
##
##HOST = 'data.pr4e.org'
##PORT = 80
##mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##mysock.connect((HOST, PORT))
##mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
##count = 0
##picture = b""
##
##while True:
##    data = mysock.recv(5120)
##    if (len(data) < 1): break
##    time.sleep(0.25)
##    count = count + len(data)
##    print(len(data), count)
##    picture = picture + data
##
##mysock.close()
##
##pos = picture.find(b"\r\n\r\n")
##print('Header length', pos)
##print(picture[:pos].decode())
##
##picture = picture[pos+4:]
##fhand = open("stuff.jpg", "wb")
##fhand.write(picture)
##fhand.close()

##THIS is a urllib example
import urllib.request, urllib.parse, urllib.error
counts = dict()
theWords = list()

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) +1
    print(line.decode().strip())
print(counts)


####THIS parses html
##import urllib.request, urllib.parse, urllib.error
##import re
##
##url = input('Enter - ')
##html = urllib.request.urlopen(url).read()
##links = re.findall(b'href="(http://.*?)"', html)
##for link in links:
##    print(link.decode())

####THIS is beautiful soup
##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = input('Enter - ')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##
##tags = soup('a')
##for tag in tags:
##    print(tag.get('href', None))

####THIS is beautiful soup pulling tags
##import urllib.request, urllib.parse, urllib.error
##from bs4 import BeautifulSoup
##import ssl
##
##ctx = ssl.create_default_context()
##ctx.check_hostname = False
##ctx.verify_mode = ssl.CERT_NONE
##
##url = input('Enter - ')
##html = urllib.request.urlopen(url, context=ctx).read()
##soup = BeautifulSoup(html, 'html.parser')
##
##tags = soup('a')
##for tag in tags:
##    print('TAG:', tag)
##    print('URL:', tag.get('href', None))
##    print('Contents:', tag.contents[0])
##    print('Attrs:', tag.attrs)
    
####THIS saves binary files to disk in one shot (MUST BE SMALLER THAN MEM)
##import urllib.request, urllib.parse, urllib.error
##
##img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
##fhand = open('cover3.jpg', 'wb')
##fhand.write(img)
##fhand.close()

####THIS saves binary files to disk in blocks (NO MEM ISSUE)
##import urllib.request, urllib.parse, urllib.error
##
##img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
##fhand = open('cover3.jpg', 'wb')
##size =  0
##while True:
##    info = img.read(100000)
##    if len(info) < 1: break
##    size = size + len(info)
##    fhand.write(info)
##
##print(size, 'characters copied.')
##fhand.close()
