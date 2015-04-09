#!/usr/bin/python

import projEulerFuncs

isPrime = projEulerFuncs.isPrime
permuteRec = projEulerFuncs.permuteRec
reverseDigitize = projEulerFuncs.reverseDigitize

def main():
	results = []

	for i in xrange(8, 2, -1):
		lst = permuteRec(range(1, i))
		lst = [reverseDigitize(x) for x in lst]

		for j in lst:
			if isPrime(j):
				results.append(j)

	results = sorted(results)

	for i in results:
		print i

if __name__ == "__main__":
	main()
