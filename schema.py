import sqlite3
conn = sqlite3.connect('fantasy.db')
c = conn.cursor()

# Create table
c.execute("""
CREATE TABLE elements (
    id integer,
    team_code integer, 
    name text, 
    total_points integer, 
    form real
    )
""")
conn.commit()
conn.close()
