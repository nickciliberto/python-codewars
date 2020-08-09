#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 12:55:04 2020

@author: nicholas
"""
def rolldice_sum_prob(sum_, dice_amount):
    import itertools
    rolls = 0
    totalRolls = 0
    for roll in itertools.product(range(1,7), repeat=dice_amount):
        totalRolls += 1
        rollSum = 0
        for num in roll:
            rollSum += num
        if rollSum == sum_:
            rolls += 1
    return rolls/totalRolls

print(rolldice_sum_prob(11, 2))