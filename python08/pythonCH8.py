
## exercise 1 the program called chop to slice up a list

##letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
##
##lettersWork = letters
##less1 = lettersWork.pop(0)
##less2 = lettersWork.pop()
##
##print(letters)
##print(less1)
##print(less2)

## EXERCISE 4 TO EXTRACT FILELS FROM SHAKESPEARE

##romeo = open('romeo.txt')
##romWords = []
##filterWords = []
##
##for line in romeo:
##    line = line.strip()
##    line = line.lower()
##    words = line.split()
##    words = romWords.extend(words)
##    romWords.sort()
##
##    for word in romWords:
##        if word in filterWords: continue
##        else:
##            word = filterWords.append(word)
##            filterWords.sort()
##    
##print(filterWords)


## EXERCISE TO EXTRACT EMAILS FROM A TEXT FILE

fhand = open('mbox-short.txt')
emails = []
counter = 0

for line in fhand:
    if not line.startswith('From '): continue
    emails = line.split()
    print(emails[1])
    counter += 1

print('This file contains', counter, 'lines that start with "From:"')
    
        
## EXERCISE 6 TO ENTER NUMBERS AND PRINT MIN AND MAX

##userNum = input('Enter an integer, or "done" when finished: ')
##numSet = []
##
##try:
##    int(userNum)
##    while True:
##        int(userNum)
##        print(userNum)
##        userNum = numSet.append(userNum)
##        print(numSet)
##        userNum = input('Enter an integer, or "done" when finished: ')
##        
##except:
##    print('Done')
##    try:
##        print(numSet)
##        print("Maximum:", float(max(numSet)))
##        print("Minimum:", float(min(numSet)))
##    except:
##        print()
