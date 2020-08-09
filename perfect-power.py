#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:29:05 2020

@author: nicholas
"""

def isPP(n):
    '''
    takes input n as integer, determines if n is a perfect power
    returns a list [m, k] such that mˆk = n
    if n is not perfect power returns None
    '''
    for m in range(2, int(n**1/2)+1):
        for k in range(2, int(n/2)+1):
            if m**k == n:
                return [m,k]
            elif m**k > n:
                break
n = 255
print(isPP(n))