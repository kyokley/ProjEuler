#!/usr/bin/python

alphaVals = {
            'A':1,
            'B':2,
            'C':3,
            'D':4,
            'E':5,
            'F':6,
            'G':7,
            'H':8,
            'I':9,
            'J':10,
            'K':11,
            'L':12,
            'M':13,
            'N':14,
            'O':15,
            'P':16,
            'Q':17,
            'R':18,
            'S':19,
            'T':20,
            'U':21,
            'V':22,
            'W':23,
            'X':24,
            'Y':25,
            'Z':26,
            }

triNums = set()

def wordVal(inVal):
    val = 0
    for i in inVal:
        val += alphaVals[i]
    return val

def triNum(n):
    return .5 * n * (n + 1)

def main():
    wordFile = open('words.txt')
    words = wordFile.readline()
    wordFile.close()

    words = words.split(',')
    words = map(lambda x: x.strip('"'), words)

    wordValues = map(wordVal, words)

    tri = 0
    i = 0
    while tri < 192:
        i += 1
        tri = triNum(i)
        triNums.add(tri)

    triWords = filter(lambda x: x in triNums, wordValues)
    print 'TriWords', len(triWords)

if __name__ == '__main__':
    main()
