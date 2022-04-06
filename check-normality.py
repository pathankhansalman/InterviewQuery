# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 17:58:26 2022

@author: patha
"""

import numpy as np

def solution():
    mean = np.mean(arg)
    stdev = np.std(arg)
    n = len(arg)
    if len(arg[(arg >= (mean - stdev)) &
               (arg <= (mean + stdev))])/n <= 0.68 and\
       len(arg[(arg >= (mean - 2*stdev)) &
               (arg <= (mean + 2*stdev))])/n <= 0.95 and\
       len(arg[(arg >= (mean - 3*stdev)) &
               (arg <= (mean + 3*stdev))])/n <= 0.9997:
        return 0
    return 1

arg = np.array([1, 2, 3, 4, 5])