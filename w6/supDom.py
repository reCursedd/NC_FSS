# working on it

def super(data):
    rows = data.rows
    enough = len(rows) ** 0.55

    def band(c, lo, hi):
        if lo == 0:
            return ".." + str(rows[hi][c])
        # elif hi:
        #     return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        if (hi - lo > 2 * enough):
            l, r = Num(), Num()
            for i in range(lo, hi + 1): r.numInc(rows[i][c])
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
