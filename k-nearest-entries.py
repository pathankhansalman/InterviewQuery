# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:34:55 2022

@author: patha
"""

def nearest_entries(ints, N, k):
    min_diff = 999999999
    idx = -1
    for i, num in enumerate(ints):
        if abs(num - N) < min_diff:
            min_diff = abs(num - N)
            idx = i
    return ints[max(0, idx - k):min(len(ints), idx + k + 1)]