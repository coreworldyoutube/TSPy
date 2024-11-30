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
