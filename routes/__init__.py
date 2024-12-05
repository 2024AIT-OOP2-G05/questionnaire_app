from .user import user_bp
from .product import product_bp
from .order import order_bp
from.favorite_subject import favorite_subject_bp

# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  favorite_subject_db
]
