##fhand = open('mbox.txt')
##print(fhand)

##stuff = 'Hello\nWorld'
##print(stuff)

##fhand = open('mbox.txt')
##count = 0
##for line in fhand:
##    count = count +1
##print('Line Count:', count)

##fhand = open('mbox.txt')
##inp = fhand.read()
##print(len(inp))
##print(inp[:20])

##fhand = open('mbox.txt')
##count = 0
##for lines in fhand:
##    count = count + 1
##print('Number of lines: ', count)

#fhand = open('mbox.txt')
#count = 0
#while count < 10:
#for line in fhand:
#    line = line.rstrip()
#    if line.find('Tue Oct 30') == -1: continue
#        count = count + 1
#    print(line)
            

##fname = input('Enter the file name: ')
##fhand = open(fname)
##count = 0
##for line in fhand:
##    if line.startswith('Subject'):
##        count = count + 1
##print('There were ', count, ' lines containing the word "Subject" in ', fname)

##fout = open('OutputCH7.txt', 'w')
##print('fout')
###<_io.TextIOWrapper name='output.txt' mode='w' encoding='cp1252'>
##
##line1 = "This is the first line of text, \n"
##fout.write(line1)
##
##line2 = "This is thesecond line of text, \n"
##fout.write(line2)
##
##fout.close()

##THIS IS EXERCISE 1
##fname = input('Please enter a filename: ')
##fhand = open(fname)
##for line in fhand:
##    if line.startswith('This'):
##        print(line.upper())

fname = input('Please enter a filename: ')
fhand = open(fname)
count = 0
NumLines = 0
NumSum = set()
TotalSum = 0
for line in fhand:
    if line.find('X-DSPAM-Confidence') == -1: continue
    count = float(line[20:26])
    NumLines = NumLines + 1
    NumSum.add(count)
    TotalSum = sum(NumSum)

TotalMean = float(TotalSum / NumLines)
print(TotalSum, NumLines)
print(TotalMean)










