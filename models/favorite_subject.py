from peewee import Model, CharField
from .db import db

class Favorite_subject(Model):
    name = CharField()
    subject = CharField()

    class Meta:
        database = db