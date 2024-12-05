from peewee import Model, CharField
from .db import db

class Subject(Model):
    name = CharField()
    price = CharField()

    class Meta:
        database = db