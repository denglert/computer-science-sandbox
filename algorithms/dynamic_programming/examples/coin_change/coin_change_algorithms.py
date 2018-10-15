#!/usr/bin/env python

import math


def print_result(result):

    combinations = result['combinations']
    nCalls       = result['nCalls']

    msg = "Number of possible combinations: {} | Number of calls: {}".format(combinations, nCalls)
    print(msg)

def coin_change_recursion_brute_force(original_amount, coins):

    nCoins = len(coins)
    combinations = 0
    nCalls = 0

    def check_l_th_layer(amount, l):
        
        nonlocal combinations
        nonlocal nCalls

        nCalls += 1

        coin = coins[l]
    
        max_multiplier = int(math.floor(amount/coin))
        if max_multiplier == 0: return False
    
        for multiplier in range(max_multiplier+1):
    
    
            remaining_amount = amount - multiplier*coin
    
            if remaining_amount < 0:
                break
            elif remaining_amount == 0:
    
                combinations += 1
                break
    
            new_layer_index = l + 1
    
            if new_layer_index == nCoins:
                continue 
            if new_layer_index > nCoins:
                break
            else:
                check_l_th_layer(remaining_amount, new_layer_index)
    

    check_l_th_layer(original_amount, 0)

    result = {'combinations': combinations, 'nCalls':nCalls}

    return result



def coin_change_dynamic_programming(original_amount, coins):

    nCalls = 0

    # - Initializing combinations array
    combinations = [1] + [0 for i in range(original_amount)]

    # - Looping over the coins
    for coin in coins:
    
        # - Loop over amounts
        for amount in range(coin, original_amount+1):
    
            old_value = combinations[amount]  
            new_value = old_value + combinations[amount-coin]

            # - Update
            combinations[amount] = new_value

            nCalls += 1
    
    result = {'combinations': combinations[original_amount], 'nCalls' : nCalls}
    
    return result
