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

##THIS is exercise 2 counting characters returned
import socket
bucket = list()
counter = 0


userURL = input('Please enter a URL: ')
splitURL = userURL.split('/')
domain = splitURL[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((domain, 80))

cmd = 'GET ' + userURL + ' HTTP/1.0\r\n\r\n'
cmd1 = cmd.encode()
mysock.send(cmd1)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
    bucket = data.decode()
    bucket = bucket.split()
    print(bucket)
##    if data not in bucket:
##        bucket.extend(data.decode())
##    print(bucket[0:300])

mysock.close()


