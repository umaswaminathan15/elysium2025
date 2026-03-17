from flask import Flask,jsonify,request
app = Flask('Flask1RESTfulAPIs')
@app.route("/", methods=['GET'])
def homePage():
    return jsonify({'msg': 'Hello World'})
app.run(debug=True)
