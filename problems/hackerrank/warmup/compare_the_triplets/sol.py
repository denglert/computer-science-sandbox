#!/usr/bin/env python

import time
from utils import Timer

@Timer(nloops=5)
def compareTriplets_loop(a,b):
	
	a_pts = 0
	b_pts = 0

	for ai, bi in zip(a,b):
			
		if ai > bi:
			a_pts += 1
		elif ai < bi:
			b_pts += 1
		
	return [a_pts,b_pts]



@Timer(nloops=5)
def compareTriplets_map(a,b):

    return map(
        lambda t: sum([x > y for x, y in zip(*t)]), 
        ((a, b), (b, a))
        )


#####################################################


a = [17, 28, 30]
b = [99, 16, 8]


score = compareTriplets_loop(a, b)
print(score)

score = compareTriplets_map(a, b)
print(score)
