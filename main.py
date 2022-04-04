import csv
import lib.rand_Chois
import lib.make_dict
import lib.windowapp as wd
import lib.view_list

# ガター内の緑色のボタンを押すとスクリプトを実行します。
if __name__ == '__main__':
    make_dict = lib.make_dict.MakeDict(test=False)
    rand_chois = lib.rand_Chois.RandChois()
    view_list = lib.view_list.view_list()
    app = lib.windowapp.WindowApp(make_dict, rand_chois)

    # 実行処理
    while True:
        reset = app.mainloop()
        if not reset:
            break
        else:
            app = lib.windowapp.WindowApp(make_dict, rand_chois)
