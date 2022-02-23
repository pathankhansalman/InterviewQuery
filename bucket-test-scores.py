# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:46:39 2022

@author: patha
"""

import numpy as np

def bucket_test_scores(df):
    for i in [50, 75, 90, 100]:
        df.loc[:, '<%d' % i] = df.loc[df['test score'] <= i, 'test score'].copy()
    df = df.groupby('grade').count()
    df = df.loc[:, ['<50', '<75', '<90', '<100']].copy()
    df.columns.name = 'test score'
    df = np.floor((100*df.div(df['<100'], axis=0))).astype(int)
    df = df.stack().to_frame('percentage').reset_index()
    df['percentage'] = df['percentage'].astype('str') + '%'
    return df