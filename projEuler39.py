#!/usr/bin/python

import projEulerFuncs

pythaTriple = projEulerFuncs.pythagoreanTriple

def rank(tup):
	return tup[1]

def main():
	upperBound = 1000
	results=[]
	for i in range(1,upperBound+1):
		count = 0
		for a in range(1,i):
			tmp = min(a,i-a)
			for b in range(1,tmp):
				(x,y) = pythaTriple(a,b)
				if x:
					if a + b + y == i:
						count += 1
		results.append((i,count))
	ranked = sorted(results,key=rank,reverse=True)
	print ranked
	print ranked[0]	

if __name__ == "__main__":
	main()
