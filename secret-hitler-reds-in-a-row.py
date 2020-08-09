# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

class Deck:
    def __init__(self, numBlues, numReds):
        deck = []
        for i in range(numBlues):
            deck.append('blue')
        for i in range(numReds):
            deck.append('red')
        self.deck = deck
    
    def drawCards(self, numCardsToDraw):
        choices = []
        for i in range(numCardsToDraw):
            choice = random.choice(self.deck)
            choices.append(choice)
            self.deck.remove(choice)
        return choices

def monteCarlo(numBlues, numReds, numCardsToDraw, numTrials, outcome):
    occurrences = 0
    blues = outcome.count('blue')
    for num in range(numTrials):
        deck = Deck(numBlues, numReds)
        draw = deck.drawCards(numCardsToDraw)
        if draw.count('blue') == blues:
            occurrences += 1
    return occurrences/numTrials

def probCalc(numBlues, numReds, numCardsToDraw):
    totalCards = numBlues + numReds
    probability = 1
    for i in range(numCardsToDraw):
        probability *= numReds/totalCards
        numReds -= 1
        totalCards -= 1
    return probability

def compareMethods(numBlues, numReds, numCardsToDraw, outcome, numTrials):
    monteResult = monteCarlo(numBlues, numReds, numCardsToDraw, numTrials, outcome)
    calcResult = probCalc(numBlues, numReds, numCardsToDraw)
    error = monteResult - calcResult
    return 'Simulation Probability: {}, Calculated Probability: {}, Difference: {}'.format(monteResult, calcResult, error)

numBlues = 2
numReds = 10
numCardsToDraw = 3
outcome = ['red', 'red', 'red']
numTrials = 100000

print(compareMethods(numBlues, numReds, numCardsToDraw, outcome, numTrials))
print(monteCarlo(numBlues, numReds, numCardsToDraw, numTrials, outcome))
