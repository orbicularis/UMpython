##import re
##hand = open('mbox-short.txt')
##for line in hand:
##    line = line.strip()
##    if re.search('^From:.+@', line):
##        print(line)

###this one uses \S to mean non-whitespace + @ + \S
##import re
##s = 'A message from csev@umich.edu to cwen@iupi.edu about meeting @2pm'
##lst = re.findall('\S+@\S+', s)
##print(lst)

###taken a step further, this finds @ appearing with blocks of letters
##import re
##s = open('mbox-short.txt')
##for line in s:
##         line = line.strip()
##         lst = re.findall('\S+@\S+', line)
##         if len(lst) > 0:
##             print(lst)

####still further, this finds @ appearing with blocks of letters, excluding punct
##import re
##s = open('mbox-short.txt')
##for line in s:
##         line = line.strip()
##         lst = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
##         if len(lst) > 0:
##             print(lst)
         
####search and extract, check out line 37 - the parentheses limit
####the extraction to that number alone
##import re
##s = open('mbox-short.txt')
##for line in s:
##         line = line.strip()
##         lst = re.findall('^X\S*: ([0-9.]+)', line)
##         if len(lst) > 0:
##             print(lst)

##here's the email search to find the hour of the sent email
import re
s = open('mbox-short.txt')
for line in s:
         line = line.strip()
         lst = re.findall('^From .* ([0-9][0-9])', line)
         if len(lst) > 0:
             print(lst)
