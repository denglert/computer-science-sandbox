#!/usr/bin/env python


from algorithms import *


amount = 12
coins = [1,3,5]

print("Amount: {}".format(amount))
print("Coins: {}".format(coins))



### --- Dynamic programming --- ###
result = dp_algo(coins, amount)

print("DP algo:")
print_result(result)


### --- Recursive --- ###

result = recursive_algo(coins, amount)
print("Recursive algo:")
print_result(result)
