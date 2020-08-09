#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:54:38 2020

@author: nicholas
"""

def max_sumDig(nMax, maxSum):
    numList = []
    for i in range(1000, nMax+1):
        digSum = 0
        for dig in str(i):
            digSum += int(dig)
        if digSum <= maxSum:
            numList.append(i)
    numSum = 0
    for num in numList:
        numSum += num
    mean = numSum/len(numList)
    res = 0
    for num in numList:
        if abs(mean - num) <= abs(mean - res):
            res = num
    return [len(numList), res, numSum]