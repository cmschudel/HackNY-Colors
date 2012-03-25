import sys, string, json
import numpy, Pycluster
from flask import Flask
from functools import wraps
from flask import request, redirect, current_app, jsonify
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

def cluster_colors(points):
    num_clusters = min(len(points), 3)

    labels, error, nfound = Pycluster.kcluster(points, num_clusters)

    totals = []
    for i in range(num_clusters):
        totals.append( [[0, 0, 0], 0] )

    for i in range(len(labels)):
        tmp = totals[labels[i]]
        tmp[0][0] += points[i][0]
        tmp[0][1] += points[i][1]
        tmp[0][2] += points[i][2]
        tmp[1] += 1

    averages = [ [ 1.0 * a[0]/n, 1.0 * a[1]/n, 1.0 * a[2]/n] for a,n in totals]

    return averages

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/search', methods=['GET'])
@support_jsonp
def search():
    raw = request.args.get('colors', '')
    colors = string.split(raw, ';')
    colors_split = [ string.split(color, ',') for color in colors ]
    color_points = [[float(color[0]), float(color[1]), float(color[2])]
            for color in colors_split if len(color) == 3]

    return jsonify({"colors": cluster_colors(color_points)})

if __name__ == '__main__':
    app.run(debug = True)
