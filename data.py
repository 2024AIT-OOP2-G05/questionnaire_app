import requests
from bs4 import BeautifulSoup
import json

# WebページのURLを指定
url = "http://127.0.0.1:8080"

# Webページを取得
response = requests.get(url)
response.raise_for_status()  # エラーチェック

# HTMLを解析
soup = BeautifulSoup(response.text, "html.parser")

# 必要なデータを抽出（例: タイトルとリンク）
data = []
for item in soup.find_all("a"):  # すべてのリンクを取得
    title = item.get_text(strip=True)  # リンクのテキスト
    link = item.get("href")  # リンクのURL
    if title and link:
        data.append({"title": title, "link": link})

# JSON形式に変換
json_data = json.dumps(data, indent=4, ensure_ascii=False)

# 結果を表示
print(json_data)

# JSONをファイルに保存
with open("output.json", "w", encoding="utf-8") as file:
    file.write(json_data)