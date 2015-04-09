from math import sqrt

def pentagonalNumber(n):
    return n * (3 * n -1) / 2

def main2():
    pentLst = []
    for i in xrange(1, 5000):
        pentLst.append(pentagonalNumber(i))

    pentSet = set(pentLst)
    for i in xrange(1, 3000):
        for j in xrange(i+1, 3001):
            #print i,j
            diffVal = diffFunc(i,j)
            if diffVal in pentSet:
                val1 = pentagonalNumber(i)
                val2 = pentagonalNumber(j)
                sumVal = val1 + val2
                if sumVal in pentSet:
                    return i, j, val1, val2, sumVal, diffVal

def main():
    for i in xrange(1, 3000):
        val1 = pentagonalNumber(i)
        for j in xrange(i+1, 3001):
            val2 = pentagonalNumber(j)
            sumVal = val1 + val2
            diffVal = val2 - val1
            if isPent(sumVal) and isPent(diffVal):
                print i, j, val1, val2, sumVal, diffVal
                return

def diffFunc(a, b):
    total = 0
    for i in xrange(a, b):
        total += 4 + 3 * (i - 1)
    return total

def isPent(x):
    val = (.5 + sqrt(.25 + 6 * x)) / 3
    return val - int(val) == 0
