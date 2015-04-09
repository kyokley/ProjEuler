from itertools import permutations
from projEulerFuncs import digitize, reverseDigitize

def main():
    testedSet = set()
    for i in xrange(300, 10000):
        if i % 100 == 0:
            print i
        cubeVal = i**3
        cubeDigits = tuple(digitize(cubeVal))
        perms = set([x for x in permutations(cubeDigits) if x > cubeDigits])
        if perms.intersection(testedSet):
            testedSet = testedSet.union(perms)
            print '%s skipped' % (i,)
            continue

        successes = 0
        for perm in perms:
            if perm in testedSet:
                print '%s skipped' % (i,)
                break
            else:
                testedSet.add(perm)

            perm = reverseDigitize(perm)
            if isCubeRoot(perm):
                successes += 1

        if successes == 5:
            print cubeVal
            return cubeVal

def isCubeRoot(num):
    val = num ** (1/3.0)
    intVal = int(val)
    return val == intVal
