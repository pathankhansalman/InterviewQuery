# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 23:28:03 2022

@author: patha
"""

import itertools
def combinational_dice_rolls(n,m):
    return list(itertools.product(*[list(range(1, m + 1)) for i in range(n)]))
