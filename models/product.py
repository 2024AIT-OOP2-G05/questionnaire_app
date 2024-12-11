from peewee import Model, CharField, DecimalField
from .db import db

class Product(Model):
    name = CharField()
    price = DecimalField()
    bloodtype = CharField()
    class Meta:
        database = db