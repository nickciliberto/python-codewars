#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 11:04:16 2020

@author: nicholas
"""

def all_permuted(array_length):
    pass

array = [1, 2, 3, 4]

import itertools

counter = 0
for perm in itertools.permutations(array):
    counter += 1
    print(perm)
    
print(counter)