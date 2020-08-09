#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""


def mixed_fraction(s):
    import fractions
    l = s.split('/')
    numerator = int(l[0])
    denominator = int(l[1])
    if numerator * denominator < 0:
        sign = '-'
    else:
        sign = ''
    a = abs(numerator)//abs(denominator)
    remainder = str(fractions.Fraction(abs(numerator)%abs(denominator),abs(denominator)))
    if a == 0 and remainder == '0':
        result = '0'
    elif a == 0:
        result = remainder
    elif remainder == '0':
        result = '{}'.format(a)
    else:
        result = '{} {}'. format(a, remainder)
    return sign + result
    

print(mixed_fraction('6/3'))
print(mixed_fraction('4/6'))
print(mixed_fraction('0/6'))
print(mixed_fraction('-10/7'))