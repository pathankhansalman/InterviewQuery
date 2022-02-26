# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 23:15:21 2022

@author: patha
"""

def cheese_median(df_cheeses):
    return df_cheeses.fillna(df_cheeses['Price'].median())
