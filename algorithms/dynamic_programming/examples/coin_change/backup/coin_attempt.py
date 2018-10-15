#!/usr/bin/env python

import math

# - Full
#coins = [1,2,5,10,20,50,100,200]
#to_be_broken = 500

# - Test
coins = [5,1,2]
to_be_broken = 10

combinations = [1] + [0 for i in range(to_be_broken)]

print("--- Initialization ---")
print(combinations)
print("Length of the combinations: {}".format(len(combinations)))


# - Looping over the coins
for coin in coins:

    updated_combinations = list(combinations)

    # - Loop over amounts
    for amount in range(coin, to_be_broken+1):

        new_value = combinations[amount]  

        max_multiplier = int(math.floor(amount/coin))

        # - Loop over possible multipliers
        for multiplier in range(1,max_multiplier+1):
            
            remaining_amount = amount - multiplier*coin
            new_value = new_value + combinations[remaining_amount]

#           msg = "coin: {} amount: {} max_multiplier: {} multiplier: {} remaining_amount: {} new_value: {}".format(coin, amount, max_multiplier, multiplier, remaining_amount, new_value)
#           print(msg)

        updated_combinations[amount] = new_value

    combinations = list(updated_combinations)


print('--- Result ---')
print(combinations)
