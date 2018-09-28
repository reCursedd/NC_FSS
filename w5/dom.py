from w3.num import Num
from w3.sym import Sym
# row.py has to be copied and put under class
# just copied from lua

def dom(self, row1, row2):
    s1, s2, n = 0
    for x in (self.w):
        n = n + 1

    for c, w in enumerate(self.w):
        a0 = row1[c]
        b0 = row2[c]
        a = Num.NumNorm(self.nums[c], a0)
        b = Num.NumNorm(self.nums[c], b0)
        s1 = s1 - 10 ^ (w * (a - b) / n)
        s2 = s2 - 10 ^ (w * (b - a) / n)
    return s1/n < s2/n


def doms(self):
    # -- what's this!
    # n = samples
    c = len(t.name) + 1

    # not sure
    print(t.name + "," + ",>dom")
    for r1 in len(t.rows):
        row1 = self.rows[r1]
        row1[c] = 0
        for s in range(n):
            row2 = another(r1, self.rows)
            s = dom(t, row1, row2) and 1/n or 0
            row1[c] += s
        dump(t.rows)

def mainDom(source):
    doms(rows())
