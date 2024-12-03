# prog/itema.py

import json
import os

def load_object_data():
    """
    JSONファイルからデータを読み込む関数。
    ファイルが存在しない場合はエラーメッセージを表示。
    """
    json_path = os.path.join(os.path.dirname(__file__), 'json', 'object.json')  # JSONファイルのパス

    # ファイルの存在確認と読み込み
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Error: {json_path} not found.")
    
    with open(json_path, 'r') as file:
        return json.load(file)

def get_object_value(key, data):
    """
    読み込んだデータから指定されたキーの値を取得する関数。
    キーが存在しない場合は None を返す。
    """
    return data.get(key, None)  # キーが存在しない場合は None を返す
