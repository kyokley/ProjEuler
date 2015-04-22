#!/usr/bin/python2.7

import math
import time
import os

pythonDir = os.getcwd()
sqrt = math.sqrt
fact= math.factorial
savedPrimes = [int(x) for x in open(os.path.join(pythonDir, "primes.txt")).read().splitlines()]
savedPrimesSet = set(savedPrimes)

def infCounter():
    x = 0
    while 1:
        x += 1
        yield x

def genLength(gen):
    count = 0

    try:
        while 1:
            gen.next()
            count += 1
    except:
        return count

def nCr(n,r):
    return fact(n) / (fact(r)*fact(n-r)) 

def diagSpiral():
    val = 1
    yield val

    sideLength = 2

    while 1:
        for i in xrange(4):
            val += sideLength
            yield val
        sideLength += 2

def isPrime(num):
    if num < savedPrimes[-1]:
        #return bsContains(num, savedPrimes)
        return num in savedPrimesSet
    else:
        if genLength(factor(num)) == 1:
            return True
        else:
            return False

#NOTE: lst must be sorted first!
#def bsContains(x, lst):
    #if not lst:
        #return False
#
    #if x > lst[-1]:
        #return False
    #elif x < lst[0]:
        #return False
#
    #if x == lst[0] or x == lst[-1]:
        #return True
#
    #if len(lst) == 1:
        #if x == lst[0]:
            #return True
        #else:
            #return False
    #else:
        #mid = len(lst) / 2
        #if x < lst[mid]:
            #return bsContains(x, lst[:mid])
        #elif x > lst[mid]:
            #return bsContains(x, lst[mid+1:])
        #else:
            #return True

#NOTE: lst must be sorted first!
#def bsIndex(x, lst):
    #if not lst:
        #return None
#
    #upper = len(lst)
    #lower = 0
#
    #while upper > lower:
        #mid = (upper + lower) / 2
#
        #if x == lst[mid]:
            #return mid
        #elif x < lst[mid]:
            #upper = mid - 1
        #elif x > lst[mid]:
            #lower = mid + 1
    #else:
        #return None
#
#def bsInsert(x, lst):
    #if not lst:
        #lst.append(x)
        #return
#
    #if x < lst[0]:
        #lst.insert(0, x)
        #return
    #elif x > lst[-1]:
        #lst.append(x)
        #return
#
    #upper = len(lst)
    #lower = 0
    #mid = 0 
#
#
    #while upper > lower:
        #mid = (upper + lower) / 2
#
        #if x == lst[mid]:
            #lst.insert(mid, x)
            #return
        #elif x < lst[mid]:
            #upper = mid - 1
        #elif x > lst[mid]:
            #lower = mid + 1
#
        #if upper == lower:
            #lst.insert(upper, x)
    #else:
        #mid = (upper + lower) / 2
        #if x < lst[mid - 2]:
            #lst.insert(mid - 2, x)
        #elif x < lst[mid - 1]:
            #lst.insert(mid - 1, x)
        #elif x < lst[mid]:
            #lst.insert(mid, x)
        #elif x < lst[mid + 1]:
            #lst.insert(mid + 1, x)
        #else:
            #lst.insert(mid + 2, x)

def factor(n):  
    yield 1  
    i = 2  
    limit = n**0.5  
    while i <= limit:  
        if n % i == 0:  
            yield i  
            n = n / i  
            limit = n**0.5  
        else:  
            i += 1  
    if n > 1:  
        yield n

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return (a * b) / gcd(a, b)

def carmichael(n):
    def dictify(gen):
        factors = dict()
        for i in gen:
            if i == 1:
                continue

            if i in factors.keys():
                factors[i] += 1
            else:
                factors[i] = 1
        return factors
    factors = dictify(factor(n))
    return carmichaelHelper(factors)

def carmichaelHelper(pDict):
    if len(pDict) == 1:
        p = pDict.keys()[0]
        if p == 2 and pDict[p] > 2:
            return 2 ** (pDict[p] - 2)
        else:
            return (p ** (pDict[p] - 1)) * (p - 1)
    else:
        return reduce(lambda x,y: lcm(x,y), [carmichaelHelper(dict({p:a})) for p,a in pDict.items()])

