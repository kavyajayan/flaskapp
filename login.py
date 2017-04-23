import dbconnect
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def login():
	if request.method == 'POST':
		datas= dbconnect.fetch()
		for row in datas:
			if request.form.uname==row[0]:
				flag=1		
		if flag==0:
			redirect('/register')
				
	else:
			return render_template('login.html')

@app.route('/register')
def register():	
	return render_template('register.html')

if __name__== '__main__':
	app.run()

