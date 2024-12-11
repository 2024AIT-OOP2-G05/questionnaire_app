from flask import Blueprint, render_template, request, redirect, url_for
from models import User

# Blueprintの作成
user_bp = Blueprint('user', __name__, url_prefix='/users')

# 星座の選択肢
ZODIAC_SIGNS = [
    "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座",
    "乙女座", "天秤座", "蠍座", "射手座", "山羊座",
    "水瓶座", "魚座"
]

@user_bp.route('/')
def list():
    
    # データ取得
    users = User.select()

    return render_template('user_list.html', title='ユーザー一覧', items=users)


@user_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        zodiac_sign = request.form['zodiac_sign']  # 星座データを取得
        User.create(name=name, age=age, zodiac_sign=zodiac_sign)
        return redirect(url_for('user.list'))
    
    return render_template('user_add.html', zodiac_signs=ZODIAC_SIGNS)


@user_bp.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit(user_id):
    user = User.get_or_none(User.id == user_id)
    if not user:
        return redirect(url_for('user.list'))

    if request.method == 'POST':
        user.name = request.form['name']
        user.age = request.form['age']
        user.zodiac_sign = request.form['zodiac_sign']  # 星座データを更新
        user.save()
        return redirect(url_for('user.list'))

    return render_template('user_edit.html', user=user, zodiac_signs=ZODIAC_SIGNS)