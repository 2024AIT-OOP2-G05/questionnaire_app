from flask import Blueprint, render_template, request, redirect, url_for
from models import Subject

# Blueprintの作成
subject_bp = Blueprint('subject', __name__, url_prefix='/subjects')


@subject_bp.route('/')
def list():
    subjects = Subject.select()
    return render_template('subject_list.html', title='好きな教科一覧', items=subjects)


@subject_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']  # 'name' フィールドを取得

        #person_name = request.form['person_name']  # 'person_name' フィールドを取得
        subject = request.form['subject']  # 選ばれた血液型を取得
        #Blood_type.create(name=name, person_name=person_name, price=blood_type_value)  # データベースに保存
        Subject.create(name=name,  subject=subject)

        return redirect(url_for('subject.list'))

    return render_template('subject_add.html')


@subject_bp.route('/edit/<int:subject_id>', methods=['GET', 'POST'])
def edit(subject_id):
    subject = Subject.get_or_none(subject.id == subject_id)
    if not subject:
        return redirect(url_for('subject.list'))

    if request.method == 'POST':
        subject.name = request.form['name']
        subject.subject = request.form['subject']
        subject.save()
        return redirect(url_for('subject.list'))
    

    return render_template('subject_edit.html', subject=subject)