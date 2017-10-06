
###### THIS IS ASSIGNMENT 1 FOR CHAPTER 15 - AGE DATABASE
##
####import re
##import string
##import sqlite3
##
##conn = sqlite3.connect('CH15py4eA2.sqlite')
##cur = conn.cursor()
##
##cur.execute('DROP TABLE IF EXISTS Counts')
##cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
##cur.execute('DELETE FROM Counts');
##
##data = open('mbox.txt')
##counts = dict()
##
##for line in data:
##    line = line.strip()
##    newline = line.find('From')
##    if newline is not 0:
##        continue
##    else:
##        amper = line.find('@')
##        endSpace = line.find(' ', amper)
##        domains = line[amper+1 : endSpace]
####        print(domains)
##
##        if domains not in counts:
##            counts[domains] = 1
##        else:
##            counts[domains] += 1
##
##for organ, num in counts.items():
##    print(organ, num)
##    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)',
##        (organ, num))
##
##conn.commit()


##    domains = line[amper+1 : endSpace]
##    print(domains)

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
##import sqlite3
##
##conn = sqlite3.connect('CH15py4eA2.sqlite')
##cur = conn.cursor()
##
##cur.execute('DROP TABLE IF EXISTS Counts')
##cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
##
###### LONGER WAY OF WRITING IT:
####cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
####    ('Kaitlynn', 17))
##
###### SHORTER WAY OF WRITING IT:
##cur.execute('DELETE FROM Counts');
##cur.execute("INSERT INTO Counts (org, count) VALUES ('GE', 44)");
##
##conn.commit()
##
##print('Hex Dump:')
##cur.execute('SELECT hex(org || count) AS X FROM Counts ORDER BY X')
##for row in cur:
##    print(row)
##
##conn.close()
##
##
##


## THIS IS THE EXAMPLE CODE
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    line = line.strip()
    if not line.startswith('From: '): continue
    pieces = line.split('@')
    email = pieces[1]
    print(email)

    
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
