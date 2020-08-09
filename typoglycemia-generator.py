#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:52:13 2020

@author: nicholas
"""

def scramble_words(words):
#    import string
    if words:
        wordList = words.split(' ')
        resultList = []
        for word in wordList:
            specialChars = []
            word_without_special_chars = ''
            for i in range(len(word)):
                if word[i] in "-',.":
                    specialChars.append(i)
                else:
                    word_without_special_chars = word_without_special_chars + word[i]
            if len(word_without_special_chars) == 1:
                resultString = word
            else:
                firstLetter = word_without_special_chars[0]
                lastLetter = word_without_special_chars[-1]
                sortedMiddle = ''.join(sorted(word_without_special_chars[1:-1]))
                resultString = str(firstLetter + sortedMiddle + lastLetter)
                for index in specialChars:
                    resultString = resultString[:index] + word[index] + resultString[index:]
            resultList.append(resultString)
        return ' '.join(resultList)
    else:
        return ''



print(scramble_words('professionals'), 'paefilnoorsss')
print()
print(scramble_words('i'), 'i')
print()
print(scramble_words(''), '')
print()
print(scramble_words('me'), 'me')
print()
print(scramble_words('you'), 'you')
print()
print(scramble_words('card-carrying'), 'caac-dinrrryg')
print()
print(scramble_words("shan't"), "sahn't")
print()
print(scramble_words('-dcba'), '-dbca')
print()
print(scramble_words('dcba.'), 'dbca.')
print()
print(scramble_words("you've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth."), "you've gotta dacne like teehr's nbdooy wachintg, love like ylo'ul neevr be hrut, sing like teehr's nbdooy leiinnstg, and live like it's haeevn on earth.")
