# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, render_template, redirect, url_for, request
import Utils
import SqlLite
import mail

app = Flask(__name__, static_folder='templates\static')


@app.route("/")
def home_page():
    sl = SqlLite.Sqllite3()
    sl.__check__table__existence__()
    return render_template("main.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/studentblog", methods=["GET","POST"])
def studentblog():
    d = request.form
    username = d.get("username")
    password = d.get("password")
    email = d.get("email")
    dob = d.get("dob")
    Utils.log(f"{d}")
    userid = d.get("username")
    sl = SqlLite.Sqllite3()
    valid = sl.__valid__credentials__(username, password)
    if not valid:
        return render_template("login.html", error="Invalid Credentials. Retry or do signup.")
    else:
        return render_template("index.html", username=username, email=email, dob=dob, userid=userid)

@app.route("/social")
def social_media():
    return render_template("workinprogress.html")

@app.route("/login", methods=["GET","POST"])
def login():
    return render_template("login.html")

@app.route("/studentsignup", methods=["GET","POST"])
def studentsignup():
    form = request.form
    username = form.get("username")
    password = form.get("password")
    firstname = form.get("firstname")
    lastname = form.get("lastname")
    mailid = form.get("email")
    dob = form.get("dob")
    sl = SqlLite.Sqllite3()
    available = sl.__is_username__available__(username)
    if available:
        sl.__insert__user__credentials__(username, password)
        sl.__insert__students__marks__()
        sl.__insert__attedence__()
        sl.__insert__userinfo__(form)
        mail.sendmail(firstname, lastname, username, mailid)
        return render_template("index.html", username=username,name=f"{firstname} {lastname}", email=mailid, dob=dob)
    else:
        return render_template("signup.html", firstname=form.get("username"), lastname=form.get("lastname"), email=form.get("email"), dob=form.get("dob"),error="User Id Not available. Try with different User Id")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/userdetails", methods=["Get"])
def user_info():
    pass

if __name__ == "__main__":
    app.run()