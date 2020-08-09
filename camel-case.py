#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 13:15:50 2020

@author: nicholas
"""

def kebabize(string):
    from string import ascii_lowercase, ascii_uppercase
    kebab = ''
    for letter in string:
        if letter in ascii_lowercase:
            kebab = kebab + letter
        elif letter in ascii_uppercase:
            if not kebab:
                kebab = kebab + letter.lower()
            else:
                kebab = kebab + '-' + letter.lower()
    return kebab

string = '6ZjpRFn9tM9L767D'
print(kebabize(string))