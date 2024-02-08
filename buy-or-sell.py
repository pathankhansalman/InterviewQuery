# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 15:43:59 2022

@author: patha
"""

def max_profit(stock_prices, dts):
    curr_min_price = stock_prices[0]
    curr_max_price = stock_prices[0]
    curr_min_idx = 0
    curr_max_idx = 0
    max_profit = -1
    for i in range(len(stock_prices)):
        if stock_prices[i] < curr_min_price:
            curr_min_price = stock_prices[i]
            curr_min_idx = i
            curr_max_price = stock_prices[i]
            curr_max_idx = i
        elif stock_prices[i] > curr_max_price:
            curr_max_price = stock_prices[i]
            curr_max_idx = i
        elif stock_prices[i] < curr_max_price:
            if curr_max_price - curr_min_price > max_profit:
                max_profit = curr_max_price - curr_min_price
            curr_min_price = stock_prices[i]
            curr_min_idx = i
            curr_max_price = stock_prices[i]
            curr_max_idx = i
    return max_profit, dts[curr_min_idx], dts[curr_max_idx]