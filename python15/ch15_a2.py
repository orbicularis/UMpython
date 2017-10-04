#### THIS IS ASSIGNMENT 1 FOR CHAPTER 15 - AGE DATABASE

data = open('mbox-short.txt')
print(data)
    




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


#### THIS IS THE EXAMPLE CODE
##import sqlite3
##
##conn = sqlite3.connect('emaildb.sqlite')
##cur = conn.cursor()
##
##cur.execute('DROP TABLE IF EXISTS Counts')
##
##cur.execute('''
##CREATE TABLE Counts (email TEXT, count INTEGER)''')
##
##fname = input('Enter file name: ')
##if (len(fname) < 1): fname = 'mbox-short.txt'
##fh = open(fname)
##for line in fh:
##    if not line.startswith('From: '): continue
##    pieces = line.split()
##    email = pieces[1]
##    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
##    row = cur.fetchone()
##    if row is None:
##        cur.execute('''INSERT INTO Counts (email, count)
##                VALUES (?, 1)''', (email,))
##    else:
##        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
##                    (email,))
##    conn.commit()
##
### https://www.sqlite.org/lang_select.html
##sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
##
##for row in cur.execute(sqlstr):
##    print(str(row[0]), row[1])
##
##cur.close()
