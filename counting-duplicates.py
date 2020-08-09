#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""

def duplicate_count(text):
    text = text.lower()
    counts = 0
    dups = ''
    for i in range(len(text)):
        letter = text[i]
        if letter in text[i+1:] and letter not in dups:
            counts += 1
            dups = dups + letter
    return counts

print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdea"), 1)
print(duplicate_count("indivisibility"), 1)