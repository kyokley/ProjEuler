#!/usr/bin/python2.7

import projEulerFuncs
import math

divisors = projEulerFuncs.divisors
log10 = math.log10

def perfect(num):
    val = sum(divisors(num)[:-1])

    if val < num:
        return -1
    elif val > num:
        return 1
    else:
        return 0

def abundGen(abund):
    for i in abund:
        for j in abund:
            if i + j > 28124:
                break
            yield i+j

def main():
    abund = []
    upperBound = 28124
    blah = set()
    for i in xrange(upperBound):
        if perfect(i) == 1:
            abund.append(i) 

    valSet = set()
    for i in abundGen(abund):
        valSet.add(i)

    for i in xrange(upperBound):
        if i not in valSet:
            blah.add(i)

    print sum(blah)

if __name__ == "__main__":
    main()
