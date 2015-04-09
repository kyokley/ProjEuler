#!/usr/bin/python

import math

floor = math.floor

def probs():
	r = 2 * 10**11
	b = 6 * 10**11
	
	while 1:
		prob = discs(b, r)
		print prob
		diff = prob - .5
		if diff > .0000001:
			r += floor(b * diff) 
		elif diff < .4999999:
			b += floor(abs(r * diff))
		else:
			if prob > .5:
				r += 1
			elif prob < .5:
				b += 1
			else:
				yield (b,r)
				b += 1
				r += 1

def discs(inB, inR):
	b = float(inB)
	r = float(inR)
	return b*(b-1)/((b+r)*(b+r-1))

def main():
	discs(15.0,6.0)

if __name__ == "__main__":
	main()
