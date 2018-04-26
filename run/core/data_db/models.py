import sqlite3 as sql

def insertUser(username):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username) VALUES (?)", (username))
    con.commit()
    con.close()

def retrieveUsers():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username FROM users")
	users = cur.fetchall()
	con.close()
	return users