from peewee import Model, CharField, DecimalField
from .db import db

class Blood_type(Model):
    name = CharField()
    price = DecimalField()

    class Meta:
        database = db