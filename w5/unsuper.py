from w5.dom import Data
from w3.num import Num
import util
def unsuper(data):
    rows = data.rows
    enough = len(rows) ** 0.55

    def band(c, lo, hi):
        if lo == 1:
            return ".." + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        if (hi - lo > 2 * enough):
            l, r = Num(0), Num(0)
            for i in range(lo, hi + 1):
                r.numInc(rows[i][c])
            best = r.sd
            for i in range(lo, hi + 1):
                x = rows[i][c]
                l.numInc(x)
                r.numDec(x)
                if l.n >= enough and r.n >= enough:
                    tmp = Num.numXpect(l, r) * 1.04
                    if tmp < best:
                        cut, best = i, tmp
        return cut


    def cuts(c, lo, hi, pre):
        txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
        cut = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut + 1, hi, pre + "|.. ")
        else:
            b = band(c, lo, hi)
            print(txt + " (" + b + ")")
            for r in range(lo, hi + 1):
                rows[r][c] = b


    def stop(c, t):
        for i in range(len(t) - 1, -1, -1):
            if t[i][c] != "?": return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows = sorted(rows.values(), key=lambda x:x[c])
            most = stop(c, rows)
            print("\n---------- Output ----------")
            cuts(c, 0, most, "|.. ")
    print("\n")
    title = data.name
    # title = ' '.join(str(title))
    print(title)
    for s in rows:
        print(*s)


@util.O.k
def testUnsuper():
    # print("WeatherLong.csv")
    d1 = Data()
    print ("weatherLong results")
    d1.readerRows("../w4/weatherLong.csv")
    unsuper(d1)
    # unsuper(x)