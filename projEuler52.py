from itertools import permutations
from projEulerFuncs import digitize, reverseDigitize

def main():
    for i in xrange(2, 1000000):
        if i % 100 == 0:
            print i
        digitSet = set(digitize(i))

        for mult in xrange(2, 7):
            testVal = mult * i
            testSet = set(digitize(testVal))
            if not digitSet.issuperset(testSet) or not digitSet.issubset(testSet):
                break
        else:
            print i
            return i
