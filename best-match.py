#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:52:54 2020

@author: nicholas
"""

def best_match(goals1, goals2):
    minGoalDiff = goals1[0] - goals2[0]
    maxGoals = min(goals2)
    index = 0
    for i in range(len(goals1)):
        if goals1[i] - goals2[i] < minGoalDiff:
            minGoalDiff = goals1[i] - goals2[i]
            maxGoals = goals2[i]
            index = i
        elif goals1[i] - goals2[i] == minGoalDiff:
            minGoalDiff = goals1[i] - goals2[i]
            if goals2[i] > maxGoals:
                maxGoals = goals2[i]
                index = i
    return index

goals1 = [14, 5, 12, 16, 13, 13]
goals2 = [10, 2, 3, 10, 10, 3]

print(best_match(goals1, goals2))