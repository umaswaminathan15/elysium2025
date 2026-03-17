from flask import Flask, request
app = Flask('FlaskRESTfulAPIs')
@app.route("/", methods=['GET'])
def homePage():
    try:
        L = request.args.getlist('drinks')
        if len(L) != 0:
            return  f"List:{L}"
        else:
            d = request.args.to_dict(flat=False)
            if len(d) != 0:
                return f"Dictionary:{d}"
    except Exception as e:
        print("Error:", e)
    return "Hello World"
app.run(debug=True, host='0.0.0.0', port=1234)