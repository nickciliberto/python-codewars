#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:19:52 2020

@author: nicholas
"""

def play_if_enough(hand, play):
    newHand = hand[:]
    for letter in play:
        if letter not in newHand:
            return (False, hand)
        else:
            index = newHand.index(letter)
            newHand = newHand[:index] + newHand[index+1:]
    return (True, newHand)