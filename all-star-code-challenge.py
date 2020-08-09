#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:19:11 2020

@author: nicholas
"""

def slogan_maker(array):
    import itertools
    words = list(set(array))
    slogans = []
    for slogan in itertools.permutations(words,len(words)):
        slogans.append(slogan)
    result = []
    for slogan in slogans:
        phrase = ''
        for word in slogan:
            phrase += '{} '.format(word)
        result.append(phrase[:-1])
    return list(set(result))

array = ["super", "guacamole", "super", "super", "hot", "guacamole"]
print(slogan_maker(array))            