#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:21:48 2020

@author: barry
"""


def binarySearch(Arr, val):
    mini = 0
    maxi = len(Arr) - 1
    
    while mini <= maxi:
        middle = (mini + maxi) // 2
        
        if val == Arr[middle]:
            return True
        elif val < Arr[middle]:
            maxi = middle -1
        else:
            mini = middle + 1
    return False
        
Arr = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(Arr, 3))