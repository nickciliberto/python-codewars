#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:38:43 2020

@author: nicholas
"""

def stat(strg):
    '''
    input string of h|m|s times separated by commas
    output a string of range, mean, and median of times
    '''
    timeList = strg.split(',')
    secondsList = []
    for time in timeList:
        runnersTime = 0
        runnerList = time.split('|')
        for i in range(len(runnerList)):
            if i == 0:
                runnersTime += int(runnerList[i])*3600
            if i == 1:
                runnersTime += int(runnerList[i])*60
            if i == 2:
                runnersTime += int(runnerList[i])
        secondsList.append(runnersTime)
    runnerRange = rangeList(secondsList)
    runnerMean = mean(secondsList)
    runnerMedian = median(secondsList)
    finRange = formatSecs(runnerRange)
    finMean = formatSecs(runnerMean)
    finMedian = formatSecs(runnerMedian)
    result = 'Range: {} Average: {} Median: {}'.format(finRange, finMean, finMedian)
    return result
    
def formatSecs(a):
    '''
    input a as float, number of seconds
    converts seconds to hours, mins, seconds
    returns string in format h|m|s
    '''
    hours = int(a//3600)
    mins = int((a - (hours*3600))//60)
    secs = int(a - (hours*3600) - (mins*60))
    res = '{}|{}|{}'.format(addZero(hours), addZero(mins), addZero(secs))
    return res

def addZero(a):
    '''
    input a as int
    return str "0a"
    '''
    s = str(a)
    if a < 10:
        s = '0'+str(a)
    return s
    
def rangeList(a):
    '''
    input a is a list
    returns range (max - min) of values in list as float or int
    '''
    if a:
        return max(a) - min(a)

def mean(a):
    '''
    input a is a list
    returns average of all values in list as an float
    '''
    listSum = 0
    for num in a:
        listSum += num
    try:
        mean = listSum/len(a)
    except ZeroDivisionError:
        mean = None
    return mean

def median(a):
    '''
    input a is a list
    returns median of all values in list as an float
    '''
    a.sort()
    if len(a) == 1:
        return a[0]
    elif len(a) == 2:
        med = (a[0]+a[1])/2
        return med
    elif not a:
        return None
    else:
        return median(a[1:-1])
    
test1 = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"
test2 = "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"
print(stat(test1))
print(stat(test2))
