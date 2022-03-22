import csv
import tkinter
import tkinter as tk
from pprint import pprint
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog
import tkinter.filedialog
import os


class WindowApp:

    def __init__(self, make_dict, rand_chois):
        # 変数宣言
        self.csvlist = ''
        self.make_dict = make_dict
        self.rand_chois = rand_chois
        self.listflag = False

        # mlist = lib.make_dict.MakeDict(test=False)
        # rand_chois = lib.rand_Chois.RandChois(1, 10, mlist.list)

        # ウィンドウを作成 --- (*1)
        self.win = tk.Tk()
        self.win.geometry("500x250")  # サイズを指定
        self.win.resizable(False, False)

        # 部品を作成 --- (*2)
        # ラベルを作成
        # self.label = tk.Label(self.win, text='名前は?')
        # self.label.pack()

        # メインフレーム
        main_frm = ttk.Frame(self.win)
        main_frm.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)

        # ファイル参照ラベル
        folder_label = ttk.Label(main_frm, text="フォルダ指定")
        folder_label.grid(column=0, row=0, pady=10)

        # ファイル参照ファイルパス表示ボックス
        folder_box = ttk.Entry(main_frm)
        folder_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)

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

        # 実行ボタン
        app_btn = ttk.Button(main_frm, text="抽選実行", command=self.lottery_click)
        app_btn.grid(column=1, row=2)

        # リスト表示ボタン
        list_btn = ttk.Button(main_frm, text="リスト表示", command=self.listwin)
        list_btn.grid(column=1, row=4)

        # 閉じるボタン
        close_btn = ttk.Button(main_frm, text="閉じる", command=self.close)
        close_btn.grid(column=3, row=5)

        # 再描画
        # reset = ttk.Button(main_frm, text="再描画", command=self.reset)

        # self.order_label.grid(column=0, row=1)
        # self.order_comb.grid(column=1, row=1, sticky=tkinter.W, padx=5)

        # reset.grid(column=1, row=5)

        # 配置設定

        # win&メインフレームの描画
        self.win.columnconfigure(0, weight=1)
        self.win.rowconfigure(0, weight=1)
        main_frm.columnconfigure(1, weight=1)

        # self.okButton = tk.Button(self.win, text='参照', command=self.ok_click)
        # self.okButton.pack()

        # 抽選ボタン
        # self.okButton = tk.Button(self.win, text='抽選', command=self.lottery_click)
        # self.okButton.pack()

        # 画面のメニューバー
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
        menu_file.add_command(label='ファイルを開く(O)', command=self.file_read)
        menu_file.add_separator()
        menu_file.add_command(label='終了(X)', command=self.close)

    # 参照ボタンを押した時 --- (*3)
    def ask_folder(self):
        self.file_read()
        pprint(self.csvlist)

    def file_read(self):
        # ファイル選択ダイアログの表示
        ftype = [("データファイル", "*.csv;*.xlsx;*.xls")]
        file_path = tkinter.filedialog.askopenfilename(filetypes=ftype)
        if len(file_path) != 0:
            # ファイルが選択された場合
            with open(file_path) as f:
                reader = csv.reader(f)
                self.csvlist = [row for row in reader]
            self.listflag = True
        else:
            # ファイル選択がキャンセルされた場合
            # csvlistは空にする
            self.csvlist = ''
            print("ファイルは選択されませんでした")

    # 抽選ボタンを押した時
    def lottery_click(self):
        if self.listflag:
            self.make_dict.make_dict(self.csvlist)
            ans = self.rand_chois.rand_chois(1, 1, self.csvlist)
            t = self.viwetext_reformat(text=ans)
            mbox.showinfo("抽選結果", t)
        else:
            mbox.showinfo("警告", "リストが読み込まれていません")

    # 抽選ボタンの結果表示の文章を整形する
    def viwetext_reformat(self, text):
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

    def listwin(self):
        listwin = tk.Tk()
        listwin.geometry("500x250")  # サイズを指定
        column = ('ID', 'Name', 'Score')
        listwin.title('Score List')
        tree = ttk.Treeview(listwin, columns=column)
        # 列の設定
        tree.column('#0', width=0, stretch='no')
        tree.column('ID', anchor='center', width=80)
        tree.column('Name', anchor='w', width=100)
        tree.column('Score', anchor='center', width=80)
        # 列の見出し設定
        tree.heading('#0', text='')
        tree.heading('ID', text='ID', anchor='center')
        tree.heading('Name', text='Name', anchor='w')
        tree.heading('Score', text='Score', anchor='center')
        # レコードの追加
        tree.insert(parent='', index='end', iid=0, values=(1, 'KAWASAKI', 80))
        tree.insert(parent='', index='end', iid=1, values=(2, 'SHIMIZU', 90))

        # ウィジェットの配置
        tree.pack(pady=10)

    def close(self):
        self.win.destroy()

    # 起動時に初期設定する
    def set(self):
        self.sp1.insert(0, '0')

    # 起動時に初期設定する
    def open_file(self):
        print("")

    def version(self):
        mbox.showinfo("バージョン情報", "Share Ver: 0.01")

    # 起動時に初期設定する
    def close_disp(self):
        # self.sp1.insert(0, '0')
        print("")

    def mainloop(self, *args):
        print("nowloop")
        self.set()
        self.win.mainloop()
        return False    # 正常終了はFalse
