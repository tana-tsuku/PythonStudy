# 勉強用にソースコードのメモを書いたファイルです
# 複数の機能があったとしても、機能に一貫性はありません。

from datetime import date

# test.txtファイルｗを読み込む
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.readline()

t = date.today()
# 今日の日付を表示
print(f"今日の日付は {t.year}年{t.month}月{t.day}日です。")
