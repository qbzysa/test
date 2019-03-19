# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/24 13:43
from model import User


def create_info(db, body):
    try:
        id = body.get('id')
        name = body.get('name')
        age = body.get('age')
        user = User(id=id, name=name, age=age)
        db.session.add(user)
        db.session.commit()
        return True
    except Exception, e:
        print e
        return False


def get_user_by_id(id):
    user = User.query.filter_by(id=id).first()
    return user


def get_all():
    return User.query.all()


def update_info_by_id(db, body):
    id = body.get("id")
    if get_user_by_id(id):
        try:
            db.session.query(User).filter_by(id=id).update({'name': body.get("name")})
            db.session.commit()
            return True
        except Exception, e:
            print e
            print "数据更新失败！"
            return False
    else:
        print "用户ID不存在，更新数据失败！"
        return False


def delete_info_by_id(db, id):
    user = get_user_by_id(id)
    if user:
        try:
            db.session.query(User).filter_by(id=id).delete()
            db.session.commit()
            return True
        except Exception, e:
            print e
            print "数据删除失败！",
            return False
    else:
        print "用户ID不存在，删除数据失败！"
        return False
