from flask import Blueprint, render_template, request, redirect, url_for
from models import Blood_type

# Blueprintの作成
blood_type_bp = Blueprint('blood_type', __name__, url_prefix='/blood_types')


@blood_type_bp.route('/')
def list():
    blood_types = Blood_type.select()
    return render_template('blood_type_list.html', title='血液型一覧', items=blood_types)


@blood_type_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        Blood_type.create(name=name, price=price)
        return redirect(url_for('blood_type.list'))
    
    return render_template('blood_type_add.html')


@blood_type_bp.route('/edit/<int:blood_type_id>', methods=['GET', 'POST'])
def edit(blood_type_id):
    blood_type = Blood_type.get_or_none(Blood_type.id == blood_type_id)
    if not blood_type:
        return redirect(url_for('blood_type.list'))

    if request.method == 'POST':
        blood_type.name = request.form['name']
        blood_type.price = request.form['price']
        blood_type.save()
        return redirect(url_for('blood_type.list'))

    return render_template('blood_type_edit.html', blood_type=blood_type)