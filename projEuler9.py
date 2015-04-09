#!/usr/bin/python

import math

def pythag(a, b):
	c = math.sqrt(a*a + b*b)
	if c == math.floor(c):
		return 1
	else:
		return 0

def main():
	found = 0
	for i in range(1, 1000):
		if found == 1:
			break
		else:
			for j in range(1, 1000-i):
				print '%d, %d' % (i,j)
				if pythag(i,j) == 1:
					k = math.sqrt(i*i + j*j)
					if i+j+k==1000:
						print '%d,%d,%d->%d' % (i,j,k,i*j*k)
						found = 1
						break	

if __name__ == '__main__':
	main()
