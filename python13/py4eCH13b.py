import urllib.request, urllib.parse, urllib.error
import json
counter = []

##data = '''[{ "id" : "001", "x" : "2", "name" : "Chuck"} ,{ "id" : "009", "x" : "7", "name" : "Chuck"}]'''

##address = input('Enter location: ')
address = ('http://py4e-data.dr-chuck.net/comments_42.json')
while True:
    if len(address) < 1:
        break
    print('Retrieving', address)
    url = urllib.request.urlopen(address)
    data = url.read().decode()
    print('Retrieved', len(data), 'characters')
    alpha = json.loads(data)
##print(alpha)
    print(json.dumps(alpha, indent=4))

##name = alpha['comments'][0]['name']
    count = alpha['comments'][0]['count']
    counter.append(count)
    print(count)
    print(counter)








####=====================================TEST CODE============================
##import urllib.request, urllib.parse, urllib.error
##import json
##
### Note that Google is increasingly requiring keys
### for this API
##serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
##
##while True:
##    address = input('Enter location: ')
##    if len(address) < 1: break
##
##    url = serviceurl + urllib.parse.urlencode(
##        {'address': address})
##
##    print('Retrieving', url)
##    uh = urllib.request.urlopen(url)
##    data = uh.read().decode()
##    print('Retrieved', len(data), 'characters')
##
##    try:
##        js = json.loads(data)
##    except:
##        js = None
##
##    if not js or 'status' not in js or js['status'] != 'OK':
##        print('==== Failure To Retrieve ====')
##        print(data)
##        continue
##
##    print(json.dumps(js, indent=4))
##
##    lat = js["results"][0]["geometry"]["location"]["lat"]
##    lng = js["results"][0]["geometry"]["location"]["lng"]
##    print('lat', lat, 'lng', lng)
##    location = js['results'][0]['formatted_address']
##    print(location)
