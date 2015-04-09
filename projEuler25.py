#!/usr/bin/python

def main():
	a,b = 0,1
	count=0
	while len(str(a)) < 1000:
		count+=1
		a,b = b,a+b
		#print "%i - %i" % (a, count)

	print count
		


if __name__ == '__main__':
	main()
