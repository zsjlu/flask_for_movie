# coding: utf-8
from application import db




class User1(db.Model):
    __tablename__ = 'user1'

    id = db.Column(db.Integer, primary_key=True, info='??')
    nickname = db.Column(db.String(30), nullable=False, server_default=db.FetchedValue(), info='??')
    login_name = db.Column(db.String(20), nullable=False, unique=True, server_default=db.FetchedValue(), info='?????')
    login_pwd = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='??????')
    login_salt = db.Column(db.String(32), nullable=False, server_default=db.FetchedValue(), info='?????????')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='?? 0??? 1???')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????????')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='????')
