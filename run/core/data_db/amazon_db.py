import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE users(
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                username     VARCHAR,
                created_on   TIMESTAMP DEFAULT CURRENT_TIMESTAMP);''')

connection.commit()
cursor.close()
connection.close()           