from google.colab import drive
drive.mount('/content/drive')

import sys
sys.path.append('/content/drive/My Drive/your-repository-path/prog')

from prog.itema import load_object_data, get_object_value

# "gold" の値を取得
print(get_object_value('gold'))  # 2
