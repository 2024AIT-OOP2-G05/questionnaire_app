from flask import Flask, render_template
from models import initialize_database
from routes import blueprints
import sqlite3
import json

app = Flask(__name__)

# データベースの初期化
initialize_database()

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# テーブルをJSONに変換する関数
def convert_table_to_json(db_file, table_name, json_file):
    try:
        # SQLite データベースに接続
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # テーブルのデータを取得
        cursor.execute(f"SELECT * FROM `{table_name}`")
        rows = cursor.fetchall()

        # テーブルのカラム名を取得
        cursor.execute(f"PRAGMA table_info(`{table_name}`)")
        columns = [column[1] for column in cursor.fetchall()]

        # データをリストの辞書形式に変換
        table_data = [dict(zip(columns, row)) for row in rows]

        # JSON ファイルに書き出し
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({table_name: table_data}, f, indent=4, ensure_ascii=False)

        print(f"テーブル '{table_name}' が正常に {json_file} に変換されました。")
        return True, f"テーブル '{table_name}' が正常に {json_file} に変換されました。"
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False, f"エラーが発生しました: {e}"
    finally:
        if connection:
            connection.close()

# ホームページのルート
@app.route('/')
def index():
    db_file = 'my_database.db'  # データベースファイルのパス
    table_name = 'blood_type'  # 変換したいテーブル名
    json_file = f'{table_name}.json'  # 出力するJSONファイル名

    # テーブルをJSONに変換
    success, message = convert_table_to_json(db_file, table_name, json_file)

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
