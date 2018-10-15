#!/usr/bin/env python

"""
Realising he would never know his hash-tables from his hat-stand, Bob got tired
of programming and decided to get a much more appropriate job as skydiving
instructor.

To his dismay, on his first day at work, he is presented with a maths problem.
 
Imagine that N humans are in the queue for a skydiving jump, naively placing
their lives in Bob’s incapable hands.

Every second, one of two possibilities occurs:

- The first human in the queue jumps from the aeroplane, with probability P
- The first human in the queue hesitates, making the other humans in the queue
wait, with probability (1 - P)

The i-th human in the queue cannot jump from the aeroplane until all humans
with indices 1 to (i - 1) have made the jump. Only one human can make the jump
each second.

Bob needs to calculate the expected value of the number of humans that have
jumped after T seconds.

Firmly aware of his own inadequacy pertaining to calculations of any kind, Bob
has come to you for help.

Compute the expected value of the number of humans that have jumped after t
seconds for N = 40, t = 20, P = 0.7.
"""

import random
import math


def comb(n,k):
    """Comb function: n!/(k! * (n-k)!)"""

    c = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    return c


def binom_pmf(x,n,p):
    """Binomial pmf"""
    pmf = comb(n,x) * p**x * (1.0-p)**(n-x)
    return pmf


def doJump(p=0.7):
    """Returns whether a human has jumped or not with probability p."""

    x = random.uniform(0,1.0)
    if x <= p:
    	return True
    if x > p:
    	return False


def get_nJumps(p=0.7, time=20, nHumans=40):
    """ Returns the number of jumps for a trial run, given:
        - p,
        - time
        - nHumans
    Only one human can make the jump each second.
    """

    nJumps = 0

    for attempt in range(time):

        hasJumped = doJump(p)
        if hasJumped:
            nHumans -= 1
            nJumps += 1

        if nHumans == 0:
            break

    return nJumps


def expected_nJumps_from_simulation(p=0.7,
                                    time=20,
                                    nHumans=40,
                                    experiments=10000):
    """Returns the expected mean of the jumps."""

    nJumps_ensemble = [get_nJumps(p, time, nHumans) for i in range(experiments)]
    nJumps_mean = sum(nJumps_ensemble)/len(nJumps_ensemble)
    
    return nJumps_mean


def expected_nJumps_formula(p=0.7,
                            time=20,
                            nHumans=40):
    

    nJumps_mean = 0

    if time <= nHumans:
        nJumps_mean = time * p
        return nJumps_mean

    if time > nHumans:
        """Only gives approximate number, might be prone to numerical errors due to comb()."""
        
        # - Everybody jumps except one
        for nJumps in range(nHumans): # - range goes from '0' to 'nHumans-1'
            nJumps_mean += binom_pmf(nJumps, time, p) * nJumps

        # - Everybody jumps
        for nTrials in range(nHumans, time+1): # - number of active trials
            nHesitations = (nTrials-nHumans)   # - number of times a person hesitates
            probability = comb(nTrials-1, nHesitations) * p**(nHumans) * (1.0-p)**(nHesitations)
            nJumps_mean += probability * nHumans
             
            # msg = "nTrials: {} nHesitations: {}".format(nTrials, nHesitations)
            # print(msg)

        return nJumps_mean


p = 0.7
time = 20
nHumans = 40
experiments = 10000

jumps_mean_exp_simu = expected_nJumps_from_simulation(p, time, nHumans, experiments)
jumps_mean_exp_form = expected_nJumps_formula(p, time, nHumans)

print("Expected number of jumps: {} (from direct simulation)".format(jumps_mean_exp_simu))
print("Expected number of jumps: {} (from Bernoulli distr)".format(jumps_mean_exp_form))
