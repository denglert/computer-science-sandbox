#!/usr/bin/env python


import math

original_amount = 300
#coins = [1, 2, 5]
coins = [10, 5, 2, 1]

#original_amount = 500
#coins = [1, 2, 5, 10, 20, 50, 100, 200]

nCoins = len(coins)

combinations = 0

def check_configuration(amount, iCoin):

    global combinations

    coin = coins[iCoin]

    max_multiplier = int(math.floor(amount/coin))
    if max_multiplier == 0: return False


    for multiplier in range(max_multiplier+1):


        remaining_amount = amount - multiplier*coin

        if remaining_amount < 0:
            break
        elif remaining_amount == 0:

            combinations += 1
            break



        new_iCoin = iCoin + 1

        if new_iCoin == nCoins:
            continue 
        if new_iCoin > nCoins:
            break
        else:
            check_configuration(remaining_amount, new_iCoin)

check_configuration(original_amount, 0)

print("Total combinations: {}".format(combinations))





#   print("Recursion level: {} ||| Current amount: {} coin: {} max_multiplier: {}".format(iCoin, amount,
#       coin, max_multiplier))

#       print("Multiplier: {}".format(multiplier))
#
##       print("Remaining amount: {}".format(remaining_amount))
#
#       if iCoin == 2:
#           print('iCoin: {} max_multiplier: {} multiplier: {} remaining_amount: {}'.format(iCoin,
#               max_multiplier, multiplier,
#               remaining_amount))



#           print("Found one!".format(remaining_amount))
