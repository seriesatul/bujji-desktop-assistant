import sqlite3

connection = sqlite3.connect("bujji.db")

cursor = connection.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_commands (id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_commands VALUES (null,'blender', 'C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender-launcher.exe')"
# cursor.execute(query)
# connection.commit()

query = "CREATE TABLE IF NOT EXISTS web_commands (id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_commands VALUES (null,'chatgpt', 'https://chatgpt.com/')"
cursor.execute(query)
connection.commit()