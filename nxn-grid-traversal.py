# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:25:52 2022

@author: patha
"""

import math
def traverse_count(n):
    if n == 1:
        return 1
    return math.factorial(2*n - 2)/math.factorial(n - 1)**2