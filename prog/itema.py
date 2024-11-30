import json
import os

# object.jsonを読み込む関数
def load_object_data():
    # 'prog/json' フォルダ内の object.json を指定
    json_path = os.path.join(os.path.dirname(__file__), 'json', 'object.json')
    
    # ファイルの存在を確認
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"指定されたファイルが見つかりません: {json_path}")
    
    with open(json_path, 'r') as file:
        return json.load(file)

# 読み込んだデータを利用する
def get_object_value(object_name):
    data = load_object_data()  # object.jsonの内容を読み込む
    return data.get(object_name, "Object not found")  # 存在しない場合はエラーメッセージを返す
