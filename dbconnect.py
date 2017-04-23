import sqlite3
DATABASE = 'database.db'

def insert(uname,pwd):
	con1 = sqlite3.connect(DATABASE)
	cur1 = con1.cursor()
	cur1.execute("INSERT INTO LOGIN (username,password) values (?,?)", (uname,pwd))
	con1.commit()
	con1.close()

def fetch():
	con2 = sqlite3.connect(DATABASE)
	cur2 = con2.cursor()
	cur2.execute("SELECT username, password from LOGIN")	
	data=cur2.fetchall()
	con2.close()
	return data

def removerows():
	con3 = sqlite3.connect(DATABASE)
	cur3 = con3.cursor()
	cur3.execute("Delete from LOGIN")
	con3.commit()
	con3.close()



	
