#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""


import string

def is_pangram(s):
    s = s.lower()
    counter = 0
    for i in string.ascii_lowercase:
        if i in s:
            counter += 1
    if counter == len(string.ascii_lowercase):
        return True
    else:
        return False
    
pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))