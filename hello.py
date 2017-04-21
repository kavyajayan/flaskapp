from flask import Flask
app = Flask(__name__)

@app.route('/')
def helo_world():
	return 'Hello world!'
