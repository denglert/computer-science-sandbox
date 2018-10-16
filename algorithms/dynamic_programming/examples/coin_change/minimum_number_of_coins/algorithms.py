#!/usr/bin/env python



def dp_algo(coins, amount):

    nCalls = 0

    minimum_ncoins_lookup_table = [1] + [0]*amount


    for coin in coins:

        for i in range(coin,amount+1):

            diff = i - coin
            minimum_ncoins_lookup_table[i] = 1 + minimum_ncoins_lookup_table[diff]

            nCalls += 1


    result = {}
    result['nCalls'] = nCalls
    result['minimum_number_of_coins'] = minimum_ncoins_lookup_table[-1]

    return result
    



def recursive_algo_wrapper(coins, amount):

    nCalls = 0
    ncoin_counter = 0
    minimum_coins = float("inf")

    nAllCoins = len(coins)

    def recursive_algo(coins, amount):

        nonlocal ncoin_counter
        nonlocal nCalls
        nonlocal nAllCoins

        for i in range(0,nAllCoins):

            if (coins[i] < amount):

                return 0
        

    result = {'combinations': combinations, 'nCalls':nCalls}

    return result




def print_result(result):

    mininum_number_of_coins = result['minimum_number_of_coins']
    nCalls                  = result['nCalls']

    msg = "Minimum number of coins needed: {} | Number of calls: {}".format(mininum_number_of_coins, nCalls)
    print(msg)

