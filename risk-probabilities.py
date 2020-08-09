#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:08:31 2020

@author: nicholas
"""

import random
import numpy as np
import pandas


def turn(attack_pieces, defend_pieces):
    '''
    Input: number of attacking die and defending die being rolled
    Output: Tuple showing how many attacking troops and defending troops were \
    lost (attacking_lost, defending_lost)
    '''
    attack_roll = []
    defend_roll = []
    for i in range(attack_pieces):
        attack_roll.append(random.randint(1,6))
    for i in range(defend_pieces):
        defend_roll.append(random.randint(1,6))
    attack_roll.sort(reverse=True)
    defend_roll.sort(reverse=True)
    attacks_lost = 0
    defense_lost = 0
    for i in range(min(len(attack_roll), len(defend_roll))):
        if attack_roll[i] > defend_roll[i]:
            defense_lost += 1
        else:
            attacks_lost += 1
    return (attacks_lost, defense_lost)

def one_turn_prob_calc(attack_pieces, defend_pieces, numTrials):
    '''
    Input: number of attacking die and defending die being rolled and number of trials
    Output: Three strings showing probability of each result
    '''
    attack_wins_both = 0
    defense_wins_both = 0
    one_and_one = 0
    
    for i in range(numTrials):
        result = turn(attack_pieces, defend_pieces)
        if result[0] == 0:
            attack_wins_both += 1
        elif result[1] == 0:
            defense_wins_both += 1
        else:
            one_and_one += 1
    return 'Attack Wins Both: {} \nDefense Wins Both: {} \nOne And One: {}'.format(attack_wins_both/numTrials, defense_wins_both/numTrials, one_and_one/numTrials)


def attack_simulation(attack_pieces, defense_pieces):
    '''
    Input: number of pieces attacking player is using to attack, number of \
    pieces defender is defending with
    Output: Return True if attack win, False if defense win
    '''
    while attack_pieces > 0 or defense_pieces > 0:
        if attack_pieces >= 3:
            x = 3
        else:
            x = attack_pieces
        if defense_pieces >= 2:
            y = 2
        else:
            y = defense_pieces
        result = turn(x, y)
        attack_pieces -= result[0]
        defense_pieces -= result[1]
        if attack_pieces == 0:
            return False
        if defense_pieces == 0:
            return True

def attack_prob_calc(attack_pieces, defense_pieces, numTrials):
    '''
    Input: number of pieces attacking player is using to attack, number of \
    pieces defender is defending with, number of trials
    Output: probability of attack win
    '''
    attack_wins = 0
    for num in range(numTrials):
        if attack_simulation(attack_pieces, defense_pieces) == True:
            attack_wins += 1
    return attack_wins/numTrials

def probability_matrix(max_pieces, numTrials):
    array = []
    for y in range(1, max_pieces+1):
        row = []
        for x in range(1, max_pieces+1):    
            row.append(attack_prob_calc(x, y, numTrials))
        array.append(row)
    matrix = np.array(array)
    row_labels = [x for x in range(1, max_pieces+1)]
    column_labels = row_labels[:]
    df = pandas.DataFrame(matrix, columns=column_labels, index=row_labels)
    return df

print(probability_matrix(10, 1000))
