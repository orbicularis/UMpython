##import urllib.request, urllib.parse, urllib.error
##import json
##counter = 0
##addbox = []
##
####data = '''[{ "id" : "001", "x" : "2", "name" : "Chuck"} ,{ "id" : "009", "x" : "7", "name" : "Chuck"}]'''
##
####address = input('Enter location: ')
##address = ('http://py4e-data.dr-chuck.net/comments_42.json')
##while True:
##    if counter == 1:
##        break
##    if len(address) < 1:
##        break
##    print('Retrieving', address)
##    url = urllib.request.urlopen(address)
##    data = url.read().decode()
##    print('Retrieved', len(data), 'characters')
##    alpha = json.loads(data)
####print(alpha)
##    print(json.dumps(alpha, indent=4))
##
##    for add in alpha['comments']:
##        print(add['name'])
##        print(add['count'])
##        addbox.append(add['count'])
##    print(addbox)
##    tally = sum(int(x) for x in addbox)
##    print(tally)
##
##        
##
####name = alpha['comments'][0]['name']
####    add = alpha['comments'][0]['count']
####    addbox.append(add)
####    print(add)
####    print(addbox)
##    counter += 1

## ====================HERE IS THE CLEANED UP FINAL==================

import urllib.request, urllib.parse, urllib.error
import json
counter = 0
addbox = []

##address = input('Enter location: ')
address = ('http://py4e-data.dr-chuck.net/comments_15170.json')
while True:
    if counter == 1:
        break
    if len(address) < 1:
        break
##    print('Retrieving', address)
    url = urllib.request.urlopen(address)
    data = url.read().decode()
##    print('Retrieved', len(data), 'characters')
    alpha = json.loads(data)
##    print(alpha)
##    print(json.dumps(alpha, indent=4))

    for add in alpha['comments']:
##        print(add['name'])
##        print(add['count'])
        addbox.append(add['count'])
##    print(addbox)
    tally = sum(int(x) for x in addbox)
    print(tally)
    counter += 1
