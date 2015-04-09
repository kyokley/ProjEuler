#!/usr/bin/python

import projEulerFuncs

savedPrimes = projEulerFuncs.savedPrimes

def formula(a, b, num):
	return num**2 + a*num + b

def main():
	largest = (1,41,40)
	for a in range(-1000,1000):
		for b in range(-1000,1000):
			print (a,b)
			done = False
			testNum = 0
			while not done:
				if formula(a,b,testNum) in savedPrimes:
					testNum += 1
				else:
					done = True
			if testNum > largest[2]:
				largest = (a,b,testNum)
	print largest

if __name__ == "__main__":
	main()
