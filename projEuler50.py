from projEulerFuncs import rwh_primes

def hasSumOfPrimes(num, primeTup=None):
    primes = primeTup[0]
    primeSet = primeTup[1]
    upperIndex = _findBoundIndex(num / 2, primeTup=primeTup)
    lowerIndex = 0
    while upperIndex > lowerIndex:
        pList = primes[lowerIndex:upperIndex]
        sumVal = sum(pList)
        if sumVal in primeSet:
            return (num, len(pList), pList, sum(pList))
        else:
            lowerIndex += 1
    else:
        return False

def _findBoundIndex(num, primeTup=None):
    primes = primeTup[0]
    for key, val in enumerate(primes):
        if val > num:
            return key - 1

def main(numPrimes):
    maxValues = None
    primes = rwh_primes(numPrimes)
    primeSet = set(primes)
    for prime in primes:
        values = hasSumOfPrimes(prime, primeTup=(primes, primeSet))
        if values:
            if maxValues:
                if values[1] > maxValues[1]:
                    maxValues = values
            else:
                maxValues = values

    print maxValues
