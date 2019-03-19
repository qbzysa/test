# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 14:55
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request
import sql
import json
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route("/create", methods=['PUT'])
def create():
    data = request.data
    if data:
        body = {}
        data_list = data.split("&")
        for i in data_list:
            key = i.split("=")[0]
            value = i.split("=")[1]
            body[key] = value
    else:
        body = request.form.to_dict()
    req = sql.create_info(db, body)

    if req:
        return "sucessed!"
    else:
        return "failed!"


@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    req = sql.delete_info_by_id(db, id)
    if req:
        return "sucessed!"
    else:
        return "failed!"


@app.route("/update", methods=["POST"])
def update():
    data = request.data
    if data:
        body = {}
        data_list = data.split("&")
        for i in data_list:
            key = i.split("=")[0]
            value = i.split("=")[1]
            body[key] = value
    else:
        body = request.form.to_dict()
    req = sql.update_info_by_id(db, body)
    if req:
        return "sucessed!"
    else:
        return "failed!"


@app.route("/all")
def get():
    username = {}
    users = sql.get_all()
    if users:
        for user in users:
            key = user.id
            value = user.name
            username[key] = value
    return json.dumps(username)


@app.route("/<id>")
def get_info_by_id(id):
    username = {}
    user = sql.get_user_by_id(id)
    if user:
        username[user.id] = user.name
    return json.dumps(username)


if __name__ == "__main__":
    app.run()
