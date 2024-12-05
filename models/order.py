from peewee import Model, ForeignKeyField, DateTimeField
from .db import db
from .user import User
from .product import Product
from.favorite_subject import Favorite_subject

class Order(Model):
    user = ForeignKeyField(User, backref='orders')
    product = ForeignKeyField(Product, backref='orders')
    order_date = DateTimeField()

    class Meta:
        database = db
