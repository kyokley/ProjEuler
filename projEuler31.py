#!/usr/bin/python

vals = (1, 2, 5, 10, 20, 50, 100, 200)
coins = {}
coins[1] = 0
coins[2] = 0
coins[5] = 0
coins[10] = 0
coins[20] = 0
coins[50] = 0
coins[100] = 0
coins[200] = 0

class Sack(object):

    def __init__(self, val=200, coins=None):
        self.coins = {}
        if not coins:
            self.coins = coins
        else:
            for i in xrange(len(vals)):
                self.coins[i] = val

    def maxCoin(self, val):
        eligibleCoins = dictFilter(self.coins, lambda x : x > 0)
        coinVals = sorted(eligibleCoins.keys(), reverse=True)
        for i in xrange(len(coinVals)):
            if coinVals[i] <= val:
                return coinVals[i]
        else:
            return 0

class CoinSolution(object):
    pass

def generateSolution(inSack, val):
    largestCoin = inSack.maxCoin(val)
    if not largestCoin:
        return None
    

def dictFilter(inDict, func):
    outDict = {}
    for key, val in inDict.items():
        if func(val):
            outDict[key] = val
    return outDict

def dictSum(vals):
    sum = 0
    for i in vals:
        sum += i * vals[i]
    return sum

def maxCoin(val):
    for i in xrange(len(vals), 0, -1):
        if vals[i-1] < val:
            return vals[i-1]

def main():
    '''
    1. Find an initial solution
    2. Remove one of the largest coins and attempt to find another solution
    3. Continue until no more solutions can be found
    '''
    #for i in range(1,200,10):
        #print maxCoin(i)
    print maxCoin(30)

if __name__ == "__main__":
    main()
