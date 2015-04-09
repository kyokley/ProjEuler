#!/usr/bin/python

import projEulerFuncs

digitize = projEulerFuncs.digitize
reverseDigitize = projEulerFuncs.reverseDigitize
flatten = projEulerFuncs.flatten

def concatProd(num, upperBound):
	ints = range(1,upperBound)
	prodList = []
	count = 0
	for i in ints:
		prod = num * i
		prodStr = digitize(prod)
		#print prodStr
		count += len(prodStr)
		prodList.append(prodStr)
		if count == 9:
			break
		elif count > 9:
			return 0
	prodList = flatten(prodList)
	sortedList = sorted(prodList)
	compList = range(1,10)
	for i in range(len(sortedList)):
		if compList[i] != sortedList[i]:
			return 0
	else:
		return reverseDigitize(prodList)


def main():
	nums = range(1,1000000)
	nums = [concatProd(x,10) for x in nums]
	nums = [x for x in nums if x!=0]
	for i in nums:
		print i

if __name__ == "__main__":
	main()
