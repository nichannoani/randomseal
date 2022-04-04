import csv
import tkinter
import tkinter as tk
from pprint import pprint
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog
import tkinter.filedialog
import lib.view_list
import os


class WindowApp:
    def __init__(self, make_dict, rand_chois):
        # 変数宣言
        self.csvlist = ''
        self.make_dict = make_dict
        self.rand_chois = rand_chois
        self.listflag = False
        self.tree = None
        self.listwin_tk = None

        # ウィンドウを作成
        self.win = tk.Tk()
        self.win.geometry("500x141")  # サイズを指定
        self.win.resizable(False, False)

        # メインフレーム
        main_frm = ttk.Frame(self.win)
        main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

        # ------ 各ウィジェットの設定 ------ #
        # ファイル参照ラベル
        folder_label = ttk.Label(main_frm, text="フォルダ指定")
        folder_label.grid(column=0, row=0, pady=10)

        # ファイル参照ファイルパス表示ボックス
        self.path = tk.StringVar()
        self.folder_box = ttk.Entry(main_frm)
        self.folder_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
        self.folder_box.configure(state='readonly')

        # ファイル参照ボタン
        folder_btn = ttk.Button(main_frm, text="参照", command=self.ask_folder)
        folder_btn.grid(column=2, row=0)

        # スピンボタンのラベル
        sp1_label = ttk.Label(main_frm, text="同時実行回数")
        sp1_label.grid(column=0, row=2, pady=10)

        # スピンボタン
        sptxt1 = tk.StringVar()
        self.sp1 = ttk.Spinbox(main_frm, textvariable=sptxt1, from_=0, to=10, increment=1)
        self.sp1.place(height=23, width=50, x=80, y=48)
        self.sp1.insert(0, '0')

        # 抽選実行ボタン
        self.__app_btn = ttk.Button(main_frm, text="抽選実行", command=self.lottery_click)
        self.__app_btn.grid(column=1, row=2)
        self.__app_btn['state'] = 'disabled'    # ファイルが読み込まれていない時点では、非表示にする

        # リスト表示ボタン
        self.__list_btn = ttk.Button(main_frm, text="リスト表示", command=self.listwin)
        self.__list_btn.grid(column=0, row=5, sticky=tk.SW)
        self.__list_btn['state'] = 'disabled'   # ファイルが読み込まれていない時点では、非表示にする

        # 閉じるボタン
        close_btn = ttk.Button(main_frm, text="閉じる", command=self.close)
        close_btn.grid(column=2, row=5, sticky=tk.SE)

        # 配置設定
        # win&メインフレームの描画
        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)
        main_frm.columnconfigure(1, weight=1)

        # ------ 画面のメニューバー ------ #
        # メニューバー作成
        men = tk.Menu(self.win, tearoff=0)

        # メニューバーを画面にセット
        self.win.config(menu=men)

        # メニューに親メニュー（ファイル）を作成する
        menu_file = tk.Menu(self.win, tearoff=0)
        men.add_cascade(label='ファイル', menu=menu_file)

        # バージョン情報
        version = tk.Menu(self.win, tearoff=0)
        men.add_cascade(label='バージョン情報', menu=version)
        version.add_command(label='バージョン情報', command=self.version)

        # 親メニューに子メニュー（開く・閉じる）を追加する
        menu_file.add_command(label='ファイルを開く(O)', command=self.ask_folder)
        menu_file.add_separator()
        menu_file.add_command(label='終了(X)', command=self.close)

        self.sp1.insert(0, '0')

    # 参照ボタンを押された時の処理
    def ask_folder(self):
        # pprint(self.csvlist)
        # ファイル選択ダイアログの表示
        # ftype = [("データファイル", "*.csv;*.xlsx;*.xls")]   # 最終形
        ftype = [("データファイル", "*.csv")]  # ひとまずcsvだけ
        file_path = tkinter.filedialog.askopenfilename(filetypes=ftype)
        # フォルダパスをテキストボックスに表示
        self.folder_box.configure(state='normal')
        self.folder_box.delete(0, tkinter.END)
        self.folder_box.insert(tkinter.END, file_path)
        self.folder_box.configure(state='readonly')
        # ここまで

        # ファイル起動処理
        if len(file_path) != 0:
            # ファイルが選択された場合
            with open(file_path) as f:
                reader = csv.reader(f)
                self.csvlist = [row for row in reader]
            if not self.rand_chois.set_data(self.csvlist):
                mbox.showinfo("警告", "リストが読み込まれていません")
                self.__list_btn['state'] = 'disabled'
                self.__app_btn['state'] = 'disabled'
            # 問題なく正常に処理が終わった
            self.listflag = True    # ファイルを読み込んだフラグ
            self.make_dict.make_dict(self.csvlist)  # 読み込んだファイルを整形する
            self.__list_btn['state'] = 'normal'
            self.__app_btn['state'] = 'normal'
        else:
            # ファイル選択がキャンセルされた場合
            self.csvlist = ''   # csvlistは空にする
            print("ファイルは選択されませんでした")
            self.__list_btn['state'] = 'disabled'
            self.__app_btn['state'] = 'disabled'

    # 抽選ボタンを押した時
    def lottery_click(self):
        if self.listflag:
            i = self.rand_chois.get_count()
            j = int(self.sp1.get())     # スピンボックスから同時回数を取得する
            if j > i or i <= 0:   # 同時実行回数よりも有効なリストを上回った時、もしくは有効なデータが無い時
                mbox.showerror("警告", "同時抽選回数が有効なリストを下回っています")
                return  # 関数終了
            while j >= 0:   # 同時実行回数分実行
                j -= 1
                ans = self.rand_chois.rand_chois()  # リストから抽選する
                print(type(ans))
                if ans == -1 and isinstance(ans, int):
                    mbox.showerror("警告", "同時抽選回数が有効なリストを下回っています")
                    return  # 関数終了
                t = viwetext_reformat(text=ans)    # 表示用に整形する
                mbox.showinfo("抽選結果", t)
        else:
            mbox.showinfo("警告", "リストが読み込まれていません")
        self.listwin_update()

    # リスト表示
    def listwin(self):
        vl = lib.view_list.view_list()
        self.listwin_tk = tk.Tk()
        self.listwin_tk.geometry("500x250")  # サイズを指定
        self.listwin_tk.title('Score List')
        column = self.csvlist[0]  # 先頭リスト（ヘッダ）の取得
        self.tree = ttk.Treeview(self.listwin_tk, columns=column)
        self.tree = vl.view_list(self.tree, self.csvlist)   # リストのデータを画面描画する

        # ウィジェットの配置
        self.tree.pack(pady=10)

    # リストの更新処理
    def listwin_update(self):
        self.tree.delete(*self.tree.get_children())  # 全ての描画したデータを削除
        vl = lib.view_list.view_list()
        self.tree = vl.view_list(self.tree, self.csvlist)   # 再度データを描画

    # 閉じるボタン
    def close(self):
        self.win.destroy()

    # 起動時に初期設定する
    def set(self):
        self.sp1.insert(0, '0')

    # メニューバージョン情報
    def version(self):
        mbox.showinfo("バージョン情報", "Share Ver: 0.01")

    def mainloop(self, *args):
        print("nowloop")
        self.set()
        self.win.mainloop()
        return False    # 正常終了はFalse


# 抽選ボタンの結果表示の文章を整形する
def viwetext_reformat(text):
    ans = ""
    cnt = 0

    for who in text:
        if not who == '' and cnt == 0:
            ans += who
        elif not who == '' and cnt != 2:
            ans += " " + who
        cnt += 1

    print("ans:", ans)
    return ans