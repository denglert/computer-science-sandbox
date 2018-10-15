#!/usr/bin/env python


import numpy as np

x = np.random.randint(low=1112, high=91231, size=1)[0]

print(x)

def reverse_integer(x):
    s = str(abs(x))
            
    print(s[::-1])
    reversed = int(s[::-1])
    
    if reversed > 2147483647:
        return 0
    
    return reversed if x > 0 else (reversed * -1)

reverse_integer(x)
