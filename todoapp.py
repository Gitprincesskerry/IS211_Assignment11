# !/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 11 Assignment

import re
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

EMAIL_REGEX = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"


def is_valid_email(email):
    """
    Check if the email is correct

    :param email:
    :return:
    """
    if re.search(EMAIL_REGEX, email):
        return True
    else:
        return False


tasklist = []

class Item:
    def __init__(self, name, email, priority):
        self.name = name
        self.email = email
        self.priority = priority


@app.route('/', methods=['GET','POST'])
def kerry_start():
    return render_template('index.html')


@app.route('/submit', methods = ['GET','POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['Priority']

    if is_valid_email(email):
        item = Item(task, email, priority)
        tasklist.append(item)
        email_error = ""
    else:
        email_error = "There was an email error"

    return render_template('index.html', methods=['GET', 'POST'], tasklist=tasklist, email_error=email_error)


@app.route('/clear', methods=['GET', 'POST'])
def clear():
    global tasklist

    tasklist.clear()
    return redirect(url_for('kerry_start'))


if __name__ == "__main__":
    app.run()
