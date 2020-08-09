#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 13:34:12 2020

@author: barry
"""
from customExceptions import Empty

class arrayStack:
    def __init__(self):
        self._data = []
    
    def __len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]
    

