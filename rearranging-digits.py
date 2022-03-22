# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 00:06:17 2022

@author: patha
"""

import itertools
def rearranging_digits(n):
    n_list = list(n)
    perm_list = list(itertools.permutations(n_list))
    perm_list = sorted(perm_list, key=lambda x: ''.join(x))
    if ''.join(perm_list[-1]) == n:
        return None
    for num in perm_list:
        if int(''.join(num)) > int(n):
            return ''.join(num)