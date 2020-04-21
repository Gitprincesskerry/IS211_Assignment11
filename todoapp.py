# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 11 Assignment

import re
from flask import Flask, render_template, request
app = Flask(__name__)

email_error = ""
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
def check(email):
    if(re.search(regex,email)):
        email_error = ""
        return email_error
    else:
        email_error = "Email error, Invalid Email"
        return email_error

tasklist = []

class Item:
    def __init__(self, name, email, priority):
        self.name = name
        self.email = email
        self.priority = priority

@app.route('/', methods = ['GET','POST'])
def kerry_start():
    return render_template('index.html')


@app.route('/submit', methods = ['GET','POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['Priority']


    valid_email = check(email)
    if valid_email=="":
        item = Item(task, email, priority)
        tasklist.append(item)

    return render_template('index.html',methods=['GET','POST'], tasklist=tasklist, email_error=valid_email)

@app.route('/clear', methods = ['GET','POST'])
def clear():
    tasklist = []
    return render_template('index.html', methods = ['GET','POST'], tasklist=tasklist)

if __name__ == "__main__":
    app.run()
