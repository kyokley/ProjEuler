#!/usr/bin/python

import math
import projEulerFuncs
import timeit

flatten = projEulerFuncs.flatten
sqrt = math.sqrt
time = timeit.time

def rowFunc(num):
	return math.floor(1+(-1+sqrt(1+8*num))/2)

class Node:
	def __init__(self, num, idx, tree):
		self.data = num
		self.index = idx
		self.tree = tree
		self.maxVal = -1

	def getMaxVal(self):
		if self.maxVal != -1:
			return self.maxVal
		else:
			if not self.left() and not self.right():
				self.maxVal = self.data
			else:
				if not self.left():
					self.maxVal = self.right().getMaxVal() + self.data
				elif not self.right():
					self.maxVal = self.left().getMaxVal() + self.data
				else:				
					self.maxVal = max(self.left().getMaxVal(), self.right().getMaxVal()) + self.data
			return self.maxVal

	def left(self):
		idxVal = rowFunc(self.index) + self.index
		if idxVal < self.tree.getCount():
			return self.tree.nodes[int(idxVal)]
		else:
			return None

	def right(self):
		idxVal = rowFunc(self.index) + self.index + 1
		if idxVal < self.tree.getCount():
			return self.tree.nodes[int(idxVal)]
		else:
			return None

	def display(self):
		print self.data
					

class Tree:
	nodes = []

	def addNode(self, num):
		self.nodes.append(Node(num,self.getCount(),self))

	def getCount(self):
		return len(self.nodes)

	def printAll(self):
		for i in self.nodes:
			i.display()	

def main():
	lines = open("triangle.txt").read().splitlines()
	lines = [x.split(" ") for x in lines]
	lines = flatten(lines)
	lines = [int(x) for x in lines]

	tree = Tree()
	
	for x in lines:
		tree.addNode(x)

	start = time.time()
	print tree.nodes[0].getMaxVal()
	elapsed = time.time() - start
	print elapsed


if __name__ == "__main__":
	main()
