#!/usr/bin/python2.7
import pdb

from projEulerFuncs import savedPrimes

def main():
    vals = 0
    prevVals = 0
    primes = set(savedPrimes)
    primes.update([x**2 for x in savedPrimes])
    primes.update([x**3 for x in savedPrimes])
    primes.update([x**4 for x in savedPrimes])
    primes.update([x**5 for x in savedPrimes])
    count = 0
    #for i in xrange(1, 10**7 + 1):
    pdb.set_trace() ############################## Breakpoint ##############################
    for i in xrange(1, 25 + 1):
        if i not in primes:
            vals = len([x for x in factor(i)])
            print i, vals

            if vals == prevVals:
                count += 1
            prevVals = vals
        else:
            prevVals = 0

    print count

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

def divisors(num):
	factors = [x for x in factor(num)]
	divisors = subset(factors)
	
	divisors = set([reduce(lambda x,y:x*y,i) for i in divisors if i])

	return divisors

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

if __name__ == "__main__":
    main()
