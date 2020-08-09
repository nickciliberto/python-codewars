#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 10:21:59 2020

@author: nicholas
"""

def stock_list(listOfArt, listOfCat):
    result_string  = ''
    for cat in listOfCat:
        counter = 0
        for art in listOfArt:
            if art[0] == cat:
                counter += int(art.split()[1])
        if counter > 0:
            if result_string == '':
                result_string = result_string + '({} : {})'.format(cat, counter)
            else:
                result_string = result_string + ' - ({} : {})'.format(cat, counter)
    return result_string

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c))