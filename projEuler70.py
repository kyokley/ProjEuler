#!/usr/bin/python

import projEulerFuncs

permute = projEulerFuncs.permuteRec
phi = projEulerFuncs.phi
bsContains = projEulerFuncs.bsContains
reverseDigitize = projEulerFuncs.reverseDigitize
digitize = projEulerFuncs.digitize
savedPrimes = projEulerFuncs.savedPrimes

def main():
	results = []	
	minRatio = 1.00094
	minVal = 9983167
	for i in xrange(10**7,2,-1):
		print i, minVal, minRatio

		phiVal = phi(i)
		ratio = float(i) / phiVal	
		if ratio > minRatio:
			continue

		permuteLst = map(reverseDigitize, permute(digitize(i)))
		if bsContains(phiVal, sorted(permuteLst)):
			minRatio = ratio
			minVal = i
			results.append((i, phiVal))
			print i, phiVal, ratio

	results = sorted(results, key=lambda x:float(x[0])/float(x[1]))
	print results[0]
	projEulerFuncs.updatePrimes()

if __name__ == "__main__":
	main()
