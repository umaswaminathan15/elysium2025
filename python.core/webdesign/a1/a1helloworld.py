from flask import Flask
app = Flask("Hello World")
@app.route("/")
def homePage():
    return "<h1>Hello World!</h1>"
@app.route("/hot")
def hotDrink():
    return "<h2>Coffee Tea Milk!</h2>"
@app.route("/cool")
def coolDrink():
    return "<h2>Coke Pepsi 7Up!</h2>"
@app.route("/soft")
def softDrink():
    return "<h2>Orange Apple and Mango!</h2>"
app.run(debug=True)