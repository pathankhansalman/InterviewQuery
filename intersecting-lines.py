# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:44:04 2022

@author: patha
"""

def find_intersecting(tuple_list,x_range):
    y_range = [(y[0]*x_range[0] + y[1], y[0]*x_range[1] + y[1])
                for y in tuple_list]
    int_list = []
    for i, y1 in enumerate(y_range):
        for j, y2 in enumerate(y_range):
            if j <= i:
                continue
            if y1[0] == y2[0] or y1[1] == y2[1] or\
                ((y1[0] < y2[0] and y1[1] > y2[1]) or
                    (y1[0] > y2[0] and y1[1] < y2[1])):
                if tuple_list[i] not in int_list:
                    int_list.append(tuple_list[i])
                if tuple_list[j] not in int_list:
                    int_list.append(tuple_list[j])
    return int_list