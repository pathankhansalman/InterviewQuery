# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 13:54:49 2022

@author: patha
"""

import numpy as np


def simulate_overlap(n):
   over_count = 0
   for i in range(n):
      start_1 = np.random.randint(0, 300)
      start_2 = np.random.randint(0, 300)
      if (start_1 <= start_2 and start_2 <= start_1 + 60) or (start_2 <= start_1 and start_1 <= start_2 + 60):
         over_count += 1
   return (over_count/n)*365*1000
