import random
import numpy as np
from pprint import pprint

# 規定のヘッダ。仕様変更予定。順番変更No,flag、Name。左３つ以降は無し。
HEADER = [['No', 'name', 'flag', 'rank', 'priority', 'compatibility']]


class MakeDict:
    def __init__(self, test):
        print("init MakeDict")
        self.list = None

        if test:
            #             管理番号 名前    縛り済未　  重要度   順位(num)    　　入れ子(A→B→C)
            self.list = [['No', 'name', 'flag', 'rank', 'priority ', 'compatibility'],
                         ['1', 'ライフアップB', 'F', 'SSSSS', '', ''],
                         ['2', '大きなおまもり', 'F', 'C', '', ''],
                         ['3', 'まよけのコイン', 'T', 'C', '', '']]

    # CSVから読み込んだデータを整形する
    def make_dict(self, md_list):
        self.list = md_list
        print("make_dict")
        pprint(self.list)
        pprint(self.list[0])
        a = np.array(self.list)
        b = np.array(HEADER)

        # ヘッダが定義されているかチェック
        try:
            f = (a == b).all(axis=1).any()
        except:     # 何かしらのエラーが発生したら、次の処理で一行目を削除する
            f = False

        if f:   # ヘッダがきちんと設定されていればそのまま適用
            self.list = self.list
        else:   # ヘッダが設定されてなければ、一行目を強制削除して、２行目から適用
            self.list.pop(0)
            self.list = HEADER + self.list
            pprint(self.list)
            # self.list.insert(len(self.list), header)