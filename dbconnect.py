import sqlite3

DATABASE = 'database.db'

def insert():
	con1 = sqlite3.connect(DATABASE)
	cur1 = con.cursor()
	cur1.execute("insert into LOGIN values (?,?)")

def fetch():
	con2 = sqlite3.connect(DATABASE)
	cur2 = con.cursor()	
	data=cur2.fetchall()
	return data


	
