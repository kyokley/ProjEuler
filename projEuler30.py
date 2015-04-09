#!/usr/bin/python

import math

def digitize(s):
	result=[]
	numString = str(s)
	for i in numString:
		result.append(int(i))
	return result

def pow(num):
	return math.pow(num,5)

def powList(s):
	return map(pow,s)

def sumList(s):
	return map(sum,s)

def main():
	#i=0
	#while i < 1000:
	result = []
	upperBound = 1000000
	lowerBound = 0
	nums1 = range(lowerBound, upperBound)
	nums2 = range(lowerBound, upperBound)
	numsLists = map(digitize,nums1)
	powLists = map(powList,numsLists)
	nums1 = map(sum, powLists)
	#print sumLists	
	for i in range(lowerBound, upperBound):
		if int(nums1[i-lowerBound]) == nums2[i-lowerBound]:
			result.append(nums2[i])

	print result
	print sum(result[2:]) 

if __name__=="__main__":
	main()
