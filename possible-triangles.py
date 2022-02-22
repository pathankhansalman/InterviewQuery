# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 22:23:51 2022

@author: patha
"""

def possible_triangles(sides):
    def _pos_tri_helper_(arg):
        def _bin_search_(val, sub_arg, left):
            if len(sub_arg) == 1:
                return 0
                if val > sub_arg[0]:
                    return 1
                else:
                    if left:
                        return 0
                    else:
                        return 1
            if len(sub_arg) == 2:
                if val <= sub_arg[0]:
                    return 0
                if val > sub_arg[1]:
                    return 1
                else:
                    if left:
                        return 0
                    else:
                        return 1
            mid_idx = int(len(sub_arg)/2)
            if sub_arg[mid_idx] == val:
                if left:
                    return mid_idx - 1
                else:
                    return mid_idx + 1
            elif val < sub_arg[mid_idx]:
                if val > sub_arg[mid_idx - 1]:
                    if left:
                        return mid_idx - 1
                    else:
                        return mid_idx
                else:
                    return _bin_search_(val, sub_arg[0:mid_idx], left)
            else:
                if val < sub_arg[mid_idx + 1]:
                    if left:
                        return mid_idx
                    else:
                        return mid_idx + 1
                else:
                    return mid_idx + _bin_search_(val, sub_arg[mid_idx:], left)
        if len(arg) < 3:
            return 0
        if len(arg) == 3:
            if arg[0] > abs(arg[1] - arg[2]) and\
                    arg[0] < arg[1] + arg[2]:
                return 1
            return 0
        curr_val = arg[0]
        count_tr = 0
        for j in range(len(arg[1:]) - 1):
            sum_val = curr_val + arg[1:][j]
            diff_val = abs(curr_val - arg[1:][j])
            min_idx = _bin_search_(diff_val, arg[1:][j+1:], left=False)
            max_idx = _bin_search_(sum_val, arg[1:][j+1:], left=True)
            if max_idx == min_idx:
                if arg[1:][j+1:][max_idx] >= sum_val or\
                        arg[1:][j+1:][max_idx] <= diff_val:
                    continue
            count_tr += (max_idx - min_idx + 1)
        return count_tr + _pos_tri_helper_(arg[1:])
    return _pos_tri_helper_(sorted(sides))
