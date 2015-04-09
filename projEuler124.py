#!/usr/bin/python

import projEulerFuncs

factor = projEulerFuncs.factor
unique = projEulerFuncs.unique

def rad(num):
	factors = [x for x in factor(num)]
	factors = unique(factors)
	return reduce(lambda x,y:x*y, factors)
	
def main():
	radList = []
	upperBound = 100000

	for i in xrange(1, upperBound+1):
		radList.append((rad(i), i))

	radList = sorted(radList)

	print radList[9999]

if __name__ == "__main__":
	main()
