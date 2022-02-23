# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:41:45 2022

@author: patha
"""

import pandas as pd

def plan_trip(flights):
    dfflights = pd.DataFrame(flights, columns=['Start', 'End'])
    left_on_col = 'End'
    right_on_col = 'Start'
    dfflights_mod = dfflights.copy()
    for i in range(2, len(dfflights) + 1):
        dfflights_mod = dfflights_mod.merge(dfflights, left_on=[left_on_col],
                                            right_on=[right_on_col],
                                            how='inner', suffixes=['', '_%d' % i])
        left_on_col += '_%d' % i
    return [list(x) for x in dfflights_mod.iloc[0, :].values.reshape(len(flights), 2)]