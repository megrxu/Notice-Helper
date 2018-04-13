#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('data/data.db')

c = conn.cursor()

# Create table
try:
    c.execute('''CREATE TABLE articles
             (title text, date text, feed text, link text)''')
except:
    pass
try:
    c.execute('''CREATE TABLE users
                 (id text, subs text)''')
except:
    pass

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
