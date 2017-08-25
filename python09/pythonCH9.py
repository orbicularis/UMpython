##fr2eng = dict()
##fr2eng['one'] = 'un'
##print(fr2eng['one'])
##vals = list(fr2eng.values())

##word = 'brontosaurus'
##d = dict()
##for letter in word:
##    if letter not in d:
##        d[letter] = 1
##    else:
##        d[letter] = d[letter] + 1
##
##print(d)

##counts = { 'chuck': 1, 'annie': 42, 'jan': 100}
##print(counts.get('annie', 0))

##word = 'brontosaurus'
##d = dict()
##for letter in word:
##    d[letter] = d.get(letter, 0) + 1
##print(d)


## EXERCISE 2 - this searches the text file for a from and pulls a word out

##mbox = open('mbox-short.txt')
##count = dict()
##
##for line in mbox:
##    newLine = line.find('From ')
##    if newLine is not 0:
##        continue
##    else:
####        print(line)
##        line = line.split()
##        newLine = line[2]
####        print(newLine)
##        
##        for days in newLine.split():
##            if days not in count:
##                count[days] = 1
##            else:
##                count[days] += 1
##
##print(count)

##EXERCISE 3 - thsi is a histogram of email addresses
##
##mbox = open('mbox-short.txt')
##count = dict()
##
##for line in mbox:
##    newLine = line.find('From ')
##    if newLine is not 0:
##        continue
##    else:
####        print(line)
##        line = line.split()
##        newLine = line[1]
####        print(newLine)
##        
##        for email in newLine.split():
##            if email not in count:
##                count[email] = 1
##            else:
##                count[email] += 1
##
##print(count)

##EXERCISE 4 - same as 3 except finds highest sender
##
##mbox = open('mbox-short.txt')
##count = dict()
##
##for line in mbox:
##    newLine = line.find('From ')
##    if newLine is not 0:
##        continue
##    else:
####        print(line)
##        line = line.split()
##        newLine = line[1]
####        print(newLine)
##        
##        for email in newLine.split():
##            if email not in count:
##                count[email] = 1
##            else:
##                count[email] += 1
##
##
##hiScore = 0
##key = None
##for score in count:
##    if count[score] > hiScore:
##        hiScore = count[score]
##        entry = score
##print(entry, hiScore)

##EXERCISE 5 - same as 3 except finds highest sender account

mbox = open('mbox-short.txt')
count = dict()

for line in mbox:
    newLine = line.find('From ')
    if newLine is not 0:
        continue
    else:
##        print(line)
        amper = line.find('@')
##        print(amper)
        endspot = line.find(' ',amper)
##        print(endspot)
        domain = line[amper+1:endspot]
##        print(domain)

        if domain not in count:
            count[domain] = 1
        else:
            count[domain] += 1
print(count)

##hiScore = 0
##key = None
##for score in count:
##    if count[score] > hiScore:
##        hiScore = count[score]
##        entry = score
##print(entry, hiScore)
