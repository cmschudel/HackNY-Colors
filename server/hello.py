import sys, string
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/search', methods=['GET'])
def search():
	raw = request.args.get('colors', '')
	colors = string.split(raw, ',')
	printable = ', '.join(colors)
	return printable

if __name__ == '__main__':
	app.run()
