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

##import string
##fhand = open('romeo-full.txt')
##counts = dict()
##for line in fhand:
##    line = line.translate(str.maketrans('', '', string.punctuation))
##    line = line.lower()
##    words = line.split()
##    for word in words:
##        if word not in counts:
##            counts[word] = 1
##        else:
##            counts[word] += 1
##lst  = list()
##for key, val in list(counts.items()):
##    lst.append((val, key))
##
##lst.sort(reverse=True)
##
##for key, val in lst[:10]:
##    print(key, val)
    
####EXERCISE 1 - ADDRESSES PULLED FROM FILE
####import string
##mbox = open('mbox-short.txt')
##counts = dict()
##winner = list()
##
##for line in mbox:
##    newLine = line.find('From ')
##    if newLine is not 0:
##        continue
##    else:
####        print(line)
##        amper = line.find('@')
##        endSpace = line.find(' ', amper)
##        domains = line[amper+1 : endSpace]
####        print(domain)
##
##        if domains not in counts:
##            counts[domains] = 1
##        else:
##            counts[domains] += 1
##
##for x, y in counts.items():
##    winner.append((y, x))
##    
##print(max(winner))

##EXERCISE 1 - ADDRESSES PULLED FROM FILE
##import string
mbox = open('mbox-short.txt')
counts = dict()
winner = list()

for line in mbox:
    newLine = line.find('From ')
    if newLine is not 0:
        continue
    else:
##        print(line)
        amper = line.find('@')
        endSpace = line.find(' ', amper)
        domains = line[amper+1 : endSpace]
##        print(domain)

        if domains not in counts:
            counts[domains] = 1
        else:
            counts[domains] += 1

for x, y in counts.items():
    winner.append((y, x))
    
print(max(winner))


















