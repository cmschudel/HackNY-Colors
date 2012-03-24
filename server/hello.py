import sys, string, json
from flask import Flask
from flask import request
from functools import wraps
from flask import redirect, current_app
app = Flask(__name__)

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs).data) + ')'
            return current_app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/search', methods=['GET'])
@support_jsonp
def search():
	raw = request.args.get('colors', '')
	colors = string.split(raw, ',')
	printable = ', '.join(colors)
	return printable

if __name__ == '__main__':
	app.run()
