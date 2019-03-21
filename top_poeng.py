import sqlite3
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()
c2 = conn.cursor()

sql = """
select t.name, e.name, e.total_points 
from elements e 
    join teams t on t.id = e.team_id
where
    element_type = ?
order by total_points desc 
limit 10
"""

posisjoner = {1 : 'Keeper', 2: 'Forsvar', 3: 'Midtbane', 4: 'Spiss'}

for p in posisjoner:
    rows = c.execute(sql, [p])
    print(posisjoner[p], '********************************************')
    for row in rows:
        print('{:<15}{:<30} {:>3}'.format(row[0], row[1][:30], row[2]))
    print()
