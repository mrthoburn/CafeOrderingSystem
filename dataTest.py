import sqlite3 as s

conn = s.connect('UPS_Eats2.db')
c = conn.cursor()
c.execute('select * from customer')
print(c.fetchall())