#!/usr/bin/env python

"""The “strength” of a number N is defined as the sum of all of N’s proper divisors, divided by N
itself.

A proper divisor of a positive integer N is any divisor of N other than N itself. 
The task is to find the number N_max from the interval [60000, 1000000] that has the highest
strength among all numbers in the interval.

A successful solution to this puzzle includes both the answer for this specific instance and the
Python code used to generally derive N_max for an arbitrary interval [A, B], where A and B are
non-negative integers."""


def primes(n):
    """A very crude prime factorisation algorithm. For larger number consider using a different
    algorithm (c.f. Sieve)
       Returns the prime factor decomposition of a number in a dictionary,
       stored as the [key=prime] : value=power."""

    # - List containig the prime factors
    primefactors_list = []

    # - Start with factorizing out 2s
    while (n % 2) == 0:
        primefactors_list.append(2)  # supposing you want multiple factors repeated
        n = n // 2

    # - First odd prime number (if we don't count 1)
    d = 3

    # - Finding the larger odd prime factors
    while d*d <= n:
        while (n % d) == 0:
            primefactors_list.append(d)  # supposing you want multiple factors repeated
            n = n // d
        d = d + 2

    # - If 'n' is still larger than 1, then it must be a prime: add it to the list
    if n > 1:
        primefactors_list.append(n)

    decomp = create_primefactor_decomp(primefactors_list)

    return decomp


def create_primefactor_decomp(primefactors_list):
    """Creates a dictionary from the list of prime factors in the format of:
       [key=prime] : value=power."""

    primefactor_decomp = {}
    
    for prime in primefactors_list:
        if not prime in primefactor_decomp:
            primefactor_decomp[prime] = 0

        primefactor_decomp[prime] += 1

    return primefactor_decomp
    

def get_number_from_prime_decomp(primefactor_decomp):
    """Calculates the original number from the primefactor decomposition."""

    n = 1

    for prime, power in primefactor_decomp.items():
        n = n * prime**power

    return n


def divisor_function(n):
    """The divisor function, sigma(n) is the sum of all divisors of n.
       We calculate sigma(n) using the prime factorization of the number, see
       http://mathworld.wolfram.com/DivisorFunction.html for reference."""

    p = primes(n)

    sigma = 1

    for prime, power in p.items():
        factor = (prime**(power+1) - 1)/(prime - 1)
        sigma = sigma * factor

    return sigma


def calc_strength(n):
    """Calculates the strength of a number 'n'.
    Strength is defined as the sum of all of 'n'’s proper divisors, divided by 'n' itself."""

    sum_of_all_proper_divisors = divisor_function(n) - n
    strength = sum_of_all_proper_divisors/n

    return strength


def find_highest_strength(min_int, max_int):
    """Finds the number with the highest strength between integers
    'min_int' and 'max_int'.
    Returns the number and its corresponding strength value."""

    n_with_s_max = -1
    s_max        = -1.0

    for n in range(min_int, max_int+1):

        s_current = calc_strength(n)

        if s_current > s_max:
            n_with_s_max = n
            s_max        = s_current

    return n_with_s_max, s_max


def test():
    """Test function, to validate the:
        - `primes()`
        - `divisor_function()`
        functions on some reference values."""
    n1 = 140
    p1 = primes(n1)
    n1_cs = get_number_from_prime_decomp(p1)
    sigma1 = divisor_function(n1)
    strength1   = calc_strength(n1)

    n2 = 16
    p2 = primes(n2)
    n2_cs = get_number_from_prime_decomp(p2)
    sigma2 = divisor_function(n2)
    strength2   = calc_strength(n2)

    n3 = 1000000
    p3 = primes(n3)
    n3_cs = get_number_from_prime_decomp(p3)
    sigma3 = divisor_function(n3)

    assert n1_cs == n1
    assert sigma1 == 336

    assert n2_cs == n2
    assert sigma2 == 31

    assert n3_cs == n3
    assert sigma3 == 2480437

    print('Test passed.')


test()

min_int = 60000
max_int = 1000000
n, s = find_highest_strength(min_int, max_int)
print("Interval: [{} - {}]".format(min_int, max_int))
print("Number with the highest strength: {}".format(n))
print("Strength value:                   {}".format(s))
