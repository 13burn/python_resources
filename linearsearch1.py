#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:31:21 2020

@author: barry
"""

def linearSearch(a, key):
    position = 0
    flag = False
    
    while position < len(A) and not flag:
        if A[position] == key:
            flag = True
        else:
            position = position + 1
    return flag

A = [84,21,47,96,15]
result = linearSearch(A, 96)
print(result)