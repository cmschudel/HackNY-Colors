from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/search', methods=['GET'])
def search():
	value = request.args.get('colors', '')
	return "val: %(v)s" % {'v': value}

if __name__ == '__main__':
	app.run()
