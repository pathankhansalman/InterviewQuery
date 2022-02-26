# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:00:33 2022

@author: patha
"""

import numpy as np
def linear_regression(A):
    A_arr = np.array([np.array(x) for x in A])
    A_arr = A_arr.T
    X = A_arr[:-1, :].T
    X = np.hstack((X,np.ones([X.shape[0],1], X.dtype)))
    Y = A_arr[-1,:].T
    print(X)
    print(Y)
    beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, Y))
    print(beta)
    return ([list(x) for x in A_arr], beta)