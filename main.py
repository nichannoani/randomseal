# これはサンプルの Python スクリプトです。

# Shift+F10 を押して実行するか、ご自身のコードに置き換えてください。
# Shift を2回押す を押すと、クラス/ファイル/ツールウィンドウ/アクション/設定を検索します。
import csv
import lib.rand_Chois
import lib.make_dict
import lib.windowapp as wd

# from mypackage.mod2 import square as square


def print_hi(name):
    # スクリプトをデバッグするには以下のコード行でブレークポイントを使用してください。
    print(f'Hi, {name}')  # Ctrl+F8を押すとブレークポイントを切り替えます。


# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    print_hi('PyCharm')

    # list = lib.make_dict.MakeDict(test=True)
    make_dict = lib.make_dict.MakeDict(test=False)
    rand_chois = lib.rand_Chois.RandChois()
    # rand_chois.rand_chois(1)

    app = lib.windowapp.WindowApp(make_dict, rand_chois)
    app.mainloop()

    # myinstance = MyClass("Hello!")
    # print(myinstance.value)

# PyCharm のヘルプは https://www.jetbrains.com/help/pycharm/ を参照してください
