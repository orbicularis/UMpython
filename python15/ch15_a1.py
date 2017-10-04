## THIS IS ASSIGNMENT 1 FOR CHAPTER 15 - AGE DATABASE

import sqlite3

conn = sqlite3.connect('CH15py4e.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Ages')
cur.execute('CREATE TABLE Ages (name VARCHAR(128), age INTEGER)')

cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Kaitlynn', 17))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Sajid', 37))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Elysa', 20))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Kay', 18))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Haiden', 18))
cur.execute('INSERT INTO Ages (name, age) VALUES (?, ?)',
    ('Colby', 22))

#### ALTERNATE SHORTER WAY OF WRITING IT:
##cur.execute('DELETE FROM Ages');
##cur.execute("INSERT INTO Ages (name, age) VALUES ('Kaitlynn', 17)");
##cur.execute("INSERT INTO Ages (name, age) VALUES ('Sajid', 37)");
##cur.execute("INSERT INTO Ages (name, age) VALUES ('Elysa', 20)");
##cur.execute("INSERT INTO Ages (name, age) VALUES ('Kay', 18)");
##cur.execute("INSERT INTO Ages (name, age) VALUES ('Haiden', 18)");
##cur.execute("INSERT INTO Ages (name, age) VALUES ('Colby', 22)");
conn.commit()

print('Hex Dump:')
cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
    print(row)




print()

conn.close()



