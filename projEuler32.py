from projEulerFuncs import isPandigital, reverseDigitize
from itertools import permutations

def main():
    digits = [int(x) for x in '123456789']
    perms = permutations(digits)

    validProducts = set()
    for perm in perms:
        multiplicand = reverseDigitize([perm[0], perm[1]])
        multiplier = reverseDigitize([perm[2], perm[3], perm[4]])
        product = reverseDigitize([perm[5],
                                   perm[6],
                                   perm[7],
                                   perm[8],
                                   ])
        if multiplicand * multiplier == product:
            validProducts.add(product)

        multiplicand = reverseDigitize([perm[0]])
        multiplier = reverseDigitize([perm[1], perm[2], perm[3], perm[4]])
        product = reverseDigitize([perm[5],
                                   perm[6],
                                   perm[7],
                                   perm[8],
                                   ])
        if multiplicand * multiplier == product:
            validProducts.add(product)
    print sum(validProducts)
    return sum(validProducts)
