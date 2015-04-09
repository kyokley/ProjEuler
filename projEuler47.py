from projEulerFuncs import factor

def main():
    for i in xrange(1000000):
        if i == 4:
            pass
        print i
        for j in xrange(i, i + 4):
            if len(getPrimes(j)) != 4:
                break
        else:
            print i
            return i

def getPrimes(num):
    return set([x for x in factor(num) if x != 1])

