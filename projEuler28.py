#!/usr/bin/python

def diag():
	val = 1
	yield val
	
	sideLength = 2

	while 1:
		for i in xrange(4):
			val += sideLength
			yield val
		sideLength += 2	

if __name__ == "__main__":
	main()
