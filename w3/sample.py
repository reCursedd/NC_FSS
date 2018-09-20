# Resevoir sampler, will keep only a fixed number of data and delete data if it sees more
# Followed by the test function
from util import O
import random as rand
import math


class Sample:
    def __init__(self, max=512):
        # ---Why the default of 512 in Lean.sample.max
        # ---Where is Lean.sample.max coming from?
        self.max = max
        #self.rank = 1
        self.txt = "What is the used for"
        self.n = 0
        self.sorted = False
        self.some = []

    def sampleInc(self, x):
        self.n += 1
        now = len(self.some)
        if now < self.max:
            self.sorted = False
            self.some.append(x)
        # else, delete something in random and insert the new element
        elif rand.random() < now/self.n:
            self.sorted = False
            # ---Why is 0.5 added?
            self.some[math.floor(rand.random()*now)] = x
        # This means x got lucky :P
        return x

    def sampleSorted(self):
        if self.sorted == False:
            self.some.sort()
            self.sorted = True
        return self.some

    # To access nth percentile item
    def nth(self,n):
        s = self.sampleSorted()
        return s[min((len(s))-1, max(1, math.floor(0.5+n*(len(s)-1))))]

    def nths(self, ns = [0,1,0,3,0,5,0,7,0,9]):
        # ---where is this used?
        out = []
        # --- if the index is not used, why is pairs used?
        for n in ns:
            out.append(self.nth(n))
        return out

    def sampleLt(self, s1, s2):
        return self.nth(s1, 0.5) < self.nth(s2, 0.5)



@O.k
def sampleTest():
    rand.seed(1)
    s = []
    for i in range(5, 10):
        s.append(Sample(math.pow(2, i)))
    for i in range(1, 10000):
        y = rand.random()
        for sample in s:
            # So sample holds objects of Sample class in a list?
            # And then we are inserting something in each object, till max.
            sample.sampleInc(y)

    # Check if any of them are outside +/- 0.2 of 0.5
    for sample in s:
        print ((sample.max, sample.nth(0.5)))
        assert (0.3 < sample.nth(0.5) < 0.7)


