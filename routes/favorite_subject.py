from flask import Blueprint, render_template, request, redirect, url_for
from models import Favorite_subject

favorite_subject_bp = Blueprint('favorite_subject', __name__, url_prefix='/favorite_subjects')
@favorite_subject_bp.route('/')
def list():
    products = Favorite_subject.select()
    return render_template('favorite_subject_list.html', title='教科一覧', items=favorite_subjects)

@favorite_subject_bp.route('/add', methods=['GET', 'POST'])
def add():
    
    # POSTで送られてきたデータは登録
    if request.method == 'POST':
        name = request.form['name']
        favorite_subject = request.form['favorite_subject']
        Favorite_subject.create(name=name, favorite_subject=favorite_subject)
        return redirect(url_for('favorite_sbject.list'))
    
    return render_template('favorite_subject_add.html')

@favorite_subject_bp.route('/edit/<int:favorite_subject_id>', methods=['GET', 'POST'])
def edit(favorite_subject_id):
    favorite_subject = Favorite_subject.get_or_none(Favorite_subject.id == favorite_subject_id)
    if not favorite_subject:
        return redirect(url_for('favorite_sbject.list'))

    if request.method == 'POST':
        favorite_subject.name = request.form['name']
        favorite_subject.price = request.form['price']
        favorite_subject.save()
        return redirect(url_for('favorite_sbject.list'))

    return render_template('favorite_sbject_edit.html', favorite_subject=favorite_subject)