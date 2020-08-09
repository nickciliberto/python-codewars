#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:02:26 2020

@author: nicholas
"""

def count_smileys(arr):
    '''
    input: a list of characters
    output: the number of valid smiley faces in the input list
    '''
    validEyes = [':', ';']
    validNose = ['-', '~']
    validMouth = [')', 'D']
    counter = 0
    for smiley in arr:
        if len(smiley) == 2:
            if smiley[0] in validEyes and smiley[1] in validMouth:
                counter += 1
        elif len(smiley) == 3:
            if smiley[0] in validEyes and smiley[1] in validNose and smiley[2] in validMouth:
                counter += 1
    return counter

a = []
b = [':D',':~)',';~D',':)']
c = [':)',':(',':D',':O',':;']
d = [';]', ':[', ';*', ':$', ';-D']

print(count_smileys(a), 0)
print(count_smileys(b), 4)
print(count_smileys(c), 2)
print(count_smileys(d), 1)