import random
import sys
from pprint import pprint


class ListLogic:
    def __init__(self):
        print("init ListLogic")

    # リストの初期化。１行目のIDと２行目の縛り済フラグが無いリストの時は、挿入して初期化する
    def init_list(self, list):
        return

    # 引数１ 書き換えたいリスト（１行）
    # 引数２ 全てのリスト
    # 引数３ 書き換えたい要素数
    # 引数４ 書き換えたい文字列
    def convert_list(self, w_list, list, num, str):
        # 文字列検索
        # for word in w_list:
        #     index = list.index(word)
        list[int(w_list[0])][num] = str

        return list

