import sqlite3
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()
rows = c.execute('select * from elements order by form desc limit 10')
for row in rows:
    print('{:<30} {:>3}'.format(row[2][:30], row[4]))
