from w3.num import Num
from w3.sym import Sym
from w4.rows import Data

import util
# row.py has to be copied and put under class
# just copied from lua

class Dom():

    def dom(self, row1, row2, data ):
        s1, s2, n = 0
        n = len(data.w)

        for c, w in data.w.items():
            a0 = row1[c]
            b0 = row2[c]
            a = data.nums[c].num_norm(a0)
            b = data.nums[c].num_norm(b0)
            # b = Num.NumNorm(self.nums[c], b0)
            s1 = s1 - 10 ^ (w * (a - b) / n)
            s2 = s2 - 10 ^ (w * (b - a) / n)
        #Has to return bool/ read dom
        return (s1/n) < (s2/n)

    def another(self, row):
        # return another random row
        randRow = [x for x in range(self.rows) if x != row]
        return self.rows[randRow]

    def doms(self, data):
        data = Data()
        # -- what's this!
        n = 100
        c = len(data.name) + 1

        # not sure
        print(data.name , " , " , ",>dom")

        for r1 in range(len(data.rows)):
            row1 = data.rows[r1]
            row1.append(0)

            for s in range(n):
                row2 = self.another(row1)
                s = self.dom(row1, row2, data) and 1/n or 0
                row1[c] += s
            # dump(t.rows)
            # data.rows[i] = row1
            data.rows[i][-1] = round(round[i][-1], 2)
        return data

@util.O.k
def domTest():
    dom1 = Dom()
    d1 = Data()
    x = (d1.readerRows("../w4/weatherLong.csv"))
    d1.display()


