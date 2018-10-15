#!/usr/bin/env python

import numpy as np

a = np.random.randint(low=-1000, high=1000, size=10)
a1 = np.random.choice(a)
a2 = np.random.choice(a)
target = a1 + a2

print("a: {}".format(a))
print("a1: {}".format(a1))
print("a2: {}".format(a2))
print("target: {}".format(target))

def search_with_hash(a, target):

    elements_index_dict = {}

    for i, ai in enumerate(a):

        difference = target - ai

        if difference in elements_index_dict:

            j = elements_index_dict[difference]
            return i,j

        elements_index_dict[ai] = i


    print("Not found")
    return False, False



print("Searcing with hash algo...")
i,j = search_with_hash(a, target)

if i:
    print("i,j: {} {}".format(i,j))
    print("a[i], a[j]: {} {}".format(a[i],a[j]))
