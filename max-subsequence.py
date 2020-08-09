#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:39:15 2020

@author: nicholas
"""

def max_sequence(arr):
    sum = 0
    max_list = [0]
    for i in range(len(arr)):
        temp_list = [0]
        temp_sum = arr[i]
        for j in range(i+1,len(arr)):
            temp_sum += arr[j]
            temp_list.append(temp_sum)
        max_list.append(max(temp_list))
    sum = max(max_list)
    return sum

arr = []
arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(max_sequence(arr))
print(max_sequence(arr2))

