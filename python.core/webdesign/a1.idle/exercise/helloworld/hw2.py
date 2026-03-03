from flask import Flask, render_template
app = Flask("Hello World")
@app.route('/', methods=['GET', 'POST'])
def homePage():
    return render_template("hi.html", author="cmr2su")
app.run(debug=True, host="127.0.0.1", port=1234)