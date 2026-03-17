from flask import Flask, request
app = Flask('FlskRESTfulAPIs')
@app.route('/', methods=['GET'])
def homePage():
    try:
        d = request.args.to_dict()
        if len(d) != 0:
            return  d
    except Exception as e:
        print("Error:", e)
    return "Hello World"
app.run(debug=True, host='0.0.0.0', port=1234)