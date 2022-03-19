import random
from pprint import pprint


class RandChois:
    def __init__(self):
        print("init rand_chois")
        self.list = ''

    # 取得用リストを作った方が効率が良さそうだがまずは総当たりで作成
    def rand_chois(self, rc_min, rc_max):
        flag = False
        getlist = None
        while not flag:     # ラベルは無視する
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
