import random
import numpy as np
from pprint import pprint


class MakeDict:
    print("init MakeDict")

    def __init__(self, test, md_list=None):
        header = [['No', 'name', 'flag', 'rank', 'priority', 'compatibility']]

        if md_list is None:
            md_list = header

        if test:
            #             管理番号 名前    縛り済未　  重要度   順位(num)    　　入れ子(A→B→C)
            self.list = [['No', 'name', 'flag', 'rank', 'priority ', 'compatibility'],
                         ['1', 'ライフアップB', 'F', 'SSSSS', '', ''],
                         ['2', '大きなおまもり', 'F', 'C', '', ''],
                         ['3', 'まよけのコイン', 'T', 'C', '', '']]
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

    def make_dict(self):
        print("make_dict")
