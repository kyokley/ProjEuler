#!/usr/bin/python

import projEulerFuncs

savedPrimes = projEulerFuncs.savedPrimes
isPrime = projEulerFuncs.isPrime

def diag():
	val = 1
	yield val
	
	sideLength = 2

	while 1:
		for i in xrange(4):
			val += sideLength
			yield val
		sideLength += 2	

def main():
	count = 1
	ratio = 1
	primes = 0
	diags = diag()
	diags. next()
	while ratio >= .1:
		for i in xrange(4):
			testNum = diags.next()
			count += 1
			if isPrime(testNum):
				primes += 1
			#print testNum, isPrime(testNum)
		ratio = float(primes) / float(count)
		sideLength = count / 2 + 1
		print ratio, sideLength
	
	print ratio, count, sideLength	

if __name__ == "__main__":
	main()
