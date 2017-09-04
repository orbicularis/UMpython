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
##theWord = list()
##count = 0
##
##fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
##for line in fhand:
##    words = line.decode().split()
##    for word in words:
##        theWord.extend(word)
##        count += 1
##        
##print(theWord[0:5])
##print(count)

##THIS is exercise 4
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
chars = list()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

##url = input('Enter - ')
url = ('http://www.dr-chuck.com/page1.htm')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

##print(soup)
print(html)

for letters in html:
##    html.split()
    chars.append(letters)
    

print(chars)


##tags = soup('a')
##for tag in tags:
##    print(tag.get('href', None))



    
