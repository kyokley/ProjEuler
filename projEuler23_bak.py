#!/usr/bin/python

import projEulerFuncs
import math
import pdb

divisors = projEulerFuncs.divisors
log10 = math.log10
bsInsert = projEulerFuncs.bsInsert
bsContains = projEulerFuncs.bsContains
bsIndex = projEulerFuncs.bsIndex
trace = pdb.set_trace()

def sumFrom(num, lst):
	testLst = [x for x in lst if log10(x) <= log10(num)+1 and log10(x) >= log10(num)-1]

	for i in testLst:
		for j in [x for x in testLst if i + x <= num]:
			if i + j == num:
				return True
	else:
		return False
	

def perfect(num):
	val = sum(divisors(num)[:-1])

	if val < num:
		return -1
	elif val > num:
		return 1
	else:
		return 0

def main():
	abund = []
	trace()
	upperBound = 30
	vals = range(upperBound)
	blah = []
	for i in xrange(upperBound):
		if perfect(i) == 1:
			abund.append(i)	

		
	for i in abund:
		for j in abund:
			print i+j,len(blah)
			if j > i:
				break

			#if i + j > upperBound:
			#	break

			if bsIndex(i+j, blah):
				continue
			else:
				bsInsert(i+j, blah) 

	print sum(vals)-sum(blah)

if __name__ == "__main__":
	main()
