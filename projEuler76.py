#!/usr/bin/python

from math import floor

def recSums(num):
    if num == 2:
        return 1
    else:
        return floor(num/2) + recSums(num-1)
