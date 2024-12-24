import sqlite3

conn=sqlite3.connect("Main.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null,'word','C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS websites(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO websites VALUES (null,'Github', 'https://github.com/')"
# cursor.execute(query)
# conn.commit()


