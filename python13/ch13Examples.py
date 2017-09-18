#### THIS IS EXAMPLE 1, PARSING XML, xml1.py
##import xml.etree.ElementTree as ET
##
##data = '''
##<person>
##    <name>Chuck</name>
##    <phone type="intl">
##    +1 734 303 4456
##    </phone>
##    <email hide="yes"/>
##</person>'''
##
##tree = ET.fromstring(data)
##print('Name', tree.find('name').text)
##print('Attr:', tree.find('email').get('hide'))

#### THIS IS EXAMPLE 2, xml2.py
##import xml.etree.ElementTree as ET
##
##input = '''
##<stuff>
##    <users>
##	<user x="2">
##            <id>001</id>
##            <name>Chuck</name>
##        </user>
##        <user x="7">
##            <id>009</id>
##            <name>Brent</name>
##        </user>
##    </users>
##</stuff>'''
##
##stuff = ET.fromstring(input)
##lst = stuff.findall('users/user')
##print('User count:', len(lst))
##
##for item in lst:
##    print('Name', item.find('name').text)
##    print('Id', item.find('id').text)
##    print('Attribute', item.get("x"))

## THIS IS EXAMPLE 3, json2.py
import json

data = '''
[
    { "id" : "001", "x" : "2", "name" : "Chuck"},
    { "id" : "009", "x" : "7", "name" : "Brent"}
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
    
