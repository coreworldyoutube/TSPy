import json

# object.jsonを読み込む関数
def load_object_data():
    # Google Colabのパス
    json_path = '/content/prog/json/object.json'

    with open(json_path, 'r') as file:
        return json.load(file)

# 読み込んだデータを利用する
def get_object_value(object_name):
    data = load_object_data()  # object.jsonの内容を読み込む
    return data.get(object_name, "Object not found")  # 存在しない場合はエラーメッセージを返す

# "gold" の値を取得
print(get_object_value('gold'))  # 期待値: 2
