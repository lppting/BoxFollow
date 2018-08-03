#coding:utf-8

from flask import jsonify
from flask import render_template
from app import app
import requests,json

url = "https://box.maoyan.com/promovie/api/box/second.json"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_json",methods=["GET","POST"])
def get_json():
    r = requests.get(url)
    data = json.loads(r.content)
#    data = json.dumps(dict_json)
    info = data["data"]["list"][0]
    m = "dad"
    return json.dumps(info)
