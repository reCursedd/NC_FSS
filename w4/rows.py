# just copied from lua code
from w3.num import Num
from w3.sym import Sym

class Data:
    def __init__(self):
        self.w = []
        self.syms = {}
        self.nums = {}
        self.dclass = None
        self.rows = {}
        self.name = {}
        self.use = {}

    def indep(self, c):
        return c not in self.w and self.dclass != c

    def dep(self, c):
        return not Data().indep(t,c)

    def header(self, cells, t):
        t = t or Data()
        t.indeps = {}
        for i,x in enumerate(cells):
            if ['%', '?'] not in x:
                c = len(self.use)+1
                self.use[c] = i
                self.name[c] = x
