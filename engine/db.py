import sqlite3
import csv 

connection = sqlite3.connect("bujji.db")

cursor = connection.cursor()

# query = "CREATE TABLE IF NOT EXISTS sys_commands (id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO sys_commands VALUES (null,'blender', 'C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender-launcher.exe')"
# cursor.execute(query)
# connection.commit()

# query = "CREATE TABLE IF NOT EXISTS web_commands (id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_commands VALUES (null,'chatgpt', 'https://chatgpt.com/')"
# cursor.execute(query)
# connection.commit()

# cursor.execute("CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255) NULL)")

# desied_column_indices = [0,18]

# with open("contacts.csv", "r",encoding="utf-8") as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         selected_data =  [row[i] for i in desied_column_indices]
#         cursor.execute("INSERT INTO contacts(id,'name','mobile_no') VALUES (null, ?, ?)", tuple(selected_data))

# connection.commit()
# connection.close()     


query = "Asmit Singh"
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? or LOWER(name) LIKE ?", ('%' + query + '%',query + '%'))
results = cursor.fetchall()
print(results[0][0])



