#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:46:30 2020

@author: barry
"""

def factorial(num):
    if num > 1:
        return num * factorial(num-1)
    elif num == 1:
        return num
    else:
        return "not possible"
    
for number in range(99):
    print(factorial(number))
    print("------------------------------------------------------------------")