#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:48:55 2020

@author: nicholas
"""

def list_squared(m, n):
    results = []
    for num in range(m, n+1):
        divisors = [1, num]
        for i in range(2,num//2+1):
            if num % i == 0:
                divisors.append(i)
        for i in range(len(divisors)):
            divisors[i] = divisors[i]**2
        sumOfDivisors = 0
        for divisor in divisors:
            sumOfDivisors += divisor
        if is_square(sumOfDivisors):
            results.append([num, sumOfDivisors])
    return results
    
def is_square(n):
    i = 0
    while i**2 <= n:
        if i**2 == n:
            return True
        elif i**2 < n:
            i += 1
    return False


print(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
print(list_squared(42, 250), [[42, 2500], [246, 84100]])
print(list_squared(250, 500), [[287, 84100]])