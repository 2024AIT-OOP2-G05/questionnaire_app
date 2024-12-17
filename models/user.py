from peewee import Model, CharField, IntegerField
from peewee import SqliteDatabase

# データベース接続
db = SqliteDatabase('my_database.db')

# Userモデル
class User(Model):
    name = CharField()
    age = IntegerField()
    zodiac_sign = CharField()

    class Meta:
        database = db

    def to_dict(self):
        """モデルデータを辞書形式に変換する"""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "zodiac_sign": self.zodiac_sign
        }
