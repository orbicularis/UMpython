####THIS program asks the user for an input, searches for it, and counts the
####number of occurances
##
##import re
##
##askMe = input('Please enter a search term:')
##mbox = open('mbox-short.txt')
##counts = dict()
##
##for line in mbox:
##    line = line.strip()
##    hits = re.findall(askMe, line)
##    if len(hits) > 0:
##        theWord = str(hits)
####        print(theWord)
##
##        if theWord not in counts:
##            counts[theWord] = 1
##        else:   
##            counts[theWord] += 1
##            
####print(counts)
##
##for term, tally in counts.items():
##    termfix = str(term).replace("[", "").replace("]", "")
####    print(termfix)
##    print('mbox-shot.txt had', tally ,'instances that matched the term', termfix)
##

####THIS looks for a special line format and does some math
##
##import re
##mbox = open('mbox-short.txt')
##counts = list()
##looper = 0
##
##for line in mbox:
##    line = line.strip()
##    hits = re.findall('^New Revision: ([0-9.]+)', line)
##    if len(hits) > 0:
##        looper += 1
##        theWord = str(hits).replace("['", "").replace("']", "")
####        print(theWord)
##
##        if theWord not in counts:
##            counts.append(float(theWord))
##            
####print(looper)
##score = ((sum(i for i in counts)) / looper)           
##print(score)
##

####THIS searches through text and pulls out numbers and sums them
####(There are 90 values with a sum=445833)
##
##import re
##counts = list()
##
##sampData = open('regex_sum_15165.txt')
##
##for line in sampData:
##    lst = line.strip()
##    lst = re.findall('[0-9]+', line)
##    if len(lst) > 0:
####        print(lst)
##        counts.extend(lst)
##
##numbers = list(map(int, counts))
##
##print(sum(numbers))








