#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:43:13 2020

@author: nicholas
"""

def decomp(n):
    nFact = factorial(n)
    prime_list = primeNums(n)
    resultString = ''
    resultDict = {}
    while nFact > 1:
        for prime in prime_list:
            if nFact % prime == 0:
                resultDict[prime] = resultDict.get(prime, 0) + 1
                nFact /= prime
    for i in resultDict:
        if resultDict[i] == 1:
            resultString = resultString + str(i) + ' * '
        else:
            resultString = resultString + str(i) + 'ˆ' + str(resultDict.get(i)) + ' * '
    return resultString[:-3]
            
    
def factorial(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
    
def primeNums(n):
    prime_list = [2]
    for i in range(2,n):
        for prime in prime_list:
            if i % prime == 0:
                break
        else:
            prime_list.append(i)
    return prime_list

print(decomp(25))