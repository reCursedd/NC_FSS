# Entropy
import math
import util
class Sym:

    def __init__(self):
        # It has non int keys, thus will make it a dict
       self.counts = {}
       self.mode = None
       self.most = 0
       self.n = 0
       self.ent = None

    # bulk add to sym
    def syms(self, t, f = None):
        f = lambda x:x
        # make an object of Sym class. ?? sym() works as a constructor
        s = Sym()
        for x in t:
            # ?? how will f suddenly start taking parameters
            s.symInc(f(x))

        return s

    def symInc(self, x):
        if x == "?":
            return  x
        # ?? why does it mean to have _ in varible name
        # ?? forgot: check what left and right params in functions do
        self.ent = None
        self.n += 1
        old = self.counts.get(x)
        new = old and old + 1 or 1
        self.counts[x] = new
        if new > self.most:
            self.most, self.mode = new, x

        return x

    def symDec(self, x):
        self.ent = None
        if self.n > 0:
            self.n -= 1
            self.counts[x] = self.counts.get(x, 0) - 1
        return x
    # what on earth does x store, not getting anything :(

    # Computing Entropy
    # Look at formula for entropy
    def symEnt(self):
        # Checking it has not  been doen before
        if self.ent == None:
            self.ent = 0
            for n in self.counts.values():
                p = n/self.n
                self.ent = self.ent - p * math.log(p, 2)
        return self.ent


@util.O.k
def symTest():
    s = Sym().syms(['y','y','y','y','y','y','y','y','y', 'n','n','n','n','n'])
    assert(util.close(s.symEnt(), 0.9403))
    print (s.symEnt())




