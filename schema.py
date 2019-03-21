import sqlite3
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE elements (
    id integer primary key,
    team_code integer, 
    name text, 
    total_points integer, 
    form real
    )
""")

c.execute("""
CREATE TABLE teams (
    id integer primary key,
    name text 
    )
""")


conn.commit()
conn.close()
