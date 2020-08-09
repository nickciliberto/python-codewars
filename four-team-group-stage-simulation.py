#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:24:42 2020

@author: nicholas
"""

import random
import itertools
import statistics
import matplotlib.pyplot as plt

def average_second_team(num_teams, num_trials, home_and_away = False):
    
    second_place_avg = []
    tied_avg = []
    
    for i in range(num_trials):
        second_place = []
        tied = []
        for i in range(1000):
            group = []
            for team in range(num_teams):
                group.append(0)
            
            def play_game(group, index_1, index_2):
                result = random.random()
                if result < 0.375:
                    group[index_1] += 3
                elif result > 0.625:
                    group[index_2] += 3
                else:
                    group[index_1] += 1
                    group[index_2] += 1
            
            if home_and_away == False:
                games = itertools.combinations(range(len(group)), 2)
            if home_and_away == True:
                games = itertools.permutations(range(len(group)), 2)
            
            for game in games:
                play_game(group, game[0], game[1])
            
            group.sort(reverse = True)
            if group[1] == group[2]:
                tied.append(group[1])
            else:
                second_place.append(group[1])
        if second_place:
            second_place_avg.append(statistics.mean(second_place))
        if tied:
            tied_avg.append(statistics.mean(tied))
    plt.hist(second_place_avg, bins = 12)
    plt.show()
    
#average_second_team(4, 1000)

def prob_advancing(num_teams, num_trials, num_points, home_and_away = False):

    second_place = []
    tied = []
    all_results = []
    
    for i in range(num_trials):
        group = []
        
        for team in range(num_teams):
            group.append(0)
        
        def play_game(group, index_1, index_2):
            result = random.random()
            if result < 0.375:
                group[index_1] += 3
            elif result > 0.625:
                group[index_2] += 3
            else:
                group[index_1] += 1
                group[index_2] += 1
        
        if home_and_away == False:
            games = itertools.combinations(range(len(group)), 2)
        if home_and_away == True:
            games = itertools.permutations(range(len(group)), 2)
        
        for game in games:
            play_game(group, game[0], game[1])
        
        group.sort(reverse = True)
        print(group)
        
        if any(team == num_points for team in group):
            all_results.append(num_points)    
        if group[1] == group[2]:
            tied.append(group[1])
        else:
            second_place.append(group[1])
    
    total = sum(map(lambda x : x == num_points, all_results))
    second_places = sum(map(lambda x : x == num_points, second_place))
    ties = sum(map(lambda x : x == num_points, tied))
    
    print(total)
    print(second_places)
    print(ties)
#    
#    prob_advancing = second_places / total
#    prob_tied = ties / total
#    prob_losing = 1 - prob_advancing - prob_tied
#    
#    print("Probability of Advancing: {}".format(prob_advancing), "\n",
#          "Probability of Tying: {}".format(prob_tied), "\n",
#          "Probability of Losing: {}".format(prob_losing))
            
prob_advancing(4, 100, 6)