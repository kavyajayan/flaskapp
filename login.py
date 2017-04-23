import dbconnect
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
	flag=0;
	if request.method == 'POST':
		datas= dbconnect.fetch()
		for row in datas:
			if request.form['uname']==row[0]:
				flag=1	
			else:
				flag=0
		if flag==0:
			return redirect('/register')
		else:
			return "Same username"
				
	else:
			return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():	
	if request.method == 'POST':
		dbconnect.insert(request.form['uname'], request.form['pwd'])
		return redirect('/')
	else:
		return render_template('register.html')

if __name__== '__main__':
	app.run()

