##EXAMPLES
##t1 = ('a',)
##print(type(t1))

##t = tuple('lupins')
##print(t[3:5])

##txt = 'but soft what light in yonder window breaks'
##words = txt.split()
####print(words)
##t = list()
##for word in words:
##    t.append((len(word), word))
####print(t)
##t.sort(reverse=True)
##res = list()
##for length, word in t:
##    res.append(word)
##print(res)

##addr = 'monty@python.org'
##uname, domain = addr.split('@')
##print('user:', uname, '\ndomain:', domain)

##d = {'a':10, 'b':1, 'c':22}
##l = list()
##for key, val in d.items():
##    l.append( (val, key) )
##l.sort(reverse=True)
##print(l)

import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
lst  = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)
    
