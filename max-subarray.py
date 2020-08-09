#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:40:14 2020

@author: nicholas
"""

def find_subarr_maxsum(arr):
    maxSum = 0
    maxSub = []
    for i in range(len(arr)):
        currentSum = arr[i]
        currentSub = [arr[i]]
        for j in range(i+1, len(arr)):
            currentSum += arr[j]
            currentSub.append(arr[j])
            if currentSum > maxSum:
                maxSum = currentSum
                maxSub.clear()
                maxSub.append(currentSub[:])
            elif currentSum == maxSum:
                maxSub.append(currentSub[:])
    if len(maxSub) == 1:
        return [maxSub[0], maxSum]
    else:
        return [maxSub, maxSum]

print(find_subarr_maxsum([-3, -9, -8, 7, -9, 0, 9, 7, 0, 1, 5, 6, -10, 0, 4, -5, -2, 5, 7, -2]))