# 勉強用にソースコードのメモを書いたファイルです
# 複数の機能があったとしても、機能に一貫性はありません。




# 1．Outlookを操作するコード 新しいOutlookでは動かない
""" import win32com.client

try:
    print("Outlook.Application を取得中...")
    outlook = win32com.client.Dispatch("Outlook.Application")
    print("成功: Outlook.Application オブジェクトを取得")

    print("MAPI ネームスペースを取得中...")
    namespace = outlook.GetNamespace("MAPI")
    print("成功: MAPI オブジェクト取得")

except Exception as e:
    print("失敗:", repr(e))
 """
 
 