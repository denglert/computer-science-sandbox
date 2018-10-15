#!/usr/bin/env python

amount = 500
coins = [1,2,5,10,20,50,100,200]
combinations = [1]+[0]*amount

for coin in coins:
    for i in range(coin,amount+1):
        combinations[i] += combinations[i-coin]

#coin = 1
#for i in range(coin,amount+1):
#    combinations[i] += combinations[i-coin]
#
#print(combinations)
#
#coin = 1
#for i in range(coin,amount+1):
#    combinations[i] += combinations[i-coin]
#
#print(combinations)

print("Number of combinations: {}".format(combinations[amount]))
