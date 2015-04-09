#!/usr/bin/python

import projEulerFuncs

savedPrimes = projEulerFuncs.savedPrimes
isPrime = projEulerFuncs.isPrime
permuteRec = projEulerFuncs.permuteRec

def convertToList(num):
	strNum = str(num)
	lst = [int(x) for x in strNum]
	return lst

def convertFromList(lst):
	tempStr = ""
	for i in lst:
		tempStr += str(i)

	return int(tempStr)

def rotateLst(num):
	lst = []
	strNum = str(num)

	for i in xrange(len(strNum)):
		newStr = ""
		for j in xrange(i, i + len(strNum)):
			idx = j
			if idx >= len(strNum):
				idx -= len(strNum)
			newStr += strNum[idx]
		lst.append(int(newStr))
	return lst

def binary_search(x, lst):
	if x > lst[-1]:
		return False
	elif x < lst[0]:
		return False

	if x == lst[0] or x == lst[-1]:
		return True
	
	if len(lst) == 1:
		if x == lst[0]:
			return True
		else:
			return False
	else:
		mid = len(lst)/2
		if x < lst[mid]:
			return binary_search(x, lst[:mid])
		elif x > lst[mid]:
			return binary_search(x, lst[mid+1:])
		else:
			return True

def binary(x, lst):
	upper = len(lst)
	lower = 0

	while upper > lower:
		mid = (upper + lower) / 2

		if x == lst[mid]:
			return mid
		elif x < lst[mid]:
			upper = mid - 1		
		elif x > lst[mid]:
			lower = mid + 1
	else:
		return None

def main():
	circPrimes = []
	testPrimes = savedPrimes[:]
	for i in xrange(len(testPrimes)):
		if i >= len(testPrimes):
			break

		if not testPrimes[i]:
			continue
		
		print testPrimes[i]

		rots = rotateLst(testPrimes[i])

		for j in rots:
			if not binary_search(j, savedPrimes):
				break
		else:
			circPrimes += rots

		for k in rots:
			try:
				idx = binary(k, testPrimes)
				if idx:
					testPrimes[idx] = 0
			except:
				pass

	circPrimes = [i for i in circPrimes if i < 10**6]

	for i in circPrimes:
		print i

	print len(circPrimes)

	return circPrimes

if __name__ == "__main__":
	main()
