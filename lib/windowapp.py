import csv
import tkinter
import tkinter as tk
from pprint import pprint
from tkinter import messagebox as mbox
from tkinter import filedialog
import tkinter.filedialog
import os


class WindowApp:

    def __init__(self):
        # 変数宣言
        self.csvlist = ''

        # ウィンドウを作成 --- (*1)
        self.win = tk.Tk()
        self.win.geometry("500x250")  # サイズを指定

        # 部品を作成 --- (*2)
        # ラベルを作成
        self.label = tk.Label(self.win, text='名前は?')
        self.label.pack()

        # テキストボックスを作成
        self.text = tk.Entry(self.win)
        self.text.pack()
        self.text.insert(tk.END, 'クジラ')  # 初期値を指定

        # ファイル参照ボタン
        self.okButton = tk.Button(self.win, text='参照', command=self.ok_click)
        self.okButton.pack()

        # 抽選ボタン
        self.okButton = tk.Button(self.win, text='抽選', command=self.ok_click)
        self.okButton.pack()

    # 参照ボタンを押した時 --- (*3)
    def ok_click(self):
        self.file_read()
        pprint(self.csvlist)

    def file_read(self):
        # ファイル選択ダイアログの表示
        file_path = tkinter.filedialog.askopenfilename()
        if len(file_path) != 0:
            # ファイルが選択された場合
            with open(file_path) as f:
                reader = csv.reader(f)
                self.csvlist = [row for row in reader]
        else:
            # ファイル選択がキャンセルされた場合

            # csvlistは空にする
            self.csvlist = ''
            print("ファイルは選択されませんでした")

    def mainloop(self, *args):
        print("nowloop")
        self.win.mainloop()