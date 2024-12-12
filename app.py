from flask import Flask, render_template, jsonify 
from models import initialize_database
from routes import blueprints
from models.user import User


app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/users/json', methods=['GET'])
def get_users_json():
    """ユーザーデータをJSON形式で返す"""
    # データベースから全ユーザー情報を取得
    users = User.select()

    # データを辞書形式に変換してリスト化
    users_list = [user.to_dict() for user in users]

    # JSON形式で返す
    return jsonify(users_list)


if __name__ == '__main__':
    app.run(port=8081, debug=True)
