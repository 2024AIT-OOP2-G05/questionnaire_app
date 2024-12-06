from peewee import Model, CharField, IntegerField
from .db import db

class User(Model):
    name = CharField()
    age = IntegerField()
    zodiac_sign = CharField()  # 星座フィールド追加


    class Meta:
        database = db