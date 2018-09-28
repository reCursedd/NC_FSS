from w3.num import Num
from w3.sym import Sym
from w12 import w2
import util
import re

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

    def display(self):
        print("\nindex \t name \t\t  n\t   mode \t frequency")
        for i, sym in self.syms.items():
            print('{:<8} {:<12} {:<4} {:<12} {:<12}'.format(i+1, self.name[i], sym.n, sym.mode, sym.most))

        print("\nindex \tname \t\t\t n\t mu\t\t\tsd")
        for i, num in self.nums.items():
            print('{:<8} {:<14} {:<4} {:<10.2f} {:<8.2f}'.format(i+1, self.name[i], num.n, num.mu, (num.sd)))

# Can't we manually test
@util.O.k
def rowTest():
    d1 = Data()
    print('\n\n weather.csv')
    x = d1.readerRows("weather.csv")
    d1.display()

    d2 = Data()
    print('\n\n weatherLong.csv')
    d2.readerRows("weatherLong.csv")
    d2.display()

    d3 = Data()
    print('\n\n auto.csv')
    d3.readerRows("auto.csv")
    d3.display()