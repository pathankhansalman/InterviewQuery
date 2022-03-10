# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 20:52:23 2022

@author: patha
"""

import pandas as pd

def customer_analysis(customers_df):
    customers_df.loc[:, 'Date of Sale'] = pd.\
        to_datetime(customers_df['Date of Sale'],
                    format='%Y-%m-%d')
    dfgroup = customers_df.groupby(['customer_id', 'Gender'])['Date of Sale'].\
        agg(['last', 'count']).reset_index()
    dfgroup.columns = ['customer_id', 'gender',
                       'most_recent_sale', 'order_count']
    dfgroup['most_recent_sale'] = dfgroup['most_recent_sale'].dt.strftime('%Y-%m-%d')
    return dfgroup