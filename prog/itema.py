import json
import os

# object.jsonを読み込む関数
def load_object_data():
    # 自分のプロジェクトディレクトリのパスを指定
    json_path = './prog/json/object.json'  # この場所にファイルを置いていることを確認

    # ファイルが存在するか確認
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"{json_path} が見つかりません")

    # JSONファイルを開く
    with open(json_path, 'r') as file:
        return json.load(file)

# 読み込んだデータを利用する
def get_object_value(object_name):
    data = load_object_data()  # object.jsonの内容を読み込む
    return data.get(object_name, "Object not found")  # 存在しない場合はエラーメッセージを返す

# "gold" の値を取得
print(get_object_value('gold'))  # 期待値: 2
