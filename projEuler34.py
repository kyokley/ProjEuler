#!/usr/bin/python

import math

def digitize(num):
	result=[]
	numStr = str(num)
	for i in numStr:
		result.append(int(i))

	return result

def factList(s):
	return map(math.factorial,s)

def main():
	results = []
	upperBound = 10000000
	nums1 = range(upperBound)
	nums2 = range(upperBound)
	digitLists = map(digitize, nums1)
	factLists = map(factList, digitLists)
	nums1 = map(sum,factLists)
	#print sumLists
	for i in range(upperBound):
		if nums1[i] == nums2[i]:
			results.append(nums1[i])

	print results 
	print sum(results[2:])	

if __name__ == "__main__":
	main()
