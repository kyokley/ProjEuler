#!/usr/bin/python

import projEulerFuncs
digitize = projEulerFuncs.digitize

def ones(num):
	vals = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
	return vals[num]

def tens(num):
	digitLst = digitize(num)
	vals = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

	vals2 = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}

	if len(digitLst) == 1:
		return ones(digitLst[0])

	if digitLst[0] == 1:
		return vals[num]

	return vals2[digitLst[0]] + ones(digitLst[1])	

def hundreds(num):
	digitLst = digitize(num)

	val = {1:"onehundredand",2:"twohundredand",3:"threehundredand",4:"fourhundredand",5:"fivehundredand",6:"sixhundredand",7:"sevenhundredand",8:"eighthundredand",9:"ninehundredand"}

	return val[digitLst[0]] + tens(num % 100)

def letters(num):
	digitLst = digitize(num)
	funcs = {1:ones,2:tens,3:hundreds}
	
	return funcs[len(digitLst)](num)

def main():
	print "blah"

if __name__ == "__main__":
	main()
