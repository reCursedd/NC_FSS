#A Gaussian sampler incrementally updated means and standard deviations.
# Followed by the test function
from w3.sample import Sample
import util
import math
class Num:

    def __init__(self, max):
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = 10**32
        self.hi = -1*10**32
        self.some = Sample(max)
        self.w = 1

        # Some kind of bulk add :/
    def nums(self, t):
        f = lambda x: x
        # CheckPoint
        n = Num(0)
        for x in t:
            n.numInc(f(x))
        return n


    # -- where does 'd' come in from :'(
    def numInc(self, x):
        if x == "?":
            return x

        self.n = self.n + 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu += d/self.n
        self.m2 += d*(x - self.mu)
        if x > self.hi:
            self.hi = x

        if x < self.lo:
            self.lo = x

        if (self.n >= 2):
            self.sd = math.pow(self.m2/(self.n - 1 + 10**(-32)), 0.5)
            print(self.sd)
        return x

    def numDec(self, x):
        if (x=="?"):
            return x

        if (self.n == 1):
            return x

        self.n = self.n - 1
        d = x - self.mu
        self.mu -= d/self.n
        self.m2 -= d*(x-self.mu)
        if (self.n >= 2):
            self.sd = (self.m2/(self.n -1 + 10**32))**0.5

        return x

    # Why do we need to normalize
    def numNorm(self, x):
        if x == "?":
            a = 0.5
        else:
            a = (x-self.lo) / (self.hi - self.lo + 10**32)
        return a

    def numMedian(self):
        return Sample.nth(self.some, 0.5)

    def numXpect(self, i):
        n = self.n + i.n + 0.0001
        return self.n/n * self.sd + i.n/n * i.sd

@util.O.k
def numTest():
    n = Num(520).nums([4,10,15,38,54,57,62,83,100,100,174,190,215,225, 233,250,260,270,299,300,306,333,350,375,443,475, 525,583,780,1000])
    print (n.mu)
    assert(util.close(n.mu, 270.3))
    assert(util.close(n.sd, 231.946))