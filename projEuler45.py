#!/usr/bin/python

def triangle():
	n = 1

	while 1:
		yield (n * (n + 1)) / 2
		n += 1

def pentagonal():
	n = 1

	while 1:
		yield (n * (3*n - 1)) / 2
		n += 1

def hexagonal():
	n = 1
	
	while 1:
		yield n * (2*n -1)
		n += 1

def main():
	gen1 = hexagonal()
	gen2 = pentagonal()
	gen3 = triangle()

	for i in xrange(144):
		gen3.next()

	while 1:
		testNum1 = gen1.next() 
		testNum2 = gen2.next()
		testNum3 = gen3.next()

		while testNum2 < testNum1:
			testNum2 = gen2.next()

		while testNum3 < testNum1:
			testNum3 = gen3.next()

		print testNum1, testNum2, testNum3

		if testNum1 == testNum2 and testNum1 == testNum3:
			break		

if __name__ == "__main__":
	main()
