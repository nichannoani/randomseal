import random
import numpy as np
from pprint import pprint

HEADER = [['No', 'name', 'flag', 'rank', 'priority', 'compatibility']]


class MakeDict:
    print("init MakeDict")

    # def __init__(self, test, md_list=None):
    def __init__(self, test):
        self.list = None

        if test:
            #             管理番号 名前    縛り済未　  重要度   順位(num)    　　入れ子(A→B→C)
            self.list = [['No', 'name', 'flag', 'rank', 'priority ', 'compatibility'],
                         ['1', 'ライフアップB', 'F', 'SSSSS', '', ''],
                         ['2', '大きなおまもり', 'F', 'C', '', ''],
                         ['3', 'まよけのコイン', 'T', 'C', '', '']]
        '''
        else:
            pprint(md_list)
            pprint(md_list[0])
            a = np.array(md_list)
            b = np.array(header)

            # if md_list[0] == header:
            # print((a == b).all(axis=1).any())
            try:
                f = (a == b).all(axis=1).any()
            except:
                f = False

            if f:
                self.list = md_list
            else:
                md_list.pop(0)
                self.list = header + md_list
                pprint(self.list)
                # self.list.insert(len(self.list), header)
        '''

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
        except:
            f = False

        if f:   # ヘッダがきちんと設定されていればそのまま適用
            self.list = self.list
        else:   # ヘッダが設定されてなければ、一行目を強制削除して、２行目から適用
            self.list.pop(0)
            self.list = HEADER + self.list
            pprint(self.list)
            # self.list.insert(len(self.list), header)