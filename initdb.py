#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('data/data.db')

c = conn.cursor()

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

conn.commit()
conn.close()
