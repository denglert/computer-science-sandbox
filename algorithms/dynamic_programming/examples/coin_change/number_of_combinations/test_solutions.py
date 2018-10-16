#!/usr/bin/env python

from coin_change_algorithms import *


original_amount = 100
coins = [1,2,5,10]

print("Original amount: {}".format(original_amount))
print("Available coins: {}".format(coins))
print_result(coin_change_recursion_brute_force(original_amount=original_amount, coins=coins))
print_result(coin_change_dynamic_programming(original_amount=original_amount, coins=coins))
