#-*- coding:utf-8 -*-
import requests, os, hashlib

from flask import Flask, jsonify, render_template, request,abort
from flask import redirect, url_for, g
from flask_cors import CORS, cross_origin
import sqlite3
import time
import datetime
import sys

from flask import _app_ctx_stack

DATABASE = 'database.db'

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__)
CORS(app)

#session_list = {};
#rand_id = lambda : hashlib.md5(os.urandom(24)).hexdigest()

def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(DATABASE)
    return top.sqlite_db

@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()

def make_dicts(cursor, row):
    return dict((cur.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/", methods=["GET", "POST"])
def index():
    result = query_db('Select * from management;')
    return render_template("index.html", results = result)


@app.route('/release', methods=["POST"])
def release():
    if request.method == 'POST':
      name = request.form['Name-input']
      number = request.form['phone-input']

      get_db().execute(
        'insert into management (name, phone) values (?,?);',
            (
                name, number
            )
        )
      get_db().commit()
      return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, threaded=True, debug=True)
