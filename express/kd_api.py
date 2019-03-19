# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 14:55
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
import requests
import sql
import json
import urllib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# image_url = "https://cdn.kuaidi100.com/images/all/56/%s.png" % type
@app.route("/kd", methods=['GET'])
def index():
    kds = sql.get_all()
    return render_template('index.html', kds=kds)


@app.route("/query", methods=['GET', 'POST'])
def query():
    if request.method == 'GET':
        name = str(request.url).split('&')[0].split('=')[1]
        type = str(request.url).split('&')[1].split('=')[1]
        image = str(request.url).split('&')[2].split('=')[1]
        return render_template('query.html', name=name, type=type, image=urllib.unquote(image))
    else:
        type_name = request.form['type']
        name = request.form['name']
        image = request.form['image']
        postid = request.form['postid']
        reponse = requests.get("https://www.kuaidi100.com/query?type=%s&postid=%s" % (type_name, postid))
        result = json.loads(reponse.text)
        return render_template('result.html', name=name, type_name=type_name, postid=postid, image=image,
                               result=result['data'])


if __name__ == "__main__":
    app.run()
