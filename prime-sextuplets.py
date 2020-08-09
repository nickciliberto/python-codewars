#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:29:55 2020

@author: nicholas
"""

def find_primes_sextuplet(sum_limit):
    import sympy
    for prime in sympy.primerange(0, sum_limit):
        primelist = [prime, prime+4, prime+6, prime+10, prime+12, prime+16]
        primesum = 0
        for element in primelist:
            primesum += element
            if not sympy.isprime(element):
                break
        if primesum > sum_limit:
            return primelist
        
    
print(find_primes_sextuplet(70), [7, 11, 13, 17, 19, 23])
print(find_primes_sextuplet(600), [97, 101, 103, 107, 109, 113])
print(find_primes_sextuplet(2000000), [1091257, 1091261, 1091263, 1091267, 1091269, 1091273])