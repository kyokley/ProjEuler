from itertools import permutations
from projEulerFuncs import savedPrimes, reverseDigitize

def main():
    total = 0
    for i in permutePandigital():
        numLst = list(i)
        if checkSubStrDiv(numLst):
            total += reverseDigitize(numLst)

    print total

def checkSubStrDiv(num):
    for i in xrange(1, 8):
        testNum = int(reverseDigitize(num[i:i+3]))
        if testNum % savedPrimes[i-1] != 0:
            return False
    else:
        return True

def permutePandigital():
    init = [int(x) for x in '1234567890']
    perms = permutations(init)
    
    for perm in perms:
        if perm[0]:
            yield perm
