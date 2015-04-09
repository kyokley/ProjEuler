#!/usr/bin/python2.7

import math
from projEulerFuncs import print_timing

def main():
    res1 = listPowers()
    res2 = setPowers()
    print res1, res2

@print_timing
def listPowers():
	upperBound = 101
	lowerBound = 2
	results = []

	for i in range(lowerBound, upperBound):
		for j in range(lowerBound, upperBound):
			power = math.pow(i,j)
			if not power in results:
				results.append(power)
	
	return len(results)

@print_timing
def setPowers():
	upperBound = 101
	lowerBound = 2
	results = set()

	for i in range(lowerBound, upperBound):
		for j in range(lowerBound, upperBound):
			power = math.pow(i,j)
			if not power in results:
				results.add(power)
	
	return len(results)


if __name__ == "__main__":
	main()
