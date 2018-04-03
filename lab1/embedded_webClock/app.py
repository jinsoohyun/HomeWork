#-*- coding:utf-8 -*-
import requests, os, hashlib

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import time
import datetime

app = Flask(__name__)
CORS(app)

#session_list = {};
#rand_id = lambda : hashlib.md5(os.urandom(24)).hexdigest()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route('/release', methods=["POST", "GET"])
def status():

    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

    return jsonify(s.split(' ')[0],s.split(' ')[1])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, threaded=True, debug=True)
