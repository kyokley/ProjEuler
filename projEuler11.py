#!/usr/bin/python

def pos(x,y):
	if x<0 or x>=20:
		return -1
	if y<0 or y>=20:
		return -1
	return x + 20 * y

def prod(lst):
	result =1
	for i in lst:
		result *= i
	return result

def main():
	lines = open("grid.txt").read().splitlines()
	blah = [x.split(" ") for x in lines]
	grid = [int(y) for x in blah for y in x]
	
	largest = 0

	for i in range(20):
		for j in range(20):
			right=[]
			down=[]
			dr=[]
			dl=[]
			for k in range(4):
				if pos(i+k,j) >= 0:
					right.append(grid[pos(i+k,j)])
				else:
					right.append(0)
				if pos(i,j+k)>=0:
					down.append(grid[pos(i,j+k)])
				else:
					down.append(0)
				if pos(i+k,j+k)>=0:
					dr.append(grid[pos(i+k,j+k)])
				else:
					dr.append(0)
				if pos(i-k,j+k)>=0:
					dl.append(grid[pos(i-k,j+k)])
				else:
					dl.append(0)
			rightProd = prod(right)
			downProd = prod(down)
			drProd = prod(dr)
			dlProd = prod(dl)
			largest = max(largest, rightProd, downProd, drProd, dlProd)
	print largest	

if __name__=="__main__":
	main()
