from peewee import SqliteDatabase
from .db import db
from .user import User
from .product import Product
from .order import Order
<<<<<<< Updated upstream
=======
from.favorite_subject import Favorite_subject
>>>>>>> Stashed changes

# モデルのリストを定義しておくと、後でまとめて登録しやすくなります
MODELS = [
    User,
    Product,
    Order,
<<<<<<< Updated upstream
=======
    Favorite_subject
>>>>>>> Stashed changes
]

# データベースの初期化関数
def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()