import random
import sys
from pprint import pprint


class RandChois:
    def __init__(self):
        print("init rand_chois")
        self.list = None
        self.set_flg = False
        self.__count = 0

    def set_data(self, inport_list):
        self.list = inport_list
        for l in self.list:
            if l[2] == 'T':
                self.__count += 1
        print(self.__count)

        if self.__count == 0:
            return False
        else:
            self.set_flg = True
            return True

    def get_count(self):
        return self.__count

    # 取得用リストを作った方が効率が良さそうだがまずは総当たりで作成
    def rand_chois(self):
        if not self.set_flg:    # リスト読み込みせずに抽選処理しようとした時
            sys.exit("リストが正常に読み込まれていません")
       # elif rc_max > self.count:   #
       #     sys.exit("同時抽選回数が有効なリストを下回っています")

        flag = False
        getlist = None
        while not flag:  # ラベルは無視する
            getlist = random.choice(self.list)
            print(getlist[2])
            if not getlist[0] == 'No' and getlist[2] == 'T':
                flag = True

        # 取得チェック
        print(getlist[0])  # 管理No取得
        # pprint(test)    # リスト取得
        # print(random.choice(self.list))
        print("Name", getlist[1], end='')
        print(" Rank", getlist[3])
        self.__count -= 1

        return getlist


def true_count(inport_list):
    count = 0

    # for list in inport_list:
    #        list[]

    return count
