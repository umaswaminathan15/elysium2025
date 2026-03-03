from flask import Flask
app = Flask("HelloWorld")
@app.route("/")
def homePage():
    return "<h1>Hello World!</h1>"
app.run(debug=True)