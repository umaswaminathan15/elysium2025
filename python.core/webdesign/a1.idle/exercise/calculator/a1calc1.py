from flask import Flask, render_template
app = Flask("Calculator")
@app.route('/', methods=['GET', 'POST'])
def calcuWebPage():
    return render_template("a1calc1.html", author="cmr2su")
app.run(debug=True)