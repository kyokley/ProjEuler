from projEulerFuncs import rwh_primes

def main(upperBound):
    primes = rwh_primes(upperBound)
    primeSet = set(primes)
    primeLength = len(primes)

    maxChain = None
    for i in xrange(primeLength):
        partialSum = 0
        if maxChain:
            if maxChain[1] > (primeLength - i):
                continue

        for key, val in enumerate(primes[i:]):
            partialSum += val
            print partialSum
            if maxChain:
                if maxChain[1] > (primeLength - key):
                    break

            if partialSum > upperBound:
                break

            if partialSum in primeSet:
                chainLength = key + 1
                if maxChain:
                    if maxChain[1] < chainLength:
                        maxChain = (partialSum, chainLength) 
                else:
                    maxChain = (partialSum, chainLength) 


    print maxChain
