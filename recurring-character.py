# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:44:12 2022

@author: patha
"""

def recurring_char(input):
    mydict = set()
    for curr_chr in input:
        if curr_chr in mydict:
            return curr_chr
        mydict.add(curr_chr)
    return None