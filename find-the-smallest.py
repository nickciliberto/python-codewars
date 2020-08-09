#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:34:33 2020

@author: nicholas
"""

def smallest(n):
    small = int(n)
    oldPos = 0
    newPos = 0
    for index in range(len(str(n))):
        num = str(n)[:index] + str(n)[index + 1:]
        for i in range(len(str(n))):
            newNum = int(num[:i] + str(n)[index] + num[i:])
            if newNum < small:
                small = newNum
                oldPos = index
                newPos = i
    return [small, oldPos, newPos]


print(smallest(261235), [126235, 2, 0])
print(smallest(209917), [29917, 0, 1])
print(smallest(285365), [238565, 3, 1])
print(smallest(269045), [26945, 3, 0])
print(smallest(296837), [239687, 4, 1])
print(smallest(935855753), [358557539, 0, 8])
print(smallest(916684388991717682), [166843889917176829, 0, 17])

