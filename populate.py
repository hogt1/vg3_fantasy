import sqlite3
import requests
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()

# Henter data
r = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')
data = r.json()

#    id integer,
#    team_code integer, 
#    name text, 
#    total_points integer, 
#    form real

for e in data['elements']:
    r = (e['id'], e['team'], e['first_name'] + ' ' + e['second_name'], e['total_points'], e['form'] )
    c.execute("insert into elements values (?, ?, ?, ?, ?)", r)


for t in data['teams']:
    r = (t['id'], t['name'])
    c.execute("insert into teams values (?, ?)", r)


conn.commit()
conn.close()