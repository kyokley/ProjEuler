

from projEulerFuncs import (savedPrimes,
                            reverseDigitize,
                            digitize,
                            )
from itertools import permutations

def main():
    fourDigitPrimes = [i for i in savedPrimes if 1000 < i < 9999]
    fourDigitPrimeSet = set(fourDigitPrimes)
    for i in fourDigitPrimes:
        perms = [reverseDigitize(x) for x in permutations(digitize(i))]
        perms = list(set([x for x in perms if x in fourDigitPrimeSet]))

        if len(perms) < 3:
            continue

        perms = sorted(perms)

        if checkArithSeq(perms):
            print perms

def checkArithSeq(nums):
    for key, val in enumerate(nums):
        for refVal in nums[key + 1:]:
            diff = refVal - val
            testVal = refVal + diff
            if testVal in nums:
                print '%s%s%s' % (val, refVal, testVal)
                return True
    return False

