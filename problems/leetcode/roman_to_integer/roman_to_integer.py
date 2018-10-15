#!/usr/bin/env python

# I   1
# V   5
# X   10
# L   50
# C   100
# D   500
# M   1000


roman_string = "MIV"
print("Roman: {}".format(roman_string))


def parse_roman_string(str):
   

    numbers = []
    signs = []
   
    for ch in str:
      
        n = roman_to_number(ch)
        numbers.append(n)

      
    for i,n in enumerate(numbers[:-1]):

        if n < numbers[i+1]:
            sign = -1
        else:
            sign = 1

        signs.append(sign)

    signs.append(1)
       
    total = 0
    
    for s,n in zip(signs, numbers):
        total += s * n
    
    return total
      

def roman_to_number(ch):
   
    if ch == "I":
        return 1 
    elif ch == "V":
        return 5
    elif ch == "X":
        return 10
    elif ch == "L":
        return 50
    elif ch == "C":
        return 100
    elif ch == "D":
        return 500
    elif ch == "M":
        return 1000


numeric = parse_roman_string(roman_string)
print("Numeric: {}".format(numeric))
