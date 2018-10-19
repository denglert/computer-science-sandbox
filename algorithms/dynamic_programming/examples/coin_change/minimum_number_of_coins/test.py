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

#result = recursive_algo_wrapper(coins, amount)
#print("Recursive algo:")
#print_result(result)


################################################

amount = 20
coins = [1,2,3]

print("Amount: {}".format(amount))
print("Coins: {}".format(coins))

result = dp_algo(coins, amount)

print("DP algo:")
print_result(result)


################################################

amount = 11
coins = [1,5,6,9]

print("Amount: {}".format(amount))
print("Coins: {}".format(coins))

result = dp_algo(coins, amount)

print("DP algo:")
print_result(result)
