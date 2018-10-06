from w3.num import Num
from w3.sym import Sym
from w12 import w2
import util
import re
import random
class Data:

    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.dclass = None
        self.rows = {}
        # Name of cols
        self.name = {}
        # Use are the cols that we will be using
        self.use = {}
        self.indeps = []

    def indep(self, c):
        return c not in self.w and self.dclass != c


    def dep(self, c):
        return not self.indep(c)

    # sets header and use cols
    def header(self, cells):
        for i,x in enumerate(cells):
            if not re.match('\?', x):
                # print ("printing x", x)
                c = len(self.use)
                # print ("Printing C", c)
                self.use[c] = i
                self.name[c] = x
                if re.match("[<>$]",x):
                    self.nums[c] = Num(0)
                else:
                    self.syms[c] = Sym()
                    #----why are setting goals for length of us?  Shouldn't it be for each column?
                if re.match("<",x) :
                    self.w[c] = -1
                elif re.match(">",x):
                    self.w[c] = 1
                elif re.match("!", x):
                    self.dclass = c
                else:
                    self.indeps.append(c)
        # print("last name", self.name)
        # print ("last use", self.use)

    # for every row this gets called once for formatting and incrementing values
    def row(self, cells):
        r = len(self.rows)
        # print ("r:", r)
        # print ("cells:", cells)
        self.rows[r] = []
        for i, c in (self.use).items():
            x = cells[c]
            if x != "?":
                if i in self.nums:
                    x = float(x)
                    self.nums[i].numInc(x)
                else:
                    self.syms[i].symInc(x)

            self.rows[r].append(x)



    # Only a csv reader, try doing with w2 code!
    def readerRows(self, file):
        t = Data()
        with open(file) as f:
            # ? how does this work
            first = True
            for line in f.readlines():
                re.sub("[\t\r\n ]*", "", line)
                re.sub("#.*", "", line)
                cells = [x.strip() for x in line.split(",")]
                if len(cells) > 0:
                    if first:
                        t = self.header(cells)
                    else:
                        t = self.row(cells)
                first = False
        return t

    def dom(self, row1, row2, data ):
        s1, s2, n = (0,0,0)
        n = len(data.w)

        for c, w in data.w.items():
            a0 = row1[c-1]
            b0 = row2[c-1]

            a = data.nums[c].numNorm(a0)
            b = data.nums[c].numNorm(b0)

            s1 = s1 - pow(10, (w * (a - b) / n))
            s2 = s2 - pow(10, (w * (b - a) / n))
        #Has to return bool/ read dom
        return (s1/n) < (s2/n)

    def another(self, row):
        # return another random row
        randRow = random.choice([x for x in range(0,len(self.rows)) if x != row])
        return self.rows[randRow]

    def doms(self, data):
        # -- what's this!
        n = 100
        c = len(data.name) + 1

        # not sure
        # print(data.name)

        print((','.join([x for x in data.name.values()])), ", >dom")
        data.name[c] = ">dom"
        for r1 in range(0,len(data.rows)):
            row1 = data.rows[r1]
            row1.append(0)
            # print (r1)
            for s in range(0,n):
                row2 = data.another(r1)
                s = self.dom(row1, row2, data) and 1/n or 0
                # print (self.dom(row1, row2, data))
                k = round(s, 2)
                row1[c - 1] = round((row1[c - 1] + k), 2)
                # row1[c] += s
            # dump(t.rows)
            # data.rows[i] = row1
            # data.rows[i][-1] = round(round[i][-1], 2)
        return data

@util.O.k
def domTest():
    d1 = Data()
    print ("weatherLong results")
    d1.readerRows("../w4/weatherLong.csv")
    d1.doms(d1)

    list(d1.rows.values()).sort(key=lambda x: x[-1], reverse=True)
    for i in d1.rows.values():
        print (i)

    print ("auto result")
    d2 = Data()
    d2.readerRows("../w4/auto.csv")
    d2.doms(d2)
    list(d2.rows.values()).sort(key=lambda x: x[-1], reverse=True)
    for i in d2.rows.values():
        print(i)



