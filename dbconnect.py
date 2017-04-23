import sqlite3

DATABASE = 'database.db'

def insert(uname,pwd):
	con1 = sqlite3.connect(DATABASE)
	cur1 = con1.cursor()
	cur1.execute("INSERT INTO LOGIN values (?,?)", (uname,pwd))

def fetch():
	con2 = sqlite3.connect(DATABASE)
	cur2 = con2.cursor()	
	data=cur2.fetchall()
	return data


	
