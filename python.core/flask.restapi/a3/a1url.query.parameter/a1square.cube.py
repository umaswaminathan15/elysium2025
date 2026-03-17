from flask import Flask, jsonify, request
app = Flask('FlaskRESTfulAPIs')
@app.route("/", methods=['GET'])
def homePage():
    return "Hello World"
@app.route("/author/<string:aname>", methods=['GET'])
def usum(aname):
    return jsonify({'author': aname})
@app.route("/square/<int:x>", methods=['GET'])
def usquare(x):
    d = {'x' : x, 'square': x**2}
    return jsonify(d)
@app.route("/cube/<int:x>", methods=['GET'])
def ucube(x):
    d = {'x' : x, 'cube': x**3}
    return jsonify(d)
app.run(debug=True)