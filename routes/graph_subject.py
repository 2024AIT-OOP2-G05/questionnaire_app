'''
import json
import matplotlib.pyplot as plt
from collections import Counter

# JSONファイルの読み込み
with open("database.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 全ての科目名（固定）
all_subjects = ["国語", "数学", "理科", "英語", "社会"]

# JSONデータから科目ごとの人数を集計
subjects = [item["subject"] for item in data["subject"]]
subject_counts = Counter(subjects)

# 全ての科目について人数を取得（存在しない場合は0）
counts = [subject_counts.get(subject, 0) for subject in all_subjects]

# 棒グラフの描画
plt.figure(figsize=(8, 6))
plt.bar(all_subjects, counts, color="skyblue")
plt.title("科目ごとの人数", fontsize=25)
plt.xlabel("科目", fontsize=20)
plt.ylabel("人数", fontsize=20)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# グラフの表示
plt.show()
'''

# routes/graph.py
from flask import Blueprint, jsonify, render_template
import sqlite3
import matplotlib.pyplot as plt
import os

graph_bp = Blueprint('graph', __name__)

@graph_bp.route('/generate_graph')
def generate_graph():
    # データベースに接続
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # 教科ごとの登録数を取得
    cursor.execute("SELECT subject, COUNT(*) FROM subjects GROUP BY subject")
    data = cursor.fetchall()
    conn.close()

    subjects = [item[0] for item in data]
    counts = [item[1] for item in data]

    # 棒グラフを描画
    plt.bar(subjects, counts)
    plt.xlabel('教科')
    plt.ylabel('登録数')
    plt.title('教科ごとの登録数')
    plt.xticks(rotation=45)

    # 画像を保存
    graph_path = os.path.join('static', 'graph.png')
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()

    return render_template('graph.html', graph_url=graph_path)