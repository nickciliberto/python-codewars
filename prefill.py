#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 17:16:31 2020

@author: nicholas
"""

def prefill(n,v = None):
    '''
    input n as int, v as any data type
    returns an array of n elements that all have the same value v.
    '''
    try:
        return int(n)*[v]
    except:
        raise TypeError("{} is invalid".format(n))
        