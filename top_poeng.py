import sqlite3
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()
c2 = conn.cursor()
rows = c.execute('select * from elements order by total_points desc limit 10')
for row in rows:
    t = [row[1]]
    c2.execute('SELECT * FROM teams WHERE id=?', t)
    print('{:<15}{:<30} {:>3}'.format(c2.fetchone()[1], row[2][:30], row[3]))
