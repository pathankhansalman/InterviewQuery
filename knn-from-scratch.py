# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:06:27 2022

@author: patha
"""

import numpy as np

def kNN(k,data,new_point):
    data_copy = data.copy()
    data_copy['Euclidean'] = 0
    for i in range(1, len(new_point) + 1):
        data_copy['Euclidean'] += (data_copy['Var%d' % i] -
                                   new_point[i - 1])**2
    data_copy['Euclidean'] = np.sqrt(data_copy['Euclidean'])
    curr_pt = k
    while curr_pt > 0:
        curr_data = data_copy.nsmallest(curr_pt, 'Euclidean')
        count_ser = curr_data['Target'].value_counts()
        count_ser = count_ser[count_ser == count_ser.max()].copy()
        if len(count_ser) > 1:
            curr_pt -= 1
            continue
        return count_ser.index[0]
