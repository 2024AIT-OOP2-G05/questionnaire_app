from .user import user_bp
from .product import product_bp
from .order import order_bp
from .subject import subject_bp
from .blood_type import blood_type_bp
# Blueprintをリストとしてまとめる
blueprints = [
  user_bp,
  product_bp,
  order_bp,
  subject_bp,
  blood_type_bp
]
