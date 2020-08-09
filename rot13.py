#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:11:35 2020

@author: nicholas
"""

import string

def rot13(message):
    shiftDict = createShiftDict(13)
    encryptedMessage = ''
    for char in message:
        if char in shiftDict:
            encryptedMessage = encryptedMessage + shiftDict[char]
        else:
            encryptedMessage = encryptedMessage + char
    return encryptedMessage

        
def createShiftDict(shift):
    shiftDict = {}
    for i in range(len(string.ascii_lowercase)):
        if i + shift <= 25:
            shiftDict[string.ascii_lowercase[i]] = string.ascii_lowercase[i + shift]
        else:
            shiftDict[string.ascii_lowercase[i]] = string.ascii_lowercase[(i+shift) - 26]
    for i in range(len(string.ascii_uppercase)):
        if i + shift <= 25:
            shiftDict[string.ascii_uppercase[i]] = string.ascii_uppercase[i + shift]
        else:
            shiftDict[string.ascii_uppercase[i]] = string.ascii_uppercase[(i+shift) - 26]
    return shiftDict
