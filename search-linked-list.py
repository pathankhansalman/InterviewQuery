# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:25:52 2022

@author: patha
"""

def search_list(linked_list, target):
    curr = linked_list.headval
    while curr != None:
        if curr.dataval == target:
            return True
        curr = curr.nextval
    return False