#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 00:01:07 2020

@author: barry
"""

def binarySearch(Arr, val, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if val == Arr[mid]:
            return True
        elif val < Arr[mid]:
            return binarySearch(Arr, val, low, mid - 1)
        else:
            return binarySearch(Arr, val, mid + 1, high)
        
Arr = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(Arr, 7, 0, len(Arr) - 1))