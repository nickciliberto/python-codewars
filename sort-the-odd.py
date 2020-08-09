#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""

def sort_array(source_array):
    odds_list = []
    for num in source_array:
        if num%2 != 0:
            odds_list.append(num)
    odds_list.sort(reverse=True)
    for i in range(len(source_array)):
        num = source_array[i]
        if num%2 != 0:
            source_array[i] = odds_list.pop()
    return source_array
    





print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]),[])