#!/usr/bin/python

import projEulerFuncs

pandigital = projEulerFuncs.pandigital
digitize = projEulerFuncs.digitize
fibGen = projEulerFuncs.fibGen

def fibGenShort():
	a,b=0,1
	while True:
		a,b = b, (a+b) % 1000000000
		yield a

def main():
	genShort = fibGenShort()
	gen = fibGen()
	count = 0
	count2 = 0
	candidates = []
	#while True:
	for i in xrange(1,5000000):
		count += 1
		print count
		testNum = genShort.next()
		actualNum = gen.next()
	#	if count < 275000:
	#		continue

		strNum = str(testNum)	
	
	#	if len(strNum) < 9:
	#		continue
	
	#	first = strNum[:9]
	#	last = strNum[-9:]
		
	#	if count % 2**7 == 0:
	#		print count, first, last, len(strNum)
		
	#	if "0" in first or "0" in last:
	#		continue		

		if "0" in strNum:
			continue		

		if pandigital(strNum):
			strNum2 = str(actualNum)[:9]
			if pandigital(strNum2):
				count2 = count
				break
	
	print candidates
	print count2

if __name__ == "__main__":
	main()
