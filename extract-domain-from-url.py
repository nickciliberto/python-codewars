#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:18:42 2020

@author: nicholas
"""

def domain_name(url):
    beg = url.find('www.') + 4
    if beg == 3:
        beg = (url.find('://')+3)
    end = url[beg:].find('.')+beg
    return url[beg:end]

url1 = "http://google.com"
url2 = "http://google.co.jp"
url3 = "www.xakep.ru"
url4 = "https://youtube.com"
url5 = "http://github.com/carbonfive/raygun"
url6 = "http://www.zombie-bites.com"
url7 = "https://www.cnet.com"


print(domain_name(url1))
print(domain_name(url2))
print(domain_name(url3))
print(domain_name(url4))
print(domain_name(url5))
print(domain_name(url6))
print(domain_name(url7))