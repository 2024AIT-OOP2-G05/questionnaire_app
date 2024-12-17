import sqlite3
import json

def convert_db_to_json(db_file, json_file):
    try:
        # SQLite データベースに接続
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # データベース内のすべてのテーブルを取得
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        db_data = {}

        # 各テーブルのデータを取得
        for table_name in tables:
            table_name = table_name[0]
            # テーブル名をバッククォートで囲む
            cursor.execute(f"SELECT * FROM `{table_name}`")
            rows = cursor.fetchall()

            # テーブルのカラム名を取得
            cursor.execute(f"PRAGMA table_info(`{table_name}`)")
            columns = [column[1] for column in cursor.fetchall()]

            # データをリストの辞書形式に変換
            db_data[table_name] = [dict(zip(columns, row)) for row in rows]

        # JSON ファイルに書き出し
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(db_data, f, indent=4, ensure_ascii=False)

        print(f"データベースが正常に{json_file}に変換されました。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        if connection:
            connection.close()

# 使用例
convert_db_to_json('my_database.db', 'database.json')
