import json

# object.jsonを読み込む関数
def load_object_data():
    with open('object.json', 'r') as file:
        return json.load(file)

# 読み込んだデータを利用する
def get_object_value(object_name):
    data = load_object_data()  # object.jsonの内容を読み込む
    return data.get(object_name, "item not found")  # 存在しない場合はエラーメッセージを返す

# テスト: "gold"の値を取得する
object_name = "gold"
value = get_object_value(object_name)
print(f"The value of {object_name} is: {value}")
