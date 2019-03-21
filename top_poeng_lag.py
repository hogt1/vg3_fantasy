import sqlite3
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()
c2 = conn.cursor()

sql = """
select t.name, e.name, e.total_points, e.element_type 
from elements e 
    join teams t on t.id = e.team_id
where
    team_id = ?
order by total_points desc 
limit 3
"""

teams = c2.execute('select * from teams')
for team in teams:
    rows = c.execute(sql, [team[0]])
    print(team[1], '********************************************')
    for row in rows:
        print('{:<30} ({}) {:>3}'.format(row[1][:30], row[3], row[2]))
    print()
