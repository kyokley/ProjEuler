#!/usr/bin/python

import projEulerFuncs

nCr = projEulerFuncs.nCr

def main():
	count = 0
	for i in range(1,101):
		for j in range(1,i+1):
			if nCr(i,j) > 1000000:
				count+=1
	print count

if __name__ == "__main__":
	main()
