#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:37:30 2020

@author: nicholas
"""

def find_nb(m):
    '''
    determines value n such that nˆ3 + (n-1)ˆ3 + (n-2)ˆ3 ... 1ˆ3 = m
    input m as int
    return int
    returns -1 if no such n can be found
    '''
    volume = 0
    for i in range(1, m):
        volume += i**3
        if volume == m:
            return i
        if volume > m:
            return -1



n1 = 4183059834009
n2 = 24723578342962
n3 = 135440716410000
n4 = 40539911473216
n5 = 26825883955641



print(find_nb(n1), 2022)
print(find_nb(n2), -1)
print(find_nb(n3), 4824)
print(find_nb(n4), 3568)
print(find_nb(n5), 3218)