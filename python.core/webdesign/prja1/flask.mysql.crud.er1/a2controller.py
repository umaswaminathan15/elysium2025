import cr
from flask import Flask, render_template, redirect, flash, request, url_for
from flask_mysqldb import MySQL
from a1udf import *
app = Flask("flaskAppExamResult")
app.config['MySQL_HOST']="localhost"
app.config['MySQL_PORT']="3307"
app.config['MySQL_USER']="root"
app.config['MySQL_PASSWORD']=""
app.config['MySQL_DB']="dbsu"
app.config['MySQL_CURSORCLASS']="DictCursor"

MyS = MySQL(app)
@app.route("/")
def homePage():
    qry = "select * from tbler"
    cr = MyS.connection.cursor()
    cr.execute(qry)
    res = cr.fetchall()
    return render_template('a1select.html', rows = res)

@app.route("/newRowER", methods=["GET","POST"])
def erNewRow():
    if request.method == "POST":
        sname = request.form["tbxsname"]
        m1 = float(request.form["numm1"])
        m2 = float(request.form["numm2"])
        qry = " insert into tbler(sname,m1,m2) values(%s,%s,%s)"
        cr = MyS.connection.cursor()
        cr.execute(qry, (sname,m1,m2))
        MyS.connection.commit()
        cr.close()
        flash("New row inserted")
        return redirect("homePage")
    return render_template('a2insert.html')
@app.route("/editRowER", methods=["GET"])
def erEditRow(rno):
    if request.method == "POST":
        sname = request.form["tbxsname"]
        m1 = float(request.form["numm1"])
        m2 = float(request.form["numm2"])
        qry = "update tbler set sname=%s, m1=%s, m2=%s where rno=%s"
        cr.execute(qry, (sname,m1,m2,rno))
        MyS.connection.commit()
        cr.close()
        flash("New row updated")
        return redirect(url_for("homePage"))
    qry = "select * from tbler where rno = %s"
    cr.execute(qry, (rno,))
    res = cr.fetchall()
    cr.close()
    return render_template('a3update.html', row = res)
@app.route("/deleteRowER/<string:rno>", methods=["POST"])
def erDeleteRow(rno):
    cr = MyS.connection.cursor()
    qry = " delete from tbler where rno = %s"
    cr.execute(qry, (rno,))
    MyS.connection.commit()
    cr.close()
    flash("Row deleted")
    return redirect(url_for("homePage"))

app.secret_key = 'Flask.App.Exam.Result.9876543210'
app.run(debug=True)
