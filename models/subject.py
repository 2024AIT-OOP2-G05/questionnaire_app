from peewee import Model, CharField, DecimalField
from .db import db

class Subject(Model):
    name = CharField()

    subject = CharField()

    class Meta:
        database = db