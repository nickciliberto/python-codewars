#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""

def highest_rank(arr):
    s = set(arr)
    highest_count = 0
    most_freq = min(arr)-1
    for num in s:
        count = arr.count(num)
        if count >= highest_count and num > most_freq:
            highest_count = arr.count(num)
            most_freq = num
    return most_freq




print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]), 12)
print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 10]), 10)