#!/usr/bin/python

alphaVal = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26,'"':0}

def nameVal(name):
	result = 0
	
	for i in name:
		result += alphaVal[i]

	return result

def main():
	names = open("names.txt").read()
	names = str.split(names,",")
	names = map(lambda x : x.strip('"'), names)
	names = sorted(names)
	vals = []

	for i in xrange(len(names)):
		vals.append((names[i],i+1))

	vals = [(nameVal(x[0]),x[1]) for x in vals]
	vals = map(lambda x:x[0] * x[1], vals)
	val = sum(vals)

	print val		

if __name__ == "__main__":
	main()
