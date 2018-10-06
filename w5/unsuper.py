from w3.Num import Num
import math
from w5.rows import Data

from operator import itemgetter

def dump(a, sep="\t"):
    for i in a:
        print(sep.join(str(b) for b in i))


def ksort(r,k):
     r = sorted(r, key=lambda r1:r1[k])
     return r


def unsuper(data):
    rows = data.rows
    enough = pow(len(rows),0.5)


    def band(c,lo,hi):
        if lo==0:
            return ".." + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])

    def argmin(c,lo,hi):
        cut = None
        if (hi - lo > 2*enough):
            l,r = Num(), Num()
            for i in range(lo,hi+1):
                r.numInc(rows[i][c])
            best = r.sd
            for i in range(lo,hi+1):
                x = rows[i][c]
                l.numInc(x)
                r.numDec(x)
                if l.n >= enough and r.n >= enough:
                    tmp = l.numXpect(r) * 1.05
                    if tmp < best:
                        cut,best = i, tmp
        return cut


    def cuts(c,lo,hi,pre):
        txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
        cut = argmin(c,lo,hi)
        if cut:
            print(txt)
            cuts(c,lo,   cut, pre + "|.. ")
            cuts(c,cut+1, hi, pre + "|.. ")
        else:
            b= band(c,lo,hi)
            print(txt +" ("+str(b)+")")
            for r in range(lo,hi):
                rows[r][c]=b


    def stop(c,t):
        for i in range(len(t)-1,-1,-1):
            if t[i][c] != "?":
                return i
        return 0

    for c in data.indeps:
        if data.nums.get(c):
            rows = ksort(rows,c)
            #print(rows)
            most = stop(c,rows)
            #print("\n-- " + data.name[c] + str(most)+ "----------")
            cuts(c,0,most,"|.. ")
    #print(", ".join(data.name.values()))
    print(", ".join(data.name.values()).replace("$",""))
dump(rows)