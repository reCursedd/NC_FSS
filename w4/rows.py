# just copied from lua code
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
        self.use = {}
        self.indeps = []
    def indep(self, c):
        return c not in self.w and self.dclass != c


    def dep(self, c):
        return not Data().indep(t,c)


    def header(self, cells):
        for i,x in enumerate(cells):
            if not re.match('\?', x):
                c = len(self.use)
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



    def row(self, cells):
        r = len(self.rows)
        self.rows[r] = {}
        for i, c in enumerate(self.use):
            x = cells[i]
            if x != "?":
                if c in self.nums:
                    x = float(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[r][c] = x



    # Only a csv reader
    def reader(self, file):
        t = Data()
        with open(file) as f:
            # ? how does this work
            first = True
            for line in f.readlines():
                re.sub("[\t\r ]*", "", line)
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
        print("\nindex \t name \t  n\t   mode \t frequency")
        for i, sym in self.syms.items():
            print('{:<8} {:<8} {:<4} {:<12} {:<12}'.format(i, self.name[i], sym.n, sym.mode, sym.most))

        print("\n\t          \t\t n\t\t mu\t sd")
        for i, num in self.nums.items():
            print('{:<8} {:<8} {:<4} {:<12} {:<12}'.format(i, self.name[i], num.n, num.mu, (num.sd)))

# Can't we manually test
@util.O.k
def rowTest():
    d = Data()
    print('\n\n weather.csv')
    d.reader("weather.csv")
    d.display()
    # This one is not working :( still
    print('\n\n weatherLong.csv')
    d.reader("weatherLong.csv")
    d.display()