#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i,j)

print(two_sum([1,2,3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))