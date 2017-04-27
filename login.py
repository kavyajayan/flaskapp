import dbconnect
from passlib.hash import pbkdf2_sha256
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
	flag=0
	flag2=0
	if request.method == 'POST':
		datas= dbconnect.fetch()
		for row in datas:
			if request.form['uname']==row[0]:
				flag=1
				if pbkdf2_sha256.verify(request.form['pwd'],row[1]):
					flag2=1
				else:
					flag2=0	
				break

			else:
				flag=0
		if flag==0:
			return redirect('/register')
		else:
			if flag2==0:
				return render_template('login.html', msg="Invalid password")
			else:
				return ("Successfully logged in!")		
	else:
			return render_template('login.html', msg="")

@app.route('/register', methods=['GET','POST'])
def register():	
	if request.method == 'POST':
		hash = pbkdf2_sha256.encrypt(request.form['pwd'], rounds=200000, salt_size=16)
		dbconnect.insert(request.form['uname'], hash)
		return redirect('/')
	else:
		return render_template('register.html')

if __name__== '__main__':
	app.run()

