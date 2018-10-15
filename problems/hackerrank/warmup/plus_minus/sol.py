#!/usr/bin/env python

from utils import Timer
from fractions import Fraction

arr = [-4, 3, -9, 0, 4, 1]

@Timer(nloops=5)
def plusMinus(arr):

    n = len(arr)

    pos_counter = lambda t: sum(x > 0 for x in t)
    neg_counter = lambda t: sum(x < 0 for x in t)

    pos_counts = pos_counter(arr)
    neg_counts = neg_counter(arr)
    zer_counts = n - pos_counts - neg_counts

    pos_freq = Fraction(pos_counts, n)
    neg_freq = Fraction(neg_counts, n)
    zer_freq = Fraction(n-pos_counts-neg_counts, n)

    return float(pos_freq), float(neg_freq), float(zer_freq)


print(plusMinus(arr))


