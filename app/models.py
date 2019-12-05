from app import db
import datetime
from sqlalchemy import Integer
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(Integer, primary_key=True)
    username = db.Column(db.String(64), index=False, unique=True, nullable=False)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Products(UserMixin,db.Model):
    __tablename__ = 'products'
    product_id = db.Column(Integer,primary_key=True,autoincrement=True)
    product_name = db.Column(db.String(60),nullable=False)
    quantity = db.Column(Integer, nullable=False)

    def __repr__(self):
        return '<Products {}>'.format(self.product_name,self.quantity)


class Locations(UserMixin,db.Model):
    __tablename__ = 'locations'
    location_id = db.Column(Integer, primary_key=True, autoincrement=True)
    location_name = db.Column(db.String(50),nullable=False)

    def __repr__(self):
        return '<Products {}>'.format(self.location)

class Movements(UserMixin,db.Model):
    __tablename__ = 'movements'
    transaction_id = db.Column(Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(60),nullable=False)
    time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    from_warehouse = db.Column(db.String(60),nullable=False)
    to_warehouse = db.Column(db.String(60),nullable=False)
    quantity = db.Column(Integer, nullable=False)

    def __repr__(self):
        return '<Products {}>'.format(self.transaction_id,self.product_name,self.time,self.from_warehouse,self.to_warehouse,self.to_warehouse,self.quantity)
