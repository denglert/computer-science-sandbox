#!/usr/bin/env python

import math
import numpy as np

#n = 1000000000
#n = 1000000000

m = 15
n = 1000000000

k = 5


iters = 1000

####################################################

dt = np.dtype(np.float64)

def prep_b():
    b = np.zeros(m - 1, dtype=dt)
    two = 1
    while two < m - 1:
        b[two - 1] = 0.5 / two
        two *= 2
    return b

def prep_A():
    A = np.zeros((m - 1, m - 1), dtype=dt)

    for i in range(m - 2):
        A[i + 1][i] = 1

    return A

def update_A(A, x):
    for i in range(m - 1):
        A[i][m - 2] = x[i]

    return A


def construct_B(A):

    B = np.zeros((m - 1, m - 1), dtype=dt)

    for i in range(k, 50):

        to_add = np.linalg.matrix_power(A, 2**(i-1) - m) / (2**i)
        B = np.add(B, to_add, dtype=dt)

    return B


####################################################
        
id = np.identity(m - 1, dtype=dt)

A = prep_A()
b = prep_b()
x = np.array(b, dtype=dt)

####################################################

print("A:\n{}".format(A))

for it in range(iters):

    A = update_A(A, x)

    B = construct_B(A)

    x = np.linalg.solve(id-B, b)

    if it == 0:

        print('----------')
        print("it: {}".format(it))
        print("A:\n{}".format(A))
        print("B:\n{}".format(B))
        print("x:\n{}".format(x))



p_loose          = np.dot(np.linalg.matrix_power(A, n - m), x).sum()
p_never_runs_out = 1.0 - p_loose

print('Finished iterating.')
print('----------')
print("b: {}".format(b))
print("x: {}".format(x))
print("p_loose: {}".format(p_loose))
print("p_never_runs_out: {}".format(p_never_runs_out))

#print("x: {}".format(x))
#print("{:.20f}".format(y))
