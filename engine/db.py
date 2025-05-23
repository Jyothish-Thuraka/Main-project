import csv
import sqlite3

conn=sqlite3.connect("Main.db")

cursor = conn.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS mails(id integer primary key, name VARCHAR(100), mail_id VARCHAR(1000))"
cursor.execute(query)

# query="INSERT INTO sys_command VALUES (null,'word','C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')"
# cursor.execute(query)
# conn.commit()

# query = "CREATE TABLE IF NOT EXISTS websites(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO websites VALUES (null,'Github', 'https://github.com/')"
# cursor.execute(query)
# conn.commit()

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# # Specify the column indices you want to import (0-based index)
# # Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 18]

# # # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# conn.commit()
# conn.close()

#single contact 
# query = "INSERT INTO contacts VALUES (null,'leo', '9963237421', 'null')"
# cursor.execute(query)
# conn.commit()


#search contact for testing
# query = 'leo'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])
