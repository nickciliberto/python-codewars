#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:55:04 2020

@author: nicholas
"""
def reg_sum_hits(n, s):
    import itertools
    rollDict = {}
    for roll in itertools.product(range(1,s+1), repeat=n):
        rollSum = 0
        for num in roll:
            rollSum += num
        rollDict[rollSum] = rollDict.get(rollSum,0) + 1
    sum_hits = []
    for roll, occurences in rollDict.items():
        sum_hits.append([roll, occurences])
    return sum_hits
