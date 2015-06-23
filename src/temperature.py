#! /bin/env python

"""This is a python module that converts temperature
"""

def f_to_k(temp):
    converted = ((temp-32.0)*(5.0/9.0)) + 273.15
    return converted

def k_to_c(temp)
    return temp-273.15

def f_to_c(temp)
    return k_to_c(f_to_k(temp))

print(f_to_k(212))
print(f_to_k(32))
