#!/usr/bin/python

import projEulerFuncs

divisors = projEulerFuncs.divisors

def d(num):
	return sum(divisors(num)[:-1])

def main():
	pairs = []

	for i in xrange(10000):
		if i in pairs:
			continue

		testNum = d(i)
	
		if i == testNum:
			continue
	
		if d(testNum) == i:
			print testNum, i
			pairs.append(testNum)
			pairs.append(i)

	print sum(pairs)

if __name__ == "__main__":
	main()
