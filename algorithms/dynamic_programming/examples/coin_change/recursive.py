#!/usr/bin/env python

import sys

sys.setrecursionlimit(1000000)

#coins   = [100.0, 50.0, 1.0]
coins   = [200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0]

combinations = 0

nCalls = 0

def step(remaining, iCoin):
    
    global combinations
    global nCalls
    nCalls = nCalls + 1

    if remaining < 0:
#       print("Remaining amount less than zero. No bueno.")
        return False

    if remaining == 0:
#       print("Found a good combination. iCoin: {}".format(iCoin))
        combinations += 1
        return True

    if iCoin >= len(coins):
#       print("Out of bounds")
        return False


    max_factor = int(remaining/coins[iCoin])

#   print("At Coin level: {} Remaining: {}, Max factor: {}".format(coins[iCoin], remaining, max_factor))

    for j in range(max_factor+1):
#       if iCoin == 0:
#           print(j)
        step(remaining-j*coins[iCoin], iCoin+1)
    

amount = 500.0
step(amount, 0)

print("Combinations: {}".format(combinations))
print("nCalls: {}".format(nCalls))


# - Combinations: 6295434
# - nCalls: 519629481
