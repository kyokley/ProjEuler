from projEulerFuncs import savedPrimes, isPrime

def main():
    res = []
    for prime in savedPrimes[4:]:
        subsets = _orderedSubSet(prime)
        for num in subsets:
            if not isPrime(num):
                break
        else:
            res.append(prime)
    print res

def _orderedSubSet(lst):
    # Return ordered subsets both forward and backwards
    if isinstance(lst, int):
        lst = str(lst)
    res = []
    for i in xrange(1, len(lst)):
        res.append(int(lst[i:]))
        res.append(int(lst[:-i]))
    return res
