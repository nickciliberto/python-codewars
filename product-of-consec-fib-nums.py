#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 09:10:04 2020

@author: nicholas
"""

#my solution

def gen_fib(num):
    fib_list = []
    for i in range(0, num+2):
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list

def productFib(prod):
    fib_list = gen_fib(prod)
    for x in range(len(fib_list)-1):
        
        if fib_list[x]*fib_list[x+1] < prod:
            pass
        
        elif fib_list[x]*fib_list[x+1] == prod:
            return [fib_list[x], fib_list[x+1], True]
            break
        
        elif fib_list[x]*fib_list[x+1] > prod:
            return [fib_list[x], fib_list[x+1], False]
            break

#best solution

def productFib2(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]

prod = 10
print('Calculating using your solution...')
print(productFib(prod))
print('Calculating efficient solution...')
print(productFib2(prod))