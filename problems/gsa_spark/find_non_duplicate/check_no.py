#!/usr/bin/env python
"""Membership checking is fast with the `set` collection since it uses a hash table."""

def check_for_unique_number(input_file):

    numbers = set()

    with open(input_file, 'r') as f:
        for i, line in enumerate(f):

            n = int(line)
            if not n in numbers:
                numbers.add(n)
            else:
                numbers.remove(n)
    
            if (i % 1000000) == 0:
                print(i)

    return numbers
    
input_file = './numbers.dat'
check_for_unique_number(input_file)
