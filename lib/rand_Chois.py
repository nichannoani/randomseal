import random
import sys
import lib.list_logic as list_logic
from pprint import pprint


class RandChois:
    def __init__(self):
        print("init rand_chois")
        self.__list = None  # クラス内で使うリストの複製先変数
        self.set_flg = False    # リストを正常に設定したか
        self.__count = 0    # リスト内の有効な項目（縛り前）回数のカウント
        self.__list_logic = list_logic.ListLogic()

    # リストを読み込んで、整形する
    def set_data(self, inport_list):
        self.__list = inport_list
        # 有効な項目数をカウントする
        for l in self.__list:
            if l[2] == 'T':
                self.__count += 1
        # print("このリストの有効な項目数： ", self.__count)

        # 有効な項目数
        if self.__count == 0:
            return False
        else:
            self.set_flg = True     # 正常に読み込めたら、フラグを設定
            return True

    # 有効な項目数を返す
    def get_count(self):
        return self.__count

    # リストを返す
    def get_list(self):
        return self.__list

    # 取得用リストを作った方が効率が良さそうだがまずは総当たりで作成
    def rand_chois(self):
        # 変数宣言
        flag = False
        getlist = None

        if not self.set_flg:    # リスト読み込みせずに抽選処理しようとした時
            sys.exit("リストが正常に読み込まれていません")
        elif self.__count <= 0:
            return -1

        while not flag:  # ラベルは無視する
            getlist = random.choice(self.__list)  # 抽選する。結果を変数に入れて検証
            print(getlist[2])
            if not getlist[0] == 'No' and getlist[2] == 'T':
                self.__list = self.__list_logic.convert_list(getlist, self.__list, 2, 'F')
                flag = True

        self.__count -= 1  # 正常に処理が完了したら、有効な数をデクリメントする
        # 取得チェック
        # print(getlist[0])  # 管理No取得
        # pprint(test)    # リスト取得
        # print(random.choice(self.list))
        # print("Name", getlist[1], end='')
        # print(" Rank", getlist[3])
        return getlist