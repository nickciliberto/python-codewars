#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""

def howmuch(m, n):
    ans = []
    for i in range (min(m,n),max(m,n)+1):
        if (i - 2)%7 == 0 and (i - 1)%9 == 0:
            ans.append(["M: {}".format(i), "B: {}".format(i//7), "C: {}".format(i//9)])
    return ans
    
    
print(howmuch(1, 37))