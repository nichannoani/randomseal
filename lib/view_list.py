# csvファイルを読み込んで、ttk.Treeviewに一列づつ入れていく処理
import copy


class view_list:

    def __init__(self):
        # 変数宣言
        self.hoge = 0

    # オブジェクト、リストを引数にして、リストのデータを繰り返して挿入する
    def view_list(self, tree, list):
        # treeのデータ入れていく
        # 列の設定
        tree.column('#0', width=0, stretch='no')
        # list_data = list.copy()
        list_head = list[0]
        list_data = list[1:]
        print(list_head)
        print(list_data)

        for arr in list_head:
            # for el in arr:
                print(arr)
                tree.column(arr, anchor='center', width=80)

        # 列の見出し設定
        tree.heading('#0', text='')
        # tree.heading('ID', text='ID', anchor='center')

        for arr in list_head:
            # for el in arr:
                print(arr)
                tree.heading(arr, text=arr, anchor='center')
                # tree.column(arr, anchor='center', width=80)

        # レコードの追加
        i = 0
        for arr in list_data:
            tree.insert(parent='', index='end', iid=i, values=arr)
            i += 1
            #for el in arr:
            #    print(el)
            #    tree.insert(parent='', index='end', iid=0, values=arr)

        # tree.insert(parent='', index='end', iid=0, values=(1, 'KAWASAKI', 80))

        return tree