def flatten(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

def squareSum(num):
    upperBound = math.ceil(sqrt(num))

    for i in xrange(1, int(upperBound)):
        tempSum = 0
        for j in xrange(i, int(upperBound)):
            tempSum += j**2
            if tempSum > num:
                break
            elif tempSum == num:
                return True
    else:
        return False

def permuteRec(lst):
    result = [lst[:]]
    if len(lst)>1:
        tempVal = lst[0]
        for i in permuteRec(lst[1:]):
            if not i:
                continue

            for idx in xrange(len(i) + 1):
                newElem = i[:]
                newElem.insert(idx, tempVal)
                if newElem in result:
                    continue
                result.append(newElem)
                
    return result   

def permute(lst, num):
    bak = lst[:]
    bak = sorted(bak)
    
    return _permute(lst, num)

def _permute(lst, num):
    if num == 0:
        return lst
    else:
        infCount = infCounter()
        done = False
        largestVal = 0
        temp = 1
        while not done:
            temp *= infCount.next()

            if temp > num:
                done = True
                largestVal = infCount.next() - 2
                break
            
        candidates = lst[-(largestVal+1):]
        multiple = int(math.floor(float(num)/fact(largestVal)))
        oldVal = lst[-(largestVal+1)]
        newVal = candidates[multiple]
        lst[-(largestVal+1)] = newVal
        lst[multiple-(largestVal+1)] = oldVal
        lst[-largestVal:] = sorted(lst[-largestVal:])
        return _permute(lst, num - fact(largestVal) * multiple)
        

def subset(lst):
    sets = []
    if len(lst) == 1:
        sets.append(lst)
        sets.append([])
    else:
        sets = subset(lst[1:])
        for i in subset(lst[1:]):
            sets.append([lst[0]] + i)
    return sets

def subsetGen(lst):
    if len(lst) == 1:
        yield lst
        yield []
    else:
        for i in subsetGen(lst[1:]):
            yield i

        for i in subsetGen(lst[1:]):
            yield ([lst[0]] + i)

def unique(lst):
    return list(set(lst))

def divisors(num, sort=True):
    factors = [x for x in factor(num)]
    divisors = subset(factors)
    
    divisors = [reduce(lambda x,y:x*y,i) for i in divisors if i]
    divisors = unique(divisors)

    if sort:
        return sorted(divisors)         
    else:
        return divisors

def digitize(num):
    result = []
    numStr = str(num)
    for i in numStr:
        result.append(int(i))
    return result

def digitalSum(num):
    digits = digitize(num)
    return sum(digits)

def reverseDigitize(digits):
    numStr = ""
    for i in xrange(len(digits)):
        numStr += str(digits[i])
    return int(numStr)

def pythagoreanTriple(a,b):
    c = math.hypot(a,b)
    if c == math.floor(c):
        return (True, c)
    else:
        return (False, c)

def palindrome(num):
    numStr = digitize(num)
    length = len(numStr)
    for i in range(int(math.floor(length/2.0))):
        if numStr[i] != numStr[-(i+1)]:
            return False
    return True

def isPandigital(lst):
    if len(lst) != 9:
        return False
    
    if isinstance(lst, int):
        lst = str(lst)

    for i in xrange(1,10):
        if not str(i) in lst:
            return False
    else:
        return True

    #for i in xrange(1,10):
    #   if sortedList[i-1] != i:
    #       return False
    #else:
    #   return True

def fibonacci(upperBound):
    results=[]
    a,b = 0,1
    while a < upperBound:
        a,b = b,a+b
        results.append(a)
    return results

def fibGen():
    a,b=0,1
    while True:
        a,b = b, a+b
        yield a

def _getPrimesHelper(test, lst):
    sqrVal = test**2
    valLst = lst[:]

    for i in xrange(len(lst)-1,-1,-1):
        if lst[i] < sqrVal:
            continue
        else:
            if valLst[i] % test == 0:
                valLst.pop(i)

    return valLst

def getPrimes(upperBound, lst=[]):
    if not lst: 
        ints = range(upperBound,1,-1)
        primes = []
    else:
        if lst[-1] > upperBound:
            return lst
        ints = range(upperBound,lst[-1],-1)
        primes = lst[:]
        for i in primes:
        #   print i
            ints = _getPrimesHelper(i, ints)
    
    while len(ints) > 0:
        testPrime = ints.pop()
        #print testPrime
        ints = _getPrimesHelper(testPrime, ints)
        primes.append(testPrime)
    if len(primes) > len(savedPrimes):
        f = open("primes.txt","w")
        for i in primes:
            f.writelines(str(i) + "\n")
        f.close()
    return primes

def phi(num):
    testNum = 1
    count = 1
    prod = 1
    factors = factor(num)
    factors.next()
    testNum = factors.next()
    for i in factors:
        if i == testNum:
            count += 1
        else:
            prod *= (testNum**count - testNum**(count-1))
            testNum = i
            count = 1
    else:
        prod *= (testNum**count - testNum**(count-1))

    blah = savedPrimesSet
    #primes = savedPrimes
        
    if prod == num - 1:
        if not num in blah:
            blah.add(num)
    return prod

def updatePrimes():
    primes = [int(x) for x in open("primes.txt").read().splitlines()]
    if len(savedPrimes) > len(primes):
        f = open("primes.txt","w")
        for i in savedPrimes:
            f.writelines(str(i) + "\n")
        f.close()

def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
    start = time.time()
    getPrimes(1000000, lst=savedPrimes)
    elapsed = time.time() - start
    print elapsed

if __name__ == "__main__":
    main()
