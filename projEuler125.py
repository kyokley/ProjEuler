#!/usr/bin/python

import projEulerFuncs
import math

sqrt = math.sqrt
squareSum = projEulerFuncs.squareSum
palindrome = projEulerFuncs.palindrome

def main():
	nums = []

	for i in xrange(1, 10**8):
		if palindrome(i) and squareSum(i):
			nums.append(i)

	print sum(nums)		

if __name__ == "__main__":
	main()